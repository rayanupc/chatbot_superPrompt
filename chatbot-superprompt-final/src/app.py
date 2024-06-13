from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import json
import os
import time

import openai
import litellm
import proxy
import llmrequest
import keywords
import pdftorag
import videotorag
import createvdb
import internetrag


DATA_PATH = "data"
PDF_FILE_PATH = os.path.join(DATA_PATH, "files") 
OPENAI_API_KEY = ""


app = Flask(__name__)
CORS(app)


class ApiError(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


# Gestion des erreurs personnalisées
@app.errorhandler(ApiError)

def error_handler(error):
    response = jsonify({'error': error.message})
    response.status_code = error.code
    return response


@app.route("/regenerate", methods=["POST"]) 

def reload_change_chatbot():
    data = request.form
    regenerate_option = data.get('regenerate_option')
    prompt = data.get('prompt')
    response = data.get('response')
    apikey = data.get('apikey')

    if apikey == "" :
        apikey = None
    else :
        os.environ['OPENAI_API_KEY'] = apikey.strip()

    regenerated_response = ""
    if regenerate_option == "temperature" :
        temperature = 0.8 # incite le modèle à plus de créativité dans la réponse
        presence_penalty = 1 # incite le modèle à explorer de nouvelles réponses donc à produire un texte plus varié
        regenerated_response = proxy.regenerate_detailed_answer(prompt, response, temperature, presence_penalty)

    elif regenerate_option == "top-p" :
        top_p = 0.9 # controle plus la qualité de la réponse en favorisant les réponses les plus probables
        frequency_penalty = 1 #réduis la probabilité du modèle de répéter textuellement la même ligne.
        regenerated_response = proxy.regenerate_deterministic_answer (prompt, response, top_p, frequency_penalty)

    print("regenerated_response:", regenerated_response)
    return jsonify({"response": regenerated_response, "model":"chatgpt/gpt-3.5-turbo"})


@app.route("/title", methods=["POST"]) 

def title_text():
    data = request.form
    text = data.get('text')
    title_generator_role = "Title Generator" # "Generate one super short title for this prompt."
    title = llmrequest.request_llm_local(text, role=title_generator_role)
    return jsonify({"response": title})


@app.route("/chatbot", methods=["POST"]) 

def chatbot_request():
    t = time.time()
    data = request.form
    prompt = data.get('prompt')
    messages = json.loads(data.get('messages'))
    enrichment_type = data.get('enrichment_type')
    llm_type = data.get('llm_type')
    rag_type = data.get('rag_type')
    apikey = data.get('apikey')
    files = request.files.getlist('files')
    secure_mode = data.get('secure_mode')

    if apikey == "" :
        apikey = None
    else :
        os.environ['OPENAI_API_KEY'] = apikey.strip()

    T2 = (time.time() - t) / 60
    t = time.time()
    print("chatbot_request(): Request parameters done", T2)

    # Différentes fonctionnalités

    # Fonctionnalité de upload de fichier
    try:
        if len(files) != 0:
            print("files: ", files)
            for file in files:
                file_path = os.path.join(PDF_FILE_PATH, file.filename)
                file.save(file_path)
            print(f"files: Files uploaded", end=" ")
            pdftorag.extract_info()
            videotorag.extract_info()
        else:
            print("files: No files uploaded", end=" ")
    except Exception as e:
        raise ApiError("Oops! Your file has not been uploaded. Please try again.", 500)
    T3 = (time.time() - t) / 60
    print(T3)
    t = time.time()
    
    try:
        # Fonctionnalité du mode Sécurisé
        if secure_mode == "true":
            enrichment_type = "llm-local"
            rag_type = "none"
            llm_type = "local_proxy"


        # Fonctionnalité de l'enrichissment du prompt
        
        enriched_prompt = prompt
        context = ""
        if enrichment_type == "none":
            enriched_prompt = prompt

        elif enrichment_type == "llm-local":
            user_prompt_role = "Tu es un expert en prompt engineering et en intelligence artificielle. Je veux que tu sois mon créateur de prompt attiré. Ton objectif est de me rédiger le meilleur prompt possible selon mes objectifs. Ton prompt doit etre rédigé et optimisé pour une requete à chatGPT-3.5. Pour cela tu vas d'abord me fournir le meilleur prompt possible selon ma demande, ensuite tu rédiges un paragraphe concis présentant les améliorations à apporter pour que le prompt soit un prompt 5 étoiles. Enfin tu dresses la liste des questions rééllement indisponsables pour améliorer ton prompt."
            indications = llmrequest.request_llm_local(prompt, user_prompt_role)
            llm_prompt_role = "Tu es un expert en prompt engineering et en intelligence artificielle. Je veux que tu sois mon créateur de prompt attiré. Ton objectif est de me rédiger le meilleur prompt possible selon mes objectifs. Ton prompt doit etre rédigé et optimisé pour une requete à chatGPT-3.5. Pour cela tu vas me fournir le meilleur prompt possible selon ma demande. Voici un exemple: ma question est : 'première guerre mondiale ?' et le prompt enrichi est :'je suis intéressé par des détails historiques sur la Première Guerre mondiale. Pouvez-vous me fournir un aperçu complet des causes, des événements clés, des conséquences et de l'impact global de ce conflit majeur qui a eu lieu entre 1914 et 1918 ? Merci de décrire les alliances, les batailles importantes, les innovations technologiques, les acteurs clés et tout autre détail pertinent pour mieux comprendre cette période historique cruciale.'"
            enriched_prompt = llmrequest.request_llm_local(prompt, llm_prompt_role)
            context = f"Indications pour créer un prompt plus détaillé : {indications}\n Prompt enrichi :{enriched_prompt}" # Donnée à return
        
        elif enrichment_type == "llm-chatgpt":
            user_prompt_role = "Tu es un expert en prompt engineering et en intelligence artificielle. Je veux que tu sois mon créateur de prompt attiré. Ton objectif est de me rédiger le meilleur prompt possible selon mes objectifs. Ton prompt doit etre rédigé et optimisé pour une requete à chatGPT-3.5. Pour cela tu vas d'abord me fournir le meilleur prompt possible selon ma demande, ensuite tu rédiges un paragraphe concis présentant les améliorations à apporter pour que le prompt soit un prompt 5 étoiles. Enfin tu dresses la liste des questions rééllement indisponsables pour améliorer ton prompt."
            indications = llmrequest.request_chatgpt(prompt, user_prompt_role)
            llm_prompt_role = "Tu es un expert en prompt engineering et en intelligence artificielle. Je veux que tu sois mon créateur de prompt attiré. Ton objectif est de me rédiger le meilleur prompt possible selon mes objectifs. Ton prompt doit etre rédigé et optimisé pour une requete à chatGPT-3.5. Pour cela tu vas me fournir le meilleur prompt possible selon ma demande. Voici un exemple: ma question est : 'première guerre mondiale ?' et le prompt enrichi est :'je suis intéressé par des détails historiques sur la Première Guerre mondiale. Pouvez-vous me fournir un aperçu complet des causes, des événements clés, des conséquences et de l'impact global de ce conflit majeur qui a eu lieu entre 1914 et 1918 ? Merci de décrire les alliances, les batailles importantes, les innovations technologiques, les acteurs clés et tout autre détail pertinent pour mieux comprendre cette période historique cruciale.'"
            enriched_prompt = llmrequest.request_chatgpt(prompt, llm_prompt_role)
            context = f"Indications pour créer un prompt plus détaillé : {indications}\nPrompt enrichi :{enriched_prompt}" # Donnée à return
            
        elif enrichment_type == "keywords":
            enriched_prompt = keywords.keyword_title_prompt(prompt)
            context = enriched_prompt # Donnée à return
        print("enrichment_type: Enrichment type done")


        # Fonctionnalité d'enrichissment des connaissance
        augment_prompt = ""

        if rag_type == "pdf":
            content = createvdb.query_search(prompt)
            augment_prompt = f"Add the following context to your knowledge for answering the query. If the context is not relevant feel free to use your knowledge: \n\n{content}\n\n---\nAnswer this query: {enriched_prompt}"
            context = augment_prompt
            
        elif rag_type == "internet":
            augment_prompt = internetrag.rag_manager(prompt)
            context += augment_prompt

        T4 = (time.time() - t) / 60
        print("RAG_type: RAG type done", T4)
        t = time.time()

        super_prompt = enriched_prompt +"\n"+ augment_prompt

        # Fonctionnalité d'envoie de requête au different llm
        response = ""
        model = ""

        if llm_type == "proxy" or llm_type == "none":
            model, response = proxy.proxy_manager(super_prompt, messages, OPENAI_API_KEY)

        elif llm_type == "local_proxy":
            model, response = proxy.proxy_manager_local(super_prompt, messages)
            
        elif llm_type == "mistral":
            model = "mistral"
            response = proxy.get_response_mistral(super_prompt, messages)

        elif llm_type == "chatgpt":
            model = "chatgpt"
            response = proxy.get_response_chatgpt(super_prompt, messages)

        elif llm_type == "llama":
            model = "llama"
            response = proxy.get_response_llama(super_prompt, messages)

        elif llm_type == "coral":
            model = "coral"
            response = proxy.get_response_coral(super_prompt, messages)

        T5 = (time.time() - t) / 60
        print("T5", T5)

    except litellm.exceptions.APIError as e:
        raise ApiError("Oops! You have reached your rate limit with Mistral. Please try again with an other LLM.", 400)
    except openai.OpenAIError as e:
        print(e)
        raise ApiError("Oops! There is a problem with your chatgpt API key. Please try again.", 400)
    except Exception as e:
        print(e)
        raise ApiError("Oops! Something went wrong while retrieving the response. Please try again.", 400)
    
    print({"response": response, "context":context, "model":model})
    
    return jsonify({"response": response, "context":context, "model":model})


if __name__ == "__main__":
    app.run(debug=True)