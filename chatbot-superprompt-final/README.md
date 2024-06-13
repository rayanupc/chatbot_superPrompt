# Projet Chatbot Super prompt (L3AF1)

## Description du Projet

L'utilisation des grands modèles de langage tels que ChatGPT ou Mistral comporte plusieurs subtilités. Il est nécessaire d'apporter un maximum de précision dans sa demande afin que le modèle de langage comprenne bien l'essence de la requête de l'utilisateur et puisse lui renvoyer la réponse la plus précise possible. De plus, les connaissances des différents modèles de langage sont souvent entraînées sur des données limitées dans le temps.

L'objectif de ce projet est de développer une application permettant de compléter le prompt d'un utilisateur en fonction d'un contexte prédéterminé ou d'une tâche à réaliser. Cette application aura pour but de sélectionner et d'enrichir les meilleurs modèles de langage en fonction de la requête utilisateur pour renvoyer la meilleure réponse possible.

## Contraintes du projet

1. **Coût des clés API :**
- Certaines clés API, nécessaires pour utiliser des modèles de langage, sont payantes et/ou ont des utilisations limitées ce qui limite forcément notre efficacité lors des phases de tests.

2. **Dépendances externes :**
- Il est impossible de prévoir ce que va renvoyer les LLM ce qui crée une certaine incertitude lors du développement.

3. **Hallucination des Modèles de langage :**
- Les Modèles de langage peuvent être amenés à halluciner et à donner des réponses incohérentes.

## Objectifs du Projet

1. **Enrichissement de prompt basé sur le contexte :**
   - Développement d'une application permettant de compléter les prompts des utilisateurs en fonction d'un contexte prédéterminé ou d'une tâche à réaliser, afin d'améliorer la précision des réponses fournies par les différents modèles de langage.

2. **Fourniture de connaissances aux modèles :**
   - Ajout de connaissances spécifiques aux différents modèles de langage utilisés, afin d'améliorer leur capacité à fournir des réponses pertinentes dans un domaine particulier ou pour une tâche spécifique.

3. **Optimisation de la qualité des réponses :**
   - Mise en place d'algorithmes visant à améliorer la qualité des réponses fournies par les modèles de langage en tenant compte du contexte et des besoins spécifiques de l'utilisateur.

4. **Interface utilisateur conviviale :**
   - Création d'une interface utilisateur conviviale permettant aux utilisateurs d'interagir facilement avec l'application et de saisir leurs requêtes de manière précise.

## Organisation du Projet

- `..\app.py` <br> : Contient le code source du projet lié à la gestion du serveur nécessaire au bon fonctionnement de l'application.
- `..\proxy.py` <br> : Contient le code source du projet lié à la gestion du proxy qui décide du meilleur modèle de langage pour répondre à la requête.
- `..\ragscrap.py` et `..\videotorag.py` <br> : Contient le code source lié aux différentes fonctions du RAG à savoir, l'enrichissement via les recherches sur Internet, l'ajout de document PDF et des vidéos au format mp4.
- `..\tests` <br> : Contient le code source du projet lié au test unitaire veillant au bon fonctionnement du programme.
- `..\website\*` <br> : Contient le code source du projet lié à l'application web.

## Prérequis

- Système d'exploitation Windows ou MacOs.
- Python 3.11 minimum.
- Une connexion internet fiable.
- Une clé API ChatGPT pour profiter pleinement des fonctionnalités de l'application.

## Installation

1. Ouvrez le terminal.
2. Si vous êtes sur MacOS, placez-vous dans le répertoire du fichier lunch.sh. Si vous êtes sur windows placez vous dans le répertoire du fichier lunch.bat.
3. Lancez le fichier serveur.sh avec la commande suivante : <br>
`sh launch.sh` ou `launch.bat`.

## Fonctionnalités Implémentées
### Obligatoires
1. Enrichissement du prompt.
2. Visualisation de l’enrichissement du prompt de l’utilisateur.
3. Proxy intelligent qui questionne le LLM le plus apte à répondre.
4. Accès à une réponse IA d’un serveur local par le proxy (génération de réponses moins performantes mais avec une protection des données).
5. Accès à une réponse IA payante avec une clé API (génération plus performante de réponses, mais des données non protégées).
6. Création d'une interface utilisateur.

### Secondaires
1. Enrichissement des connaissances du LLM par des informations externes (page web, vidéo, pdf) grâce au RAG.
2. Proxy intelligent qui choisit une réponse d’un modèle de langage le plus adapté pour un prompt donné, en fonction de ses capacités et de ses domaines de connaissances.
3. Possibilité de réévaluation du prompt enrichi si l’utilisateur n’est pas satisfait (si l'utilisateur possède une clé API ChatGPT).

## Ce que le projet nous a apporté
Ce projet nous a offert une expérience enrichissante à plusieurs niveaux.


#### Compétences techniques 
Tout d'abord, nous avons pu développer nos compétences techniques en travaillant sur des aspects pratiques de la programmation et de la résolution de problèmes.

#### Compétences comportementales

Ensuite, la collaboration avec nos collègues nous a permis d'améliorer nos capacités de communication et de travail d'équipe, essentielles dans un environnement professionnel. De plus, la gestion du projet nous a donné l'occasion d'acquérir des compétences en planification, en organisation et en prise de décision, ce qui s'avérera essentiel dans nos projets futurs.


#### Rayan ALMOHAIZE
#### Alicia TCHEMO
#### Melisa MERABET 
#### Djibril DAHOUB