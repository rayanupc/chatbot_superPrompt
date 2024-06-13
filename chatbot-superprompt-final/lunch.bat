@echo off

rem Installer les dépendances à partir du fichier requirements.txt
pip install -r requirements.txt

rem Lancer l'application
start "" src\website\index.html

rem Lancer le serveur
python src\app.py