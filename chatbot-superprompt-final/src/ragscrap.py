import re
import requests
import bs4
from langchain_community.document_loaders import WebBaseLoader
from googlesearch import search
import os
import config


NB_SCRAP_RESEARCH = config.NB_SCRAP_RESEARCH
DATA_PATH = "data"
FILE_EXTENTION = ".md"


def scrapping(url):
	"""
	Effectue le scrapping d'une page web spécifiée.
	Args:
		url (str): L'URL de la page web à scraper.
	Returns:
		tuple(str, str, str): Le contenu de la page web scrapée, son titre, et son url.
	"""
	html_doc = requests.get(url)
	soup = bs4.BeautifulSoup(html_doc.content, 'html.parser')
	title = soup.title.text
	content = soup.get_text()
	print(url)
	
	return content.strip(), title, url


def scrapping2(url):
	"""
	Effectue le scrapping d'une page web spécifiée par l'URL et renvoie le contenu de la page.
	Args:
		url (str): L'URL de la page web à scraper.
	Returns:
		str: Le contenu de la page web.
	"""
	# Only keep post title, headers, and content from the full HTML.
	bs4_strainer = bs4.SoupStrainer()
	loader = WebBaseLoader(
	    web_paths=(url,),
	    bs_kwargs={"parse_only": bs4_strainer},
	)
	docs = loader.load()

	return docs[0].page_content


def create_filename(text):
	"""
	Convertit un texte en un titre de fichier valide pour les systèmes d'exploitation Windows et Linux.
	Args:
		text (str): Le texte à convertir en titre de fichier.
	Returns:
		str: Le titre de fichier valide pour Windows et Linux.
	"""
	filename = text
	filename = filename.replace(".", "").replace("[", "").replace("]", "")

	# Remplace les caractères non valides par des espaces
	invalid_chars = re.compile(r'[-°<>:,`\'"/\\|?*~$!()éùèà&’–’]') # Windows <>:"/\|?* Linux /~$!*?()|<>
	filename = invalid_chars.sub(" ", filename)

	filename = re.sub(r" +", "-", filename) # Remplace les espaces consécutifs par un seul trait
	filename = filename[:255] # Tronque le nom à 255 caractères
	filename = filename.lower()

	return filename


def save_file(content, title="untitled"):
	"""
	Sauvegarde le contenu dans un fichier avec un titre spécifié. Si aucun titre n'est fourni, utilise "untitled" par défaut.
	Args:
		content (str): Le contenu à enregistrer dans le fichier.
		title (str, optional): Le titre du fichier. Par défaut, "untitled".
	Returns:
		True: True si la sauvegarde du fichier a réussi.
	"""
	writer_path = os.path.join(DATA_PATH, title+FILE_EXTENTION)
	
	# On vérifie si le nom du fichier n'existe pas déjà
	while os.path.isfile(writer_path):
		print(writer_path, os.path.isfile(writer_path))
		writer_path = writer_path.replace(FILE_EXTENTION, "")
		if writer_path[-1] in "01234567890":
			print(int(writer_path[-1]) + 1)
			print(writer_path[:-1])
			writer_path = writer_path[:-1] + str(int(writer_path[-1]) + 1)
			print(writer_path)
		else :
			writer_path += "1"
		writer_path += FILE_EXTENTION

	with open(writer_path, 'w', encoding='utf-8') as mdfile:
		mdfile.write(content.strip())
	return True


def google_search(query):
	"""
	Effectue une recherche sur Google en utilisant la requête spécifiée.
	Args:
		query (str): La requête de recherche à effectuer sur Google.
	Returns:
		list(str) : Retourne la liste de tous les urls trouvés par Google.
	"""
	return list(search(query, tld="co.in", num=NB_SCRAP_RESEARCH, stop=NB_SCRAP_RESEARCH, pause=2))


def wikipedia_search(query, lang="en"):
	"""
	Effectue une recherche sur Wikipedia dans la langue spécifiée en utilisant la requête spécifiée.
	Args:
		query (str): La requête de recherche à effectuer sur Wikipedia.
		lang (str, optional): La langue de la recherche. Par défaut, "en" (anglais).
	Returns:
		list(str) : Retourne la liste de tous les urls trouvés sur Wikipedia.
	"""
	number_of_results = NB_SCRAP_RESEARCH
	try:
		# Requête Wikipedia
		url = f'https://api.wikimedia.org/core/v1/wikipedia/{lang}/search/page'
		parameters = {'q': query, 'limit': number_of_results}
		response = requests.get(url, params=parameters)
		data = response.json()

		list_result = []
		for elem in data['pages']:
			url = f"https://{lang}.wikipedia.org/wiki/{elem['key']}"
			list_result.append(url)

	except Exception as e:
		list_result = []

	return list_result