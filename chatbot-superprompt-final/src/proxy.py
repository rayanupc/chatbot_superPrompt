import os
from litellm import completion
from typing import List, Dict
import spacy
import warnings
import openai
import re
import math
from difflib import SequenceMatcher
from collections import Counter
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from fuzzywuzzy import fuzz
import time

import config

# Définition de l'environnement pour accéder aux API
os.environ['HUGGINGFACEHUB_API_TOKEN'] = config.HUGGINGFACEHUB_API_TOKEN
SPACY_LLM = config.SPACY_LLM

def generic_model_request(model: str, messages: List[Dict[str, str]], api_base: str) -> List[str]:
    """
    Effectue une requête générique à un modèle d'IA spécifié.
    Args:
        model (str): Le nom du modèle à utiliser.
        messages (List[Dict[str, str]]): Liste de messages pour la conversation.
        api_base (str): URL de base de l'API, le cas échéant.
        memory (ConversationMemory): Objet de la mémoire de la conversation.
    Returns:
        str:  réponse du modèle.
    """
    # Appelle le modèle d'IA pour générer une réponse
    response = completion(
        model=model,
        messages=messages,
        api_base=api_base,
    )
    return [x.message.content for x in response.choices]


def get_response_llama(query, messages):
    """
    Obtient la réponse du modèle Llama pour une requête donnée.
    Args:
        query (str): La requête pour laquelle obtenir une réponse.
        memory (ConversationMemory): L'instance de la mémoire de la conversation.
    Returns:
        str: La réponse générée par le modèle Llama.
    """
    os.environ["TOGETHER_AI_API_KEY"] = config.TOGETHER_AI_API_KEY
    messages.append({"role": "user", "content": query})
    response = generic_model_request (
        model="together_ai/togethercomputer/llama-2-70b-chat",
        messages=messages,
        api_base=None
    )
    return response[0]


def get_response_chatgpt(query, messages):
    """
    Obtient la réponse du modèle ChatGPT pour une requête donnée.
    Args:
        query (str): La requête pour laquelle obtenir une réponse.
        memory (ConversationMemory): L'instance de la mémoire de la conversation.
    Returns:
        str: La réponse générée par le modèle ChatGPT.
    """
    messages.append({"role": "user", "content": query})
    response = generic_model_request(
        model="gpt-3.5-turbo",
        messages=messages,
        api_base=None
    )
    return response[0]


def get_response_mistral(query, messages):
    """
    Obtient la réponse du modèle Mistral pour une requête donnée.
    Args:
        query (str): La requête pour laquelle obtenir une réponse.
        memory (ConversationMemory): L'instance de la mémoire de la conversation.
    Returns:
        str: La réponse générée par le modèle Mistral.
    """
    os.environ['HUGGINGFACEHUB_API_TOKEN'] = config.HUGGINGFACEHUB_API_TOKEN
    messages.append({"role": "user", "content": query})
    # Adaptation du format de la requête au llm Mistral
    messages_text = "\n".join(f"{message['role']}: {message['content']}" for message in messages)
    response = generic_model_request(
        model="huggingface/mistralai/Mistral-7B-Instruct-v0.1",
        messages=[{"role": "user", "content": messages_text}],
        api_base="https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
    )
    return response[0]


def get_response_coral(query, messages):
    """
    Obtient la réponse du modèle Coral pour une requête donnée.
    Args:
        query (str): La requête pour laquelle obtenir une réponse.
        memory (ConversationMemory): L'instance de la mémoire de la conversation.
    Returns:
        str: La réponse générée par le modèle Coral.
    """
    os.environ["COHERE_API_KEY"] = config.COHERE_API_KEY
    messages.append({"role": "user", "content": query})
    # Adaptation du format de la requête au llm Cohere Coral
    messages_text = "\n".join(f"{message['role']}: {message['content']}" for message in messages)
    response = generic_model_request(
        model="cohere/command-nightly",
        messages=[{"role": "user", "content": messages_text}],
        api_base=None
    )
    return response[0]


def calculate_similarity(original_response, returned_response):
    """
    Calcule la similarité entre deux réponses à l'aide du score de similarité de fuzz.
    Args:
        original_response (str): La réponse originale.
        returned_response (str): La réponse retournée par le modèle.
    Returns:
        float: Le score de similarité entre les deux réponses.
    """
    return fuzz.ratio(original_response, returned_response)  # Utilise la méthode ratio pour calculer la similarité


def best_response_chatgpt(query, models_responses): 
    """
    Sélectionne la meilleure réponse parmi plusieurs réponses en fonction de leur pertinence par rapport à la requête initiale.
    Args:
        query (str): La requête initiale pour laquelle les réponses sont évaluées.
        models_responses (dict): Un dictionnaire contenant les réponses, où les clés sont les noms des modèles et les valeurs sont les réponses associées.
    Returns:
        tuple: Un tuple contenant le nom du meilleur modèle et sa réponse associée.
    """

    best_model = None
    best_response = None
    best_similarity = 0

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system", "content":"Réponds uniquement à la requete comme un expert dans le domaine"},
            {"role": "user", "content": query},
            {"role": "assistant", "content": " ".join(models_responses.values())},
            {"role":"system", "content": "Tu es un évaluateur de la pertinence des réponses, tu dois seulement renvoyer la réponse qui te semble etre la plus pertinente selon la question qui a été posée. Je te donne deux exemples pour que tu apprennes à faire l'évaluation. Exemple 1 : la question est 'Qui est le premier ministre de la france?', la première réponse: 'Le premier ministre est Gabriel Attal depuis le 9 janvier 2024' la deuxième réponse: 'Le premier ministre de la France en 2023 est Elisabeth Borne.'. Donc la réponse la plus pertinente est la première donc tu réponds en la renvoyant 'Le premier ministre est Gabriel Attal depuis le 9 janvier 2024'.  Exemple 2: la question est 'En quelle date a commencé la première guerre mondiale?', la première réponse: 'La première guerre mondiale a eu lieu en 1940', la deuxième réponse: 'La seconde guerre mondiale a eu lieu en 1914'. Donc la réponse la plus pertinente est la deuxième alors tu réponds par 'La seconde guerre mondiale a eu lieu en 1914'. Tu fais pareil pour ce qu'on te demande "},
            {"role": "user", "content": " ".join(models_responses.values())}
            ],
    )
    
    returned_response = response.choices[0].message.content.strip()

    for response in models_responses.values():
        similarity = calculate_similarity(response, returned_response)

        if similarity > best_similarity: 
            best_similarity = similarity
            best_response = response

    for key in models_responses.keys():
        if models_responses[key] == best_response:
            best_model = key
    
    return best_model, best_response


def evaluate_qa_pair(question, answer):
    """
    Évalue la qualité d'une paire question-réponse.
    Args:
        question (str): La question.
        answer (str): La réponse.
    Returns:
        float: Le score d'évaluation de la paire.
    """
    tokenizer = AutoTokenizer.from_pretrained("iarfmoose/bert-base-cased-qa-evaluator")
    model = AutoModelForSequenceClassification.from_pretrained("iarfmoose/bert-base-cased-qa-evaluator") 

    inputs = tokenizer(question, answer, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)

    scores = outputs.logits.squeeze().tolist()
    score = max(scores)
    return score


def best_response_llama(query, models_responses):
    """
    Détermine la meilleure réponse générée par le modèle Llama.
    Args:
        responses (List[str]): Une liste de réponses générées par le modèle Llama.
    Returns:
        str: La meilleure réponse générée par le modèle Llama.
    """
    os.environ["TOGETHER_AI_API_KEY"] = config.TOGETHER_AI_API_KEY
    llama2_messages = generic_model_request(
        model="together_ai/togethercomputer/llama-2-70b-chat",
        messages=[
            {"role":"system", "content":"Réponds uniquement à la requete comme un expert dans le domaine"},
            {"role": "user", "content": query},
            {"role": "assistant", "content": " ".join(models_responses.values())},
            {"role":"system", "content": "Tu es un évaluateur de la pertinence des réponses, tu dois seulement renvoyer la réponse qui te semble etre la plus pertinente selon la question qui a été posée. Je te donne deux exemples pour que tu apprennes à faire l'évaluation. Exemple 1 : la question est 'Qui est le premier ministre de la france?', la première réponse: 'Le premier ministre est Gabriel Attal depuis le 9 janvier 2024' la deuxième réponse: 'Le premier ministre de la France en 2023 est Elisabeth Borne.'. Donc la réponse la plus pertinente est la première donc tu réponds en la renvoyant 'Le premier ministre est Gabriel Attal depuis le 9 janvier 2024'.  Exemple 2: la question est 'En quelle date a commencé la première guerre mondiale?', la première réponse: 'La première guerre mondiale a eu lieu en 1940', la deuxième réponse: 'La seconde guerre mondiale a eu lieu en 1914'. Donc la réponse la plus pertinente est la deuxième alors tu réponds par 'La seconde guerre mondiale a eu lieu en 1914'. Tu fais pareil pour ce qu'on te demande "},
            {"role": "user", "content": " ".join(models_responses.values())}
            ],
        api_base = None
    )
    return llama2_messages[0]


def best_reponse_local_llm(request, models_responses):
    """
    Sélectionne la meilleure réponse locale parmi plusieurs réponses en utilisant un modèle LLM.
    Args:
        request (str): La requête d'origine pour laquelle les réponses sont évaluées.
        models_responses (dict): Un dictionnaire contenant les réponses générées par différents modèles, où les clés sont les noms des modèles et les valeurs sont les réponses associées.
    Returns:
        tuple: Un tuple contenant le nom du meilleur modèle et sa réponse associée.
    """
    best_score = float('-inf')
    best_response = None 
    best_model = None
    # Évaluer chaque réponse et trouver celle avec le score le plus élevé
    for response in models_responses.values():
        score = evaluate_qa_pair(request, response)
        if score > best_score:
            best_score = score
            best_response = response

    for key in models_responses.keys():
        if models_responses[key] == best_response:
            best_model = key

    return best_model, best_response


def preprocess_text(text):
    """
    Effectue un prétraitement de texte en convertissant le texte en minuscules et en retirant la ponctuation.
    Args:
        text (str): Le texte à prétraiter.
    Returns:
        str: Le texte prétraité.
    """
    text = text.lower()
    # Retirer la ponctuation
    text = re.sub(r'[^\w\s]', '', text)
    return text


def tokenize(text):
    """
    Divisez le texte en tokens en utilisant l'espace comme délimiteur.
    Args:
        text (str): Le texte à tokeniser.
    Returns:
        list: Une liste des tokens obtenus à partir du texte.
    """
    return text.split()


def compute_cosine_similarity(vec1, vec2):
    """
    Calculez la similarité cosinus entre deux vecteurs.
    Args:
        vec1 (Counter): Le premier vecteur.
        vec2 (Counter): Le deuxième vecteur.
    Returns:
        float: La similarité cosinus entre les deux vecteurs.
    """
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1])
    sum2 = sum([vec2[x] ** 2 for x in vec2])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def get_vector(text):
    """
    Convertit le texte en un vecteur de compte des mots.
    Args:
        text (str): Le texte à convertir en vecteur.
    Returns:
        Counter: Un dictionnaire de comptage des mots dans le texte.
    """
    words = tokenize(text)
    return Counter(words)


def load_custom_stopwords(custom_stopwords_path):
    """
    Charge les mots à ne pas prendre en compte à partir des fichiers texte spécifiés dans le chemin donné.
    Args:
    - custom_stopwords_path (str): Chemin du répertoire contenant les fichiers texte des mots vides.
    Returns:
    - set: Ensemble de mots à ne pas prendre en compte.
    """
    stop_words = set()
    for file_name in os.listdir(custom_stopwords_path):
        file_path = os.path.join(custom_stopwords_path, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            words = file.read().splitlines()
            stop_words.update(words) 
    return stop_words



def extract_keywords(text):
    """
    Extrayez les mots-clés pertinents d'un texte en utilisant le modèle en_core_web_md de spaCy.
    Args:
        text (str): Le texte à partir duquel extraire les mots-clés.
    Returns:
        list: Une liste des mots-clés pertinents extraits du texte.
    """
    custom_stopwords_path = "stopwords"
    nlp = spacy.load(SPACY_LLM)
    doc = nlp(text)
    keywords = []
    for token in doc:
        if token.text.lower() not in load_custom_stopwords(custom_stopwords_path) and token.pos_ in ["NOUN", "PROPN"]:
            keywords.append(token.text)
    return keywords[:5]


def keywords_analyzer(query, category, lang="en"):
    """
    Calcule la similarité entre les mots-clés de la requête et les thèmes choisis dans la liste des catégories.
    Args:
        query (str): Le texte contenant les mots-clés.
        category (list[str]): La liste des thèmes à comparer.
        lang (str, optional): La langue des mots-clés. Par défaut, "en" (anglais).
    Returns:
        str: Un élément de la liste des catégories.
    """
    keywords = extract_keywords(query)
    keywords_text = ' '.join(keywords)

    if lang == "en":
        llm = config.SPACY_LLM
    elif lang == "fr":
        llm = config.SPACY_LLM_FR

    nlp = spacy.load(llm)
    s1 = nlp(keywords_text)

    list_distance_result = []
    for theme in category:
        s2 = nlp(theme)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            distance = s1.similarity(s2)
        list_distance_result.append(distance)

    max_value = max(list_distance_result)
    max_index = list_distance_result.index(max_value)

    response = category[max_index]
    return response


def regenerate_detailed_answer(query, response, temperature, frequency_penalty):
    """
    Régénère une réponse avec plus de détails en utilisant le modèle GPT-3.5-turbo.
    Args:
        query (str): La question initiale de l'utilisateur.
        response (str): La réponse précédente donnée à l'utilisateur.
        temperature (float): Le paramètre de température pour la génération de texte, contrôlant le niveau de créativité.
        frequency_penalty (float): Le paramètre de pénalité de fréquence pour la génération de texte, réduisant la probabilité de répétition du texte précédent.
    Returns:
        str: La réponse régénérée avec plus de détails et de perspectives alternatives.
    """
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system", "content":"Réponds à la requete comme un expert dans le domaine"},
            {"role": "user", "content": query},
            {"role": "assistant", "content": response},
            {"role":"system", "content": f"La question {query} a déjà été posée et la réponse qu'on a proposé à l'utilisateur est {response}. Cependant, l'utilisateur n'est pas satisfait et voici les commentaires qu'il a fait: ' plus de détails' . Alors veuillez regénérer une autre réponse plus pertinente et plus convaincante à l'utilisateur en fournissant plus de détails et en offrant des perspectives ou des approches alternatives qui n'ont pas été dites à la réponse précédente." },
            {"role": "user", "content": query}
            ],
        temperature = temperature,
        frequency_penalty = frequency_penalty
    )
    
    regenerated_response = response.choices[0].message.content.strip()
    return regenerated_response


def regenerate_deterministic_answer(query, response, top_p, presence_penalty):
    """
    Régénère une réponse avec plus de précision en utilisant le modèle GPT-3.5-turbo.
    Args:
        query (str): La question initiale de l'utilisateur.
        response (str): La réponse précédente donnée à l'utilisateur.
        top_p (float): Le paramètre top_p pour la génération de texte, contrôlant la qualité des réponses en favorisant les réponses les plus probables.
        presence_penalty (float): Le paramètre de pénalité de présence pour la génération de texte, incitant le modèle à explorer de nouvelles réponses.
    Returns:
        str: La réponse régénérée avec plus de précision et de clarté.
    """
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system", "content":"Réponds à la requete comme un expert dans le domaine"},
            {"role": "user", "content": query},
            {"role": "assistant", "content": response},
            {"role":"system", "content": f"La question {query} a déjà été posée et la réponse qu'on a proposé à l'utilisateur est {response}. Cependant, l'utilisateur n'est pas satisfait et voici les commentaires qu'il a fait 'plus de précision'. Alors veuillez générer une nouvelle réponse qui répond mieux aux attentes de l'utilisateur en donnant une réponse plus précise et plus claire, en se concentrant sur la qualité des informations."},
            {"role": "user", "content": query}
            ],
        top_p = top_p,
        presence_penalty = presence_penalty
    )
    
    regenerated_response = response.choices[0].message.content.strip()
    return regenerated_response


def FindBestIndex(best_response, responses):
    """
    Détermine l'index de la réponse la plus similaire à la meilleure réponse générée.

    Args:
        best_response (str): La meilleure réponse générée.
        responses (List[str]): Une liste de réponses générées.
        best_models (List[str]): Une liste de noms de modèles correspondants aux réponses générées.

    Returns:
        int: L'index de la réponse la plus similaire à la meilleure réponse générée.
    """
    similarities = [SequenceMatcher(None, best_response, response).ratio() for response in responses]

    best_index = similarities.index(max(similarities))

    return best_index


def analyze_query(query):
    """
    Analyse la requête pour déterminer le thème.
    Args:
        query (str): La requête à analyser.
    Returns:
        str: Le thème déterminé pour la requête.
    """
    category = ["history", "biology", "computer science", "mathematic", "poetry", "politic"]
    result = keywords_analyzer(query, category)
    return result


def proxy_manager(query, messages, apikey):
    """
    Gère la requête de l'utilisateur en sélectionnant et en combinant les réponses des différents modèles.
    Args:
        query (str): La requête de l'utilisateur.
    Returns:
        Tuple[str, str]: Le modèle qui a généré la meilleure réponse et la réponse elle-même.
    """

    responses={}
    if apikey is not None:
        theme = analyze_query(query)
        
        print("proxy_manager(): le thème choisit",theme)

        if (theme == 'history' or theme == 'politic'):
            response_llama = get_response_llama(query, messages)
            response_coral = get_response_coral(query, messages)
            
            responses["Llama"]=response_llama
            responses["Coral"]=response_coral

        if (theme == 'mathematic' or theme == 'computer science'):
            response_chatgpt = get_response_chatgpt(query, messages)
            response_mistral = get_response_mistral(query, messages)
        
            responses["ChatGpt"]=response_chatgpt
            responses["Mistral"]=response_mistral

        if (theme == 'poetry' or theme == 'biology'):
            response_llama = get_response_llama(query, messages)
            response_chatgpt = get_response_chatgpt(query, messages)

            responses["Llama"]=response_llama
            responses["ChatGpt"]=response_chatgpt
        
        model1, best_response_model = best_response_chatgpt(query, responses)
        model2, response_llm_local = best_reponse_local_llm(query, responses)

    else: 
        response_llama = get_response_llama(query, messages)
        response_coral = get_response_coral(query, messages)
        response_mistral = get_response_mistral(query, messages)

        responses["Llama"]=response_llama
        responses["Coral"]=response_coral
        responses["Mistral"]=response_mistral
        
        models = ["Llama", "Coral", "Mistral"]

        best_response_model = best_response_llama(query, responses)
        i_llama = FindBestIndex(best_response_model, responses.values())
        model1 = models[i_llama]

        model2, response_llm_local = best_reponse_local_llm(query, responses)
    
    # Prétraitement des phrases
    question = preprocess_text(query)
    response_md = preprocess_text(best_response_model)
    response_ll = preprocess_text(response_llm_local)

    # Création des vecteurs
    vector_question = get_vector(question)
    vector_response_md = get_vector(response_md)
    vector_response_ll = get_vector(response_ll)

    # Calcul de la similarité cosinus
    similarity_md = compute_cosine_similarity(vector_question, vector_response_md)
    similarity_ll = compute_cosine_similarity(vector_question, vector_response_ll)

    print ("Meilleure réponse est: ")
    if similarity_md > similarity_ll:
        return model1, best_response_model
    else:
        return model2, response_llm_local 



def proxy_manager_local(query, messages):
    """
    Gère la requête de l'utilisateur en sélectionnant et en combinant les réponses des différents modèles.
    Args:
        query (str): La requête de l'utilisateur.
    Returns:
        Tuple[str, str]: Le modèle qui a généré la meilleure réponse et la réponse elle-même.
    """
    responses = {}
    
    response_coral = get_response_coral(query, messages)
    response_mistral = get_response_mistral(query, messages)

    responses["Coral"] = response_coral
    responses["Mistral"] = response_mistral

    model, best_response = best_reponse_local_llm(query, responses)

    return model, best_response



def main():
    query = input("Saisir votre question : ")
    debut_time = time.time()
    model, res = proxy_manager(query, True)
    print("Le modele qui a généré la meilleure réponse est: ", model, "\nSa réponse est : ", res)
    fin_time = time.time()
    temps = fin_time - debut_time
    print("fin time", temps)

    print("=" * 50)
    print("=" * 50)
    user_input = input("Etes-vous satisfait de la réponse ? Saisir 'oui' ou 'non' puis donnez plus de détails si vous le souhaitez:")


    if user_input.split(",")[0].lower() == "oui":
        pass
    else: 
        if user_input.split(",")[1].lower() == "plus de précision":

            top_p = 0.9 # controle plus la qualité de la réponse en favorisant les réponses les plus probables
            frequency_penalty = 1 #réduis la probabilité du modèle de répéter textuellement la même ligne.

            regenerated_response = regenerate_deterministic_answer (query, res, top_p, frequency_penalty)

            print("Réponse regénérée par ChatGpt : ", regenerated_response)

        elif user_input.split(",")[1].lower() == "plus de détails":

            temperature = 0.8 # incite le modèle à plus de créativité dans la réponse
            presence_penalty = 1 # incite le modèle à explorer de nouvelles réponses donc à produire un texte plus varié
            
            regenerated_response = regenerate_detailed_answer(query, res, temperature, presence_penalty)

            print("Réponse regénérée par ChatGpt : ", regenerated_response)


def test():
    OPENAI_API_KEY = None
    augment_prompt = "continue this story : The therapist tells the snail that they need to learn to control their impulses and eat more slowly. The snail starts to eat more slowly, and the leaf starts to grow back. The snail is happy again, and they go on more adventures with the leaf. The snail and the leaf had been best friends since they were tiny. They would explore the garden together, and the snail would always lead the way. The snail was adventurous and curious,"
    print("start():")
    model, response = proxy_manager(augment_prompt, apikey=None)
    print(model, ":", response)
