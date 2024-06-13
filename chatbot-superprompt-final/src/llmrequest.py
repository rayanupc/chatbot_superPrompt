import openai
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import config

MODEL_LLM_LOCAL = config.MODEL_LLM_LOCAL_XL


def request_llm_local(prompt, role):
    """
    Fonction pour améliorer le prompt en utilisant un modèle de génération de texte.
    Prend en entrée le prompt fourni par l'utilisateur et le rôle de l'IA, et renvoie une réponse améliorée générée par le modèle.
    Args:
        prompt (str): Le prompt fourni par l'utilisateur.
        role (str): Les instructions pour le rôle de l'IA.
    Returns:
        str: La réponse améliorée générée par le modèle.
    """
    # Spécification du modèle à utiliser
    model_name = MODEL_LLM_LOCAL

    # Chargement du tokenizer et du modèle
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name) 
     
    #Création d'un pipeline pour la génération de texte
    pipe = pipeline("text2text-generation", model=model_name)

    # Encodage du rôle de l'IA et du prompt utilisateur
    role_token = tokenizer.encode(role, return_tensors="pt")
    prompt_tokens = tokenizer.encode(prompt, return_tensors="pt")
   
    # Concaténation des tokens du rôle et du prompt
    input_ids = torch.cat((role_token, prompt_tokens), dim=1)
    output = model.generate(input_ids, num_return_sequences=1, no_repeat_ngram_size=2)
    
    # Décodage de la réponse générée
    improved_prompt = tokenizer.decode(output[0], skip_special_tokens=True)
   
    return improved_prompt.strip()


def request_chatgpt(prompt, role):
    """
    Fonction pour améliorer le prompt en utilisant l'API OpenAI ChatGPT.
    Prend en entrée le prompt fourni par l'utilisateur et renvoie une réponse améliorée.
    Args:
        prompt (str): Le prompt fourni par l'utilisateur.
        role (str): Les instructions pour le rôle de l'IA.
    Returns:
        str: La réponse améliorée générée par ChatGPT.
    """

    # Appel à l'API ChatGPT pour améliorer le prompt
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": role},
            {"role": "user", "content": prompt}
        ]
    ) 
    # Renvoi du contenu de la réponse améliorée
    return response.choices[0].message.content.strip()