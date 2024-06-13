from transformers import pipeline
import spacy
import warnings
from rake_nltk import Rake
import config

MODEL_LLM_LOCAL = config.MODEL_LLM_LOCAL_XL

SPACY_LLM_EN = config.SPACY_LLM
SPACY_LLM_FR = config.SPACY_LLM_FR

def extract_keywords(text):
    """
    Extrait jusqu'à 5 mots-clés du texte avec leur score. Les mots-clés sont identifiés grâce à une analyse grammaticale.
    Args:
        text (str): Le texte depuis lequel on extrait les mots-clés.
    Returns:
        list(tuple(float 0->1, str)): Une liste de tuples contenant le score et le mot-clé correspondant.
    """
    r = Rake()
    r.extract_keywords_from_text(text)
    scores_list = r.get_ranked_phrases_with_scores()
    #print(scores_list)
    print("extract_keywords():", end=" ")
    
    list_keywords = []
    for rating, keyword in scores_list:
        if rating > 1:
            list_keywords.append((rating, keyword))
            print(rating, keyword, end=" ")
    n = len(list_keywords) if len(list_keywords) < 5 else 5
    
    return list_keywords[:n]



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
    # Concaténation des mots-clés
    list_keywords = [elem[1] for elem in keywords]
    keywords_text = ' '.join(list_keywords)

    if lang == "en":
        llm = SPACY_LLM_EN
    if lang == "fr":
        llm = SPACY_LLM_FR

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


def llm_analyzer(query, category, lang="en"):
    """
    Demande à un modèle de langage local de catégoriser la requête dans l'une des catégories spécifiées.
    Args:
        query (str): Le texte à catégoriser.
        category (list[str]): La liste des catégories possibles.
        lang (str, optional): La langue de la requête. Par défaut, "en" (anglais).
    Returns:
        str: Un élément de la liste des catégories.
    """
    category_text = ", ".join(category)
    # keywords = extract_keywords(query)
    request = f"In which category does this query relate most: {category_text}? If you can not categorize the following query, respond with 'None'. Respond with only the word representing the category. Here is the query : {query}"
    text2text_generator = pipeline("text2text-generation", model=MODEL_LLM_LOCAL)
    response = text2text_generator(
        request,
        max_length=20,
    )
    response = response[0]["generated_text"]
    return response


def main():
    category = ["history", "science", "farytail"]
    query = "Tell me about a significant event from World War II that often gets overlooked in books."
    result = llm_analyzer(query, category)
    print("llm_analyzer(query, category):", result)
    result = keywords_analyzer(query, category)
    print("keywords_analyzer(query, category):", result)