Intelligence artificielle
Agents intelligents
Elise Bonzon
elise.bonzon@u-paris.fr
LIPADE - Universit´
e Paris Cit´
e
http://www.math-info.univ-paris5.fr/∽bonzon/
1
Agents intelligents
1. Agents et environnement
2. Rationalit´
e
3. PEAS
4. Types d’environnement
5. Structure des agents
6. Conclusion
2
Agents et environnement
Agents et environnement
Les agents peuvent ˆ
etre des humains, des robots, des logiciels, des
thermostats...
?
agent
percepts
sensors
actions
environment
actuators
S. Russell and P. Norvig. Artificial Intelligence : A Modern Approach. 2002.
3
Le monde de l’aspirateur
A
B
• Percepts : emplacement et ´
etat de propret´
e e.g., [A, Sale]
• Actions : Gauche, Droite, Aspire, Rien
4
Le monde de l’aspirateur
Percepts
Action
[A, Propre]
Droite
[A, Sale]
Aspire
[B, Propre]
Gauche
[B, Sale]
Aspire
Agent aspirateur
1
function
Reflex -Vacuum -Agent(loc ,status) returns
an action
2
if status = Dirty
then
return
Suck
3
else if loc = A then
return
Right
4
else if loc = B then
return
Left
5
Rationalit´
e
Rationalit´
e
• Une mesure de performance ´
evalue l’environnement
• Un point par emplacement nettoy´
e dans le temps t ?
• Un point par emplacement propre `
a chaque pas de temps, moins 1
point par action effectu´
ee ?
• Un agent rationnel choisit l’action qui maximise la valeur attendue
de la mesure de performance en fonction de la s´
equence de percepts
obtenue jusque l`
a
• Rationnel ̸= omniscient
→les percepts ne permettent peut-ˆ
etre pas d’obtenir toutes les
informations utiles
• Rationnel ̸= clairvoyant
→les actions peuvent ne pas avoir les effets escompt´
es
⇒Rationnel ̸= efficace
⇒Un agent rationnel explore, apprend, est autonome
6
PEAS
PEAS
• PEAS : Performance measure, Environment, Actuators, Sensors
• Pour concevoir un agent rationnel, il faut pouvoir sp´
ecifier son
environnement
• Exemple : Taxi automatis´
e
• Mesure de performance : s´
ecurit´
e, destination, profits, confort, . . .
• Environnement : rues, traffic, pi´
etons, temps, . . .
• Actionneurs : volant, acc´
el´
erateur, frein, klaxon, . . .
• Capteurs : vid´
eo, acc´
el´
erom`
etre, GPS, . . .
7
Types d’environnement
Types d’environnement
• Totalement observable vs. Partiellement observable
• Mono agent vs. Multi agent
• D´
eterministe vs. Stochastique
• Episodique vs. S´
equentiel
• Statique vs. Dynamique
• Discret vs. Continu
⇒Monde r´
eel ?
8
Types d’environnement
Observable
D´
eterministe
Episodique
Statique
Discret
Agent
Echecs
Totalement
D´
eterministe
S´
equentiel
Statique
Discret
Multi
Mots crois´
es
Totalement
D´
eterministe
S´
equentiel
Statique
Discret
Mono
Poker
Partiellement
Stochastique
S´
equentiel
Statique
Discret
Multi
Diag. m´
edical
Partiellement
Stochastique
S´
equentiel
Dynamique
Continu
Mono
Taxi
Partiellement
Stochastique
S´
equentiel
Dynamique
Continu
Multi
Analyse d’images
Totalement
D´
eterministe
Episodique
Statique
Discret
Mono
9
Structure des agents
Structure des agents
• Agent = architecture + programme
• Architecture : syst`
eme, capteurs, actionneurs...
• Programme : 4 types basiques
• Agent r´
eflexe simple
• Agent r´
eflexe avec ´
etat
• Agent focalis´
e sur l’objectif
• Agent focalis´
e sur l’utilit´
e
10
Agent r´
eflexe simple
Agent
Environment
Sensors
What the world
is like now
What action I
should do now
Condition−action rules
Actuators
11
Agent r´
eflexe avec ´
etat
Agent
Environment
Sensors
What action I
should do now
State
How the world evolves
What my actions do
Condition−action rules
Actuators
What the world
is like now
12
Agent focalis´
e sur l’objectif
Agent
Environment
Sensors
What it will be like
  if I do action A
What action I
should do now
State
How the world evolves
What my actions do
Goals
Actuators
What the world
is like now
13
Agent focalis´
e sur l’utilit´
e
Agent
Environment
Sensors
What it will be like
  if I do action A
How happy I will be
   in such a state
What action I
should do now
State
How the world evolves
What my actions do
Utility
Actuators
What the world
is like now
14
Conclusion
Conclusion
• Les agents int´
eragissent avec leur environnement `
a travers des
capteurs et des actionneurs
• La mesure de performance ´
evalue l’environnement
• Un agent rationnel maximise la performance attendue
• La fonction de l’agent d´
ecrit ce que l’agent doit faire en toute
circonstance
• Le programme de l’agent impl´
emente des fonctions d’agent
• Le PEAS permet de sp´
ecifier l’environnement
15
