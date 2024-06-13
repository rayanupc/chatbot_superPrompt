#!/bin/bash

# Installer les dépendances à partir du fichier requirements.txt
python3.11 -m pip install -r requirements.txt

# Lancer l'application
open src/website/index.html

# Lancer le serveur
python3.11 src/app.py 