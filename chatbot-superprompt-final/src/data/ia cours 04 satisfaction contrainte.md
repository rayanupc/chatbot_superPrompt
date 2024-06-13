Intelligence artificielle
Satisfaction de contraintes
Elise Bonzon
elise.bonzon@u-paris.fr
LIPADE - Université Paris Cité
http://www.math-info.univ-paris5.fr/∽bonzon/
1
Problèmes de satisfaction de contraintes
1. Exemples de CSP
2. Recherche en arrière pour les CSPs (backtracking search)
3. Structure des problèmes
4. Conclusion
2
Exemples de CSP
Problèmes de satisfaction de contraintes (CSP)
• Problèmes de recherche“classiques”:
• Un état est une“boite noire”
• N’importe quelle structure de données qui contient un test pour le
but, une fonction d’évaluation, une fonction successeur
• CSP :
• Un état est défini par un ensemble de variables Xi, dont les valeurs
appartiennent au domaine Di
• Le test pour le but est un ensemble de contraintes qui spécifient les
combinaisons autorisées pour les valeurs sur des sous-ensembles de
variables
• Exemple simple d’un langage formel de représentation
• Permet d’utiliser des algorithmes généraux plus efficaces que les
algorithmes de recherche standards
3
Exemple : coloriage de carte
Western
Australia
Northern
Territory
South
Australia
Queensland
New South Wales
Victoria
Tasmania
• Variables : WA, NT, SA, Q, NSW , V , T
• Domaines : Di = {rouge, vert, bleu}
• Contraintes : régions adjacentes de couleurs différentes
• Par exemple, WA ̸= NT (si le langage le permet)
• Ou (WA, NT) ∈{(rouge, vert), (rouge, bleu), (vert, rouge), . . .}
4
Exemple : coloriage de carte
Western
Australia
Northern
Territory
South
Australia
Queensland
New South Wales
Victoria
Tasmania
• Les solutions sont des affectations qui satisfont toutes les contraintes
• Par exemple, {WA = rouge, NT = vert, Q = rouge, NSW =
vert, V = rouge, SA = bleu, T = vert}
5
Pourquoi choisir un tel modèle ?
• L’utilisation des contraintes peut permettre d’éliminer un bon
nombre d’états
• par exemple dès que SA = bleu, aucun nœud voisin ne peut prendre
la couleur bleu.
• au lieu de devoir considérer 35 = 243 allocations possibles une fois
que SA = bleu, il ne reste plus que 25 = 32 allocations possibles !
• Dans les recherches dans les espaces d’états, on peut simplement
demander“cet état est-il oui ou non solution”
• avec un CSP, si une solution partielle n’est pas solution, on n’a pas
besoin de considérer ses complétions
• Représentation naturelle pour bons nombres de problèmes
intéressants
6
Autre exemple : problème des n-reines
On veut disposer n reines sur un échiquier de taille n × n sans qu’aucune
reine ne s’attaque. On réduit le nombre d’états en ajoutant que la reine i
est placée sur la colonne i.
• Variables : {R1, . . . , Rn}
• Le domaine pour chaque reine est l’ensemble des lignes :
Di = {1, . . . , n}
• Contraintes : les reines ne doivent pas s’attaquer entre elles
7
Autre exemple : Sudoku
• 81 variables, une pour chaque case
• Domaine de chaque case : Di = {1, 2, 3, 4, 5, 6, 7, 8, 9}
• Contraintes : allDiff par ligne, par colonne, et par sous-tableau
3 × 3
8
Autre exemple : puzzle cryptarithmétique
• Variables : F, T, U, W , R, O, X1, X2, X3
• Domaines : {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
• Contraintes :
• Alldiff (F, T, U, W , R, O)
• O + O = R + 10X1
• X1 + W + W = U + 10X2
• . . .
9
Autre exemple : problème d’ordonnancement
• On a un ensembles de tˆ
aches : les variables X = {T1, . . . , Tn}
• Chaque tˆ
ache Ti a une durée di
• Certaines tˆ
aches doivent ˆ
etre effectuées avant d’autres : les
contraintes
• Objectif : trouver un temps o`
u chaque tˆ
ache doit commencer : le
domaine
Par exemple :
• La tˆ
ache T1 dure d1 = 10mn et doit ˆ
etre effectuée avant la tˆ
ache
T2 :
T1 + d1 ≤T2
• T2 et T3 ne peuvent pas avoir lieu en mˆ
eme temps (par exemple car
les deux tˆ
aches utilisent un outil en commun)
(T3 + d3 ≤T4) ∨(T4 + d4 ≤T3)
10
Variétés de CSPs
• Variables discrètes
• Domaines finis : si de taille d, il y a O(dn) affectations complètes
• Par exemple, CSPs booléens, d = 2
• Domaines infinis (entiers, caractères...)
• Par exemple, mise en place d’un planning, avec date de début/de fin
pour chaque tˆ
ache
• Nécessite un langage de contraintes. Eg T1 + d1 ≤T2
• Si les contraintes sont linéaires, le problème est soluble
• Si les contraintes sont non linéaires, problème indécidable
• Variable continues
• Par exemple, temps de début/fin pour les observations du télescope
de Hubble
• Contraintes linéaires solubles en temps polynomial en utilisant des
méthodes de programmation linéaire
11
Variétés de contraintes
• Contraintes unaires, ne concernent qu’une seule variable
• Par exemple, SA ̸= vert
• Contraintes binaires, concernent une paire de variables
• Par exemple, SA ̸= WA
• Contraintes d’ordre plus élevé, concernent 3 variables ou plus
• Par exemple, contraintes sur les puzzles cryptarithmétiques
• Préférences (ou contraintes souples)
• Par exemple, rouge est mieux que vert
• Souvent représentable par un coˆ
ut associé `
a chaque affectation de
variable
⇒Problèmes d’optimisation avec des contraintes
12
Graphe de contraintes
• CSP binaires : chaque contrainte lie au maximum deux variables
• Graphe de contraintes : les nœuds sont des variables, les arcs
représentent les contraintes
Victoria
WA
NT
SA
Q
NSW
V
T
• Les algorithmes CSP utilisent les graphes de contraintes
• Permet d’accélerer la recherche : par exemple, colorier la Tasmanie
est un sous-problème indépendant
13
Graphe de contrainte non binaire : puzzle cryptarithmétique
O
W
T
F
U
R
+
O
W
T
O
W
T
F O U R
X2
X1
X3
• Variables : F, T, U, W , R, O, X1, X2, X3
• Domaines : {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
• Contraintes :
• Alldiff (F, T, U, W , R, O)
• O + O = R + 10X1
• X1 + W + W = U + 10X2
• . . .
14
Problèmes CSPs du monde réel
• Problèmes d’affectation (eg. qui enseigne quel cours ?)
• Problèmes d’emploi du temps
• Configuration de matériels
• Planification pour les transports
• Planification dans les usines
• Allocation de salles
• . . .
• Note : beaucoup de problèmes du mondé réel impliquent des
variables `
a valeurs réelles
15
Formulation de la recherche standard (recherche incrémentale)
• Les états sont définis par les valeurs des variables déj`
a affectées
• Etat initial : un ensemble d’affectations vides {}
• Fonction successeur : attribuer une valeur `
a une variable non encore
affectée, de fa¸
con cohérente (vis `
a vis des contraintes) `
a l’affectation
actuelle
• Test du but : toutes les variables sont affectées
16
Formulation de la recherche standard (recherche incrémentale)
• Cet algorithme de recherche marche pour tous les CSPs
• Chaque solution apparait `
a une profondeur de n s’il y a n variables
→Utiliser la recherche en profondeur d’abord
• n : nombre de variables ; d : taille du domaine des variables ; b :
facteur de branchement
• b = (n −p)d `
a profondeur p
→n!dn feuilles
→alors qu’il n’y a que dn affectations possible ! !
17
Recherche en arrière pour les
CSPs (backtracking search)
Backtracking search
• L’affectation des variables est commutative
• L’ordre dans lequel on affecte les variables n’a pas d’importance
• WA = rouge puis NT = vert est la mˆ
eme chose que NT = vert puis
WA = rouge
• Il n’y a donc besoin de ne considérer qu’une seule variable par
profondeur de l’arbre de recherche
→b = d, et donc dn feuilles
• Recherche en profondeur d’abord avec l’affectation d’une variable `
a
la fois est appelée recherche par retour arrière (backtracking search)
• Algorithme de recherche basique pour les CSPs
• Permet de résoudre le problème des n reines pour n ∼25
18
Algorithme de recherche par retour arrière
1
function
BACKTRACKING -SEARCH(csp) returns
sol/fail
2
return REC - BACKTRACKING ({}, csp)
1
function REC - BACKTRACKING (aff , csp) returns
sol/fail
2
if aff is
complete
then
return
aff
3
var ←SelectUnassignedVar (Var[csp], aff , csp)
4
for
each
value ∈OrderDomainValue (var , aff , csp) do
5
if value
consistent
with
aff
given
Constraints [csp] then
6
add {var = value} to aff
7
result ←REC - BACKTRACKING (aff , csp)
8
if result ̸= failure
then
return
result
9
remove {var = value} from
aff
10
return
failure
19
Exemple
20
Améliorer l’efficacité de la recherche par backtrack
1. Comment choisir la variable `
a affecter ensuite ?
(Select-Unassigned-Variable)
2. Comment ordonner les valeurs des variables ?
(Order-Domain-Values)
3. Est-il possible de détecter un échec inévitable plus tˆ
ot ?
4. Comment tirer avantage de la structure du problème ?
21
Améliorer l’efficacité du la recherche par backtrack
1. Comment choisir la variable `
a affecter ensuite ?
(Select-Unassigned-Variable)
2. Comment ordonner les valeurs des variables ?
(Order-Domain-Values)
3. Est-il possible de détecter un échec inévitable plus tˆ
ot ?
4. Comment tirer avantage de la structure du problème ?
22
Valeurs minimum restantes (MRV)
• Heuristique des valeurs minimum restantes (MRV)
⇒choisir une des variables ayant le moins de valeur“légale”possible
23
Heuristique du degré
• Si plusieurs variables ne peuvent pas ˆ
etre départagées par
l’heuristique MRV
• Heuristique du degré
⇒choisir la variable qui a le plus de contraintes `
a respecter parmi les
variables restantes
24
Améliorer l’efficacité du la recherche par backtrack
1. Comment choisir la variable `
a affecter ensuite ?
(Select-Unassigned-Variable)
2. Comment ordonner les valeurs des variables ?
(Order-Domain-Values)
3. Est-il possible de détecter un échec inévitable plus tˆ
ot ?
4. Comment tirer avantage de la structure du problème ?
25
Valeur la moins contraignante
• Etant donné une variable, choisir celle qui a la valeur la moins
contraignante
⇒la variable qui empˆ
eche le moins d’affectations possibles sur les
variables restantes
Allows 1 value for SA
Allows 0 values for SA
• Combiner ces heuristiques permet de résoudre le problème des n
reines, avec n = 1000
26
Améliorer l’efficacité du la recherche par backtrack
1. Comment choisir la variable `
a affecter ensuite ?
(Select-Unassigned-Variable)
2. Comment ordonner les valeurs des variables ?
(Order-Domain-Values)
3. Est-il possible de détecter un échec inévitable plus tˆ
ot ?
4. Comment tirer avantage de la structure du problème ?
27
Vérification en avant
• Idée : garder en mémoire les valeurs autorisée pour les variables qu’il
reste `
a affecter
• Arrˆ
ete la recherche lorsqu’une variable n’a plus de valeur“légale”
possible
WA
NT
Q
NSW
V
SA
T
28
Propagation de contraintes
• La vérification en avant permet de propager l’information des
variables affectées aux variables non affectées, mais ne permet pas
de détecter tous les échecs
WA
NT
Q
NSW
V
SA
T
• NT et SA ne peuvent pas ˆ
etre tous les deux bleus !
• La propagation de contraintes permet de vérifier les contraintes
localement
29
Consistance des arcs
Consistance des arcs
La forme la plus simple de propagation est de rendre les arcs consistants.
X →Y est consistant ssi pour toute valeur x de X, il y a au moins un
y autorisé
Exemple :
• Contrainte : Y = X 2
• Domaines : X et Y sont des chiffres
• DX = DY = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
• Pour rendre X arc consistant avec Y :
→Réduction `
a DX = {0, 1, 2, 3}
• Pour rendre Y arc consistant avec X :
→Réduction `
a DY = {0, 1, 4, 9}
30
Consistance des arcs - Retour au coloriage de carte
WA
NT
Q
NSW
V
SA
T
• Si X perd une valeur, les voisins de X doivent ˆ
etre revérifiés
• Repère un échec avant la vérification en avant
• Peut ˆ
etre lancé comme un pré-processeur ou après chaque affectation
31
Algorithme de vérification de consistance d’arcs
1
function AC -3( csp) returns
true/false
2
File Q
contenant
tous
les
arcs du csp
3
while Q n’est pas
vide do
4
(Xi, Xj) ←pop(Q)
5
if
RemoveInconsistantValue(Xi, Xj) then
6
// Vrai si le domine de Xi
a été réduit
7
if D(Xi ) est
vide //Pas de
8
return
false
9
else
for
each
voisins Xk
de Xi
do
10
ajouter (Xk, Xi) dans Q
1
function
RemoveInconsistantValue(Xi, Xj) returns
true/false
2
change ←false
3
for
each vi ∈D(Xi) do
4
if aucune
valeur vj ∈D(Xj) ne permet `
a (vi, vj) de
satisfaire
5
les
contraintes
en Xi
et Xj
then
6
enlève vi
de D(Xi)
7
change ←true
8
return
change
32
Améliorer l’efficacité du la recherche par backtrack
1. Comment choisir la variable `
a affecter ensuite ?
(Select-Unassigned-Variable)
2. Comment ordonner les valeurs des variables ?
(Order-Domain-Values)
3. Est-il possible de détecter un échec inévitable plus tˆ
ot ?
4. Comment tirer avantage de la structure du problème ?
33
Structure des problèmes
Structure des problèmes
Victoria
WA
NT
SA
Q
NSW
V
T
• La Tasmanie est un sous-problème indépendant
• Identifiables comme étant des composants connexes du graphe de
contraintes
34
CSPs structurés sous forme d’arbre
A
B
C
D
E
F
Théorème
Si le graphe de contraintes ne contient pas de cycles, le CSP a une
complexité en temps de O(nd2)
Cas général : complexité en temps de O(dn)
35
Algorithme pour les CSPs structurés sous forme d’arbre
1. Choisir une variable comme étant la racine, et ordonner les variables
de la racine aux feuilles, de fa¸
con `
a ce que le parent de chaque nœud
le précède
A
B
C
D
E
F
A
B
C
D
E
F
2. Pour j de n `
a 2, appliquer RemoveInconsistent(Parent(Xj), Xj)
3. Pour j de 1 `
a n, affecter Xj de fa¸
con `
a ce qu’il soit consistent avec
Parent(Xj)
36
CSPs quasiment structurés sous forme d’arbre
• Conditionnement : instancier une variable, restreindre les domaines
de ses voisins
Victoria
WA
NT
Q
NSW
V
T
T
Victoria
WA
NT
SA
Q
NSW
V
• Conditionnement du coupe-cycle : instancier (de toutes les fa¸
cons
possibles) un ensemble de variables de fa¸
con `
a ce que le graphe de
contraintes restant soit un arbre
• Cycle coupé de taille c ⇒complexité en O(dc × (n −c)d2)
• Très rapide pour c petit
37
Conclusion
Conclusion
• Formulation particulière d’un état avec un ensemble de couples
valeurs/attributs
• Les conditions d’une solution sont représentées par un ensemble de
contraintes sur les variables
• La recherche avec backtrack est une technique efficace
• Des heuristiques générales (indépendantes du domaine) permettent
de résoudre plus rapidement un CSP
• D’autres techniques utilisant la décomposition peuvent aussi ˆ
etre
efficaces.
38
