import fitz
import os
import config

import ragscrap
import createvdb


DATA_PATH = "data"
PDF_FILE_PATH = os.path.join(DATA_PATH, "files") 


def pdf_to_text(file_name):
	"""
	Convertit le contenu d'un fichier PDF en texte brut.
	Args:
	    file_name (str): Le nom du fichier PDF à convertir.
	Returns:
	    str: Le texte extrait du fichier PDF.
	"""
	document = fitz.open(file_name)
	text = ""
	for page in document:
		text += page.get_text()
	return text.strip()


def extract_info():
	"""
	Extrait des informations à partir de fichiers PDF en les convertissant en texte brut et en les enregistrant dans des fichiers Markdown.
	Returns:
	    bool: True si l'extraction des informations a réussi, sinon False.
	"""
	folder = PDF_FILE_PATH

	for pdffile in os.listdir(PDF_FILE_PATH):
		file_path = os.path.join(PDF_FILE_PATH, pdffile)
		if os.path.isfile(file_path) and file_path.endswith(".pdf"):
			print("extract_info(): "+file_path)
			content = pdf_to_text(file_path)
			file_name = pdffile.replace(".pdf", "")
			file_name = ragscrap.create_filename(file_name)
			
			writer_path = os.path.join(DATA_PATH, file_name+".md")
			with open(writer_path, 'w', encoding='utf-8') as mdfile:
				mdfile.write(content)

			createvdb.add_to_vectorstores(file_name)
			os.remove(file_path)

	return True