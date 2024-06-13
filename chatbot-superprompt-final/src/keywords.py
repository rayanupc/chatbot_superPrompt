from rake_nltk import Rake
import spacy
import csv
import json
import prompts.prompts_data as data
import config

import themeanalyzer

SPACY_LLM_EN = config.SPACY_LLM
SPACY_LLM_FR = config.SPACY_LLM_FR


def compare_sentence(phrase1, phrase2, lang="fr"):
    """Pas utilisé"""
    # Retourne un résultat entre 0 et 1. Plus les phrases sont similaire dans leur sens plus le résultat est élevé
    # On parle de distance entre deux mot parce que les mots on des coordonnées
    if lang == "en":
        llm = SPACY_LLM_EN
    if lang == "fr":
        llm = SPACY_LLM_FR

    spacy.load(llm) # On peut omettre cette ligne de code avec cette ligne de commande ```python -c "import spacy; spacy.load('en_core_web_md')"```

    s1 = spacy.nlp(word1)
    s2 = spacy.nlp(word2)

    distance = s1.similarity(s2)

    return distance


def find_in_csv(num, lang="en"):
    """
    Recherche dans un fichier CSV contenant de nombreux prompts et extrait le prompt numéro 'num'.
    Args:
        num (int): Le numéro du prompt à extraire.
        lang (str, optional): La langue du fichier CSV. Par défaut, "en" (anglais).
    Returns:
        str: Le prompt extrait.
    """
    if num == None:
        return None
    i = 0
    with open(f'prompts/prompts_{lang}.csv', newline='', encoding='utf-8') as csvfile:
        reader_csv = csv.reader(csvfile)
        for ligne in reader_csv:
            if i == (num):
                break
            i += 1
    return ligne[1]


def find_predefined_prompt(text, lang="en"):
    """
    Recherche un prompt prédéfini en fonction du texte donné en utilisant un modèle de langage local.
    Args:
        text (str): Le texte à analyser pour trouver le prompt prédéfini.
        lang (str, optional): La langue du prompt. Par défaut, "en" (anglais).
    Returns:
        str: Le prompt prédéfini correspondant au texte donné.
    """
    category = data.list_prompts_title
    title = themeanalyzer.llm_analyzer(text, category, lang)
    print(title)
    try:
        index = data.dict_prompts_title[title]
        super_prompt = find_in_csv(index, lang)
    except Exception as e:
        super_prompt = "Unable to find matches"
    
    return super_prompt


def keyword_title_prompt(query, lang="en"):
    super_prompt = find_predefined_prompt(query, lang)
    result = f"With this instructions : {super_prompt} \nAnswers to this query : {query}"
    return result


def main():
    prompt = "history"
    prompt = "main event world war II"
    prompt = "Tell me about a significant event from World War II that often gets overlooked in history books."
    prompt = "Many history books focus on well-known events of World War II, such as D-Day or the Battle of Stalingrad, but there are countless lesser-known yet significant events that shaped the course of the war. From daring covert operations to lesser-known battles, there's a wealth of stories waiting to be discovered. Share with me one such event that often gets overlooked in mainstream narratives of World War II."
    prompt = "Tell me about a significant event from World War II that often gets overlooked in history books."
    prompt = "Write a short story about a weary traveler who stumbles upon a hidden village inhabited by mystical creatures straight out of a fairy tale."

    result = keyword_title_prompt(prompt)
    print(result)