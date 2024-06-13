from langchain_community.document_loaders import DirectoryLoader, TextLoader, UnstructuredMarkdownLoader
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langdetect import detect

import os
import shutil

from ragscrap import *
import themeanalyzer
import config


DATABASE_PATH = "vectorstores"
DATA_PATH = "data"


def create_vectorstores():
    """
    Crée une nouvelle base de données. Des vecteurs de représentation sont associés pour les documents texte en utilisant un modèle de langage.
    Returns:
        str: Le chemin de la base de données où sont stockés les vecteurs.
    """
    documents = load_all_documents()
    chunks = split_text(documents)
    vectorstores = save_to_vectorstores(chunks)
    return DATABASE_PATH


def save_to_vectorstores(chunks: list[Document]):
    """
    Enregistre les fragments de documents dans des vectorstores en utilisant des représentations vectorielles.
    Args:
        chunks (list[Document]): Une liste de fragments de documents.
    Returns:
        Chroma: La vectorstores contenant les représentations vectorielles des fragments de documents.
    """
    # Clear out the database first.
    if os.path.exists(DATABASE_PATH):
        shutil.rmtree(DATABASE_PATH)

    # Create a new DB from the documents.
    embedding_function = OpenAIEmbeddings()
    vectorstores = Chroma.from_documents(chunks, embedding_function, persist_directory=DATABASE_PATH)
    vectorstores.persist()
    print(f"save_to_vectorstores(): Saved {len(chunks)} chunks to {DATABASE_PATH}.")
    return vectorstores


def load_all_documents():
    """
    Charge tous les documents texte à partir d'un répertoire spécifié.
    Returns:
        list[Document]: Une liste de documents texte.
    """
    text_loader_kwargs={'autodetect_encoding': True}
    loader = DirectoryLoader(DATA_PATH, glob="*.md", show_progress=True, loader_cls=TextLoader, loader_kwargs=text_loader_kwargs)
    documents = loader.load()
    return documents


def split_text(documents: list[Document], chunk_size=700, chunk_overlap=200):
    """
    Divise les documents en fragments de texte avec une taille de fragment spécifiée et un chevauchement de fragments.
    Args:
        documents (list[Document]): Une liste de documents à diviser.
        chunk_size (int, optional): La taille de chaque fragment de texte. Par défaut, 700.
        chunk_overlap (int, optional): Le chevauchement entre les fragments de texte. Par défaut, 200.
    Returns:
        list[Document]: Une liste de fragments de texte.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"split_documents(): Split {len(documents)} documents into {len(chunks)} chunks.")

    # if len(chunks) != 0:
    #     document = chunks[0]
    #     print(document)
    #     print(document.page_content)
    #     print(document.metadata)
    return chunks


def query_search(query_text, scrap=False):
    """
    Effectue une recherche dans la base de données de vecteurs en utilisant le texte de requête spécifié.
    Args:
        query_text (str): Le texte de la requête.
        scrap (bool, optional): Indique si une recherche web doit être effectuée en cas d'absence de résultats satisfaisants dans la base de données. Par défaut, False.
    Returns:
        str: Tous les textes associés à la requête.
    """
    # Prepare the DB
    print("RAG.query_search(): ")
    context_text = "Unable to find matching results."
    embedding_function = OpenAIEmbeddings()
    vectorstores = Chroma(persist_directory=DATABASE_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = vectorstores.similarity_search_with_relevance_scores(query_text, k=3)
    
    if len(results) == 0 or results[0][1] < 0.7 and scrap == False:
        # S'il est impossible de trouver une résultat satisfaisant on lance une seule requête scrap
        print(f"query_search(): Unable to find matching results.")
        query_to_url_to_db(query_text)
        query_search(query_text, scrap=True)
    elif not(len(results) == 0 or results[0][1] < 0.7):
        context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
        print(context_text)
        print([doc.metadata for doc, _score in results])
    else:
        # Si aucun résultat satifaisant n'a été trouver mais qu'une recherche scrap a été déjà faite
        context_text = "Unable to find matching results."
    
    return context_text


def add_to_vectorstores(file_name, chunk_size=700, chunk_overlap=200):
    """
    Ajoute le contenu d'un fichier à la base de données de vecteurs en le divisant en fragments de texte.
    Args:
        file_name (str): Le nom du fichier à ajouter à la base de données.
        chunk_size (int, optional): La taille de chaque fragment de texte. Par défaut, 700.
        chunk_overlap (int, optional): Le chevauchement entre les fragments de texte. Par défaut, 200.
    """
    print(f"add_to_vectorstores(): Waiting '{file_name}' to be added...")
    text_loader_kwargs={'autodetect_encoding': True}
    loader = DirectoryLoader(DATA_PATH, glob=file_name+".md", show_progress=True, loader_cls=TextLoader, loader_kwargs=text_loader_kwargs)
    documents = loader.load()

    chunks = split_text(documents, chunk_size, chunk_overlap)

    embedding_function = OpenAIEmbeddings()
    vectorstores = Chroma(persist_directory=DATABASE_PATH, embedding_function=embedding_function)
    vectorstores.add_documents(chunks)

    print(f"Added {len(chunks)} new chunks to {DATABASE_PATH}.")


def query_to_url_to_db(prompt):
    """
    Effectue une recherche sur Internet en utilisant le prompt spécifié, puis sauvegarde le contenu des URL trouvées dans la base de données de vecteurs.
    Args:
        prompt (str): Le texte du prompt utilisé pour la recherche Internet.
    Returns:
        None / str : Retourne None si rien n'a été fait et retourne le mot-clé passé en recherche internet sinon.
    """
    list_keywords = themeanalyzer.extract_keywords(prompt)

    if len(list_keywords) != 0:
        # keywords = ', '.join([elem[1] for elem in list_keywords])
        keyword = list_keywords[0][1] # Une seul mot-clé sélectionné
        lang = detect(prompt)

        print("keywords_search: ", keyword)
        # On crée une recherche google avec les mots-clés du prompt
        urls = google_search(keyword)
        urls += wikipedia_search(keyword, lang=lang)
        urls = list(set(urls))
        print("urls_search(): ", urls)
        
        for url in urls:
            content, title, url = scrapping(url)
            file_name = create_filename(title)
            file_name = file_name.replace(FILE_EXTENTION, "")
            save_file(content, file_name)
            add_to_vectorstores(file_name)

        return keyword 

    return None


def main():
    query_text = "How こと can be used in any level ?"
    result = query_search(query_text)