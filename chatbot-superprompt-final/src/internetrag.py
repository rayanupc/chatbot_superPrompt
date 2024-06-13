import openai
import spacy
from googlesearch import search
import config

SPACY_LLM = config.SPACY_LLM

# dictionnaire pour stocker les réponses
database = {}


def stocker_reponse(question, answer):
    """
    Stocke une réponse dans la base de données.
    Args:
        question (str): La question.
        answer (str): La réponse correspondante.
    """
    normalized_question = question.strip().lower()
    normalized_answer = answer.strip().lower()
    database[normalized_question] = normalized_answer


def query_chatgpt(request, url, responses_list):
    """
    Interroge le modèle GPT-3.5 à visiter un site et répondre à une requête.
    Args:
        request (str): La requête à soumettre au modèle.
        url (str): L'URL à examiner pour obtenir plus d'informations.
        responses_list (list): Une liste pour stocker les réponses obtenues.
    Returns:
        str: La réponse générée par le modèle GPT-3.5.
    """
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"Agis comme un expert de la recherche sur internet et examine l'url {url}, affiche le passage où se trouve la réponse à la question de l'utilisateur puis extrait la réponse, mais n'utilise pas tes connaissances "},
            {"role": "user", "content": request},
            {"role": "assistant", "content": "d'accord"} 
        ],
    )
    answer = response.choices[0].message.content.strip()
    responses_list.append(answer)
    return answer


def most_relevant(query, responses_list):
    """
    Sélectionne la réponse la plus pertinente parmi celles générées.
    Args:
        query (str): La requête initiale.
        responses_list (list): Une liste contenant les réponses générées.
    Returns:
        str: La réponse la plus pertinente.
    """

    #On lui rédige l'historique de ce qu'il s'est passé auparavant
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system", "content":"En tant qu'expert en recherche sur Internet, ta mission consiste à explorer les sites de manière efficace pour extraire la réponse la plus pertinente à la question posée. Nous sommes le 22 avril 2024, lorsque je te soumis une question, j'attends une réponse actualisée au maximum. Ton processus commence par visiter le site, tu récupères les informations nécessaires sur le site et les présentes de manière claire et concise en réponse à ma requête, ainsi tu affiches l'url et la réponse. Toutefois, il est important de noter que, dans ce processus, te ne te fies pas à tes connaissances internes, mais tu t'appuie essentiellement sur les données disponibles en ligne pour garantir une réponse précise et à jour."},
            {"role": "user", "content": query},
            {"role": "assistant", "content": " ".join(responses_list)},
            {"role":"system", "content": "Évalue les réponses selon la question posée, sélectionne la plus pertinente et la plus récente provenant d'un site reconnu et fiable, en examinant attentivement la fiabilité de chaque source."},
            {"role": "user", "content": " ".join(responses_list)}
        ],
    )
    res = response.choices[0].message.content.strip()
    stocker_reponse(query, res)
    return res


def question_existante(question, threshold):
    """
    Vérifie si une question existe déjà dans la base de données.
    Args:
        question (str): La question à vérifier.
        threshold (float): Le seuil de similarité pour considérer une question comme existante.

    Returns:
        str: La réponse correspondante si la question existe déjà dans la base de données, sinon None.
    """
    normalized_question = question.strip().lower()
    for key in database.keys():
        if nlp(normalized_question).similarity(nlp(key)) > threshold:
            return database[key]
    return None


def rag_manager(query, apikey):
    """
    Gère la recherche et la récupération des réponses en fonction de la question.
    Args:
        query (str): La question à traiter.
    """
    print("rag_manager():")
    openai.api_key = apikey
    # Chargement du modèle de langage français de spaCy
    nlp = spacy.load(SPACY_LLM)
    res = question_existante(query, 0.85)
    result = ""
    if res is not None:
        print("Réponse trouvée dans la base de données.")
        print("La réponse:", res)
        result = res
    else:
        print("La réponse n'existe pas dans la base de données. Recherche sur Internet en cours...")
        responses_list = []
        for url in search(query, tld="co.in", num=8, stop=8, pause=2):
            query_chatgpt(query, url, responses_list)
        relevant_answer = most_relevant(query, responses_list)
        print(f"La réponse la plus pertinente: {relevant_answer}")
        result =  relevant_answer
    return result


def main():
    query = input("votre question: ")
    rag_manager(query)