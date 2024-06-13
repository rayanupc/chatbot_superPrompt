Intelligence artificielle
Algorithmes de recherche en IA
Elise Bonzon
elise.bonzon@u-paris.fr
LIPADE - Universit´
e Paris Cit´
e
http://www.math-info.univ-paris5.fr/∽bonzon/
1
Algorithmes de recherche en IA
1. Les diff´
erents types de probl`
eme
2. Exemples de probl`
emes
3. Algorithmes de recherche de base (recherche aveugle)
4. Strat´
egies de recherche non-inform´
ees
2
Les diff´
erents types de probl`
eme
Les diff´
erents types de probl`
emes
• D´
eterministe, compl`
etement observable
• L’agent sait exactement dans quel ´
etat il est, et dans quel ´
etat il sera
• La solution est une s´
equence d’actions
• Non-observable →probl`
eme sans possibilit´
e de percevoir
l’environnement
• L’agent n’a aucune id´
ee d’o`
u il est r´
eellement
• La solution est une s´
equence d’actions
• Non-d´
eterministe ou partiellement observable →probl`
eme dans
lesquels il faut g´
erer des ´
eventualit´
es
• Les perceptions fournissent de nouvelles informations sur l’´
etat
courant
• Souvent les phases de recherche et d’ex´
ecution sont entrelac´
ees
• L’espace d’´
etats est inconnu →probl`
eme d’exploration
3
Exemple : Le monde de l’aspirateur
Probl`
eme d´
eterministe compl`
etement observable
• Etat initial : #5
• Etat final : #8
• Solution : ⟨droite, aspire⟩
4
Exemple : Le monde de l’aspirateur
Probl`
eme non d´
eterministe partiellement observable
• Non-d´
eterministe : aspirer ne
garantit pas que le sol soit
propre
• Partiellement observable : on
ne sait pas si le sol `
a droite
est propre
⇒Etats initiaux : {#5, #7}
• Solution :
⟨droite, si sol sale alors
aspire⟩
5
Exemple : Le monde de l’aspirateur
Probl`
eme d´
eterministe non observable
• Etats initiaux : {#1, #2,
#3, #4, #5, #6, #7, #8}
• Solution pour {#1, #3, #5,
#7} :
⟨aspire, droite, aspire⟩
• Solution pour {#2, #4 #6,
#8} :
⟨gauche, aspire, droite,
aspire⟩
6
Exemple de probl`
eme : le voyage en Roumanie
Arad
Zerind
Timisoara
Oradea
Sibiu
Lugoj
Mehadia
Dobreta
Craiova
Rimnicu Vilcea
Fagaras
Pitesti
Bucharest
Giurgiu
Urziceni
Hirsova
Eforie
Vaslui
Lasi
Neamt
75
118
71
140
151
111
70
75
120
80
146
99
138
97
211
101
90
85
98
80
142
92
87
7
Les probl`
emes d´
eterministes et compl`
etement observables
• Un probl`
eme d´
eterministe et compl`
etement observable est d´
efini
par :
1. un ´
etat initial
• par exemple, “`
a Arad”
2. un ensemble d’actions ou une fonction de transition, succ(x) :
• par exemple, succ(Arad) = {Zerind, Timisoara, Sibiu}
3. un test de terminaison pour savoir si le but est atteint
• explicite, e.g., “`
a Bucharest”
• implicite, e.g., “v´
erifier mat au ´
echec”
4. un coˆ
ut (additif)
• ¸
ca peut ˆ
etre la somme des distances, le nombre d’actions ex´
ecut´
ees,
etc.
• par exemple, c(x, a, y) ≥0 est le coˆ
ut de l’action a qui permet de
passer de l’´
etat x `
a l’´
etat y
• Une solution est une s´
equence d’actions partant de l’´
etat initial et
menant `
a l’´
etat but.
8
L’espace d’´
etats
• Le monde r´
eel est trop complexe pour ˆ
etre mod´
elis´
e
• L’espace de recherche mod´
elise une vue abstraite et simplifi´
ee du
monde r´
eel
• Un ´
etat abstrait repr´
esente un ensemble d’´
etats r´
eels
• Une action abstraite repr´
esente une combinaison complexe
d’actions r´
eelles
• par exemple,“Arad →Zerind”repr´
esente un ensemble de routes
possibles, de d´
etours, d’arrˆ
ets, etc.
• Une action abstraite doit ˆ
etre une simplification par rapport `
a une
action r´
eelle
• Une solution abstraite correspond `
a un ensemble de chemins qui
sont solutions dans le monde r´
eel.
9
Exemples de probl`
emes
Exemple : Espace d’´
etats du monde de l’aspirateur
R
L
S
S
S
S
R
L
R
L
R
L
S
S
S
S
L
L
L
L
R
R
R
R
• ´
Etats ? sol sale ou propre, position de l’aspirateur
• Actions ? droite, gauche, aspire
• Test du but ? les deux pi`
eces doivent ˆ
etre propres
• Coˆ
ut du chemin ? 1 par action
10
Exemple : Le jeu du taquin
• ´
Etats ? les positions des pi`
eces
• Actions ? d´
eplacement droite, gauche, haut, bas
• Test du but ? ´
etat but donn´
e
• Coˆ
ut du chemin ? 1 par d´
eplacement
11
Exemple : Le robot assembleur
• ´
Etats ? coordonn´
ees du robot, angles, position de l’objet `
a
assembler...
• Actions ? d´
eplacements continus
• Test du but ? objet compl`
etement assembl´
e
• Coˆ
ut du chemin ? le temps d’assemblage
12
Exemple de probl`
emes r´
eels
• Recherche de parcours
• Itin´
eraires automatiques, guidage routier, planification de routes
a´
eriennes, routage sur les r´
eseaux informatiques, ...
• Robotique
• Assemblage automatique, navigation autonome, ...
• Planification et ordonnancement
• Horaires, organisation de tˆ
aches, allocation de ressources, ...
13
Algorithmes de recherche de
base (recherche aveugle)
Algorithme de recherche de base (recherche aveugle)
• Id´
ee de base
• Recherche hors ligne, i.e. exploration de l’espace d’´
etats en g´
en´
erant
des successeurs d’´
etats d´
ej`
a g´
en´
er´
es (d´
evelopper des ´
etats)
• G´
en´
eration d’un arbre de recherche
• On s’arrˆ
ete lorsqu’on a choisi de d´
evelopper un nœud qui est un
´
etat final
1
function
Tree -Search(Pb ,Strat) returns a Sol or Fail
2
initialize
the
search
tree
using
the
initial
state of Pb
3
loop do
4
if there is no
candidate
to expand
then
return
Fail
5
choose a leaf
node to expand
according
to Strat
6
if the
node
contains a goal
state
then
return
Sol
7
else
expand ; add the
resulting
nodes to the
search
tree
14
Exemple de probl`
eme : le voyage en Roumanie
Arad
Zerind
Timisoara
Oradea
Sibiu
Lugoj
Mehadia
Dobreta
Craiova
Rimnicu Vilcea
Fagaras
Pitesti
Bucharest
Giurgiu
Urziceni
Hirsova
Eforie
Vaslui
Lasi
Neamt
75
118
71
140
151
111
70
75
120
80
146
99
138
97
211
101
90
85
98
80
142
92
87
15
Exemple : arbre de recherche
Arad
Fagaras
Oradea
Rimnicu Vilcea
Sibiu
Zerind
Timisoara
Arad
16
Impl´
ementation des algorithmes de recherche
• Structure de donn´
ees nœud qui contient
• ´
etat
• parent
• enfant
• profondeur
• coˆ
ut du chemin (not´
e g(x))
• Expand cr´
ee de nouveaux nœuds
• InsertAll ins`
ere de nouveaux nœuds dans la liste `
a traiter
17
Algorithme de recherche dans les arbres
1
function
TreeSearch(Pb ,fringe) returns a Sol or Fail
2
fringe ←Insert(MakeNode(InitialState (Pb)), fringe)
3
loop do
4
if fringe is empty
then
return
Fail
5
node ←RemoveFront(fringe)
6
if
GoalTest(Pb , State(node )) then
return
Sol(node)
7
fringe ←InsertAll(Expand(node , Pb), fringe)
1
function
Expand(node ,Pb) returns a set of nodes
2
successors ←∅
3
for
each
action ,result in
SuccessorFN(Pb ,State(node )) do
4
s ←a new
node
5
ParentNode (s) ←node
6
Action(s) ←action
7
State(s) ←result
8
PathCost(s) ←PathCost(node) + StepCost(node ,action ,s)
9
Depth(s) ←Depth(node) + 1
10
add s to
successors
11
return
successors
18
Etats versus Nœuds
• Un ´
etat est une repr´
esentation d’une configuration physique du
monde
• Un nœud est une structure de donn´
ees qui est partie int´
egrante de
l’arbre de recherche et qui inclue :
• l’´
etat
• le parent, i.e. le nœud p`
ere
• l’action r´
ealis´
ee pour obtenir l’´
etat contenu dans le nœud
• le coˆ
ut g(x) pour atteindre l’´
etat contenu dans le nœud depuis l’´
etat
initial
• la profondeur du nœud, i.e., la distance entre le nœud et la racine de
l’arbre
19
Strat´
egie de recherche
• Les diff´
erents attributs des nœuds sont initialis´
es par la fonction
Expand
• Une strat´
egie de recherche est d´
efinie par l’ordre dans lequel les
nœuds sont d´
evelopp´
es, i.e., la fonction InsertFn
• Une strat´
egie s’´
evalue en fonction de 4 dimensions :
• la compl´
etude : est ce que cette strat´
egie trouve toujours une
solution si elle existe ?
• la complexit´
e en temps : le nombre de nœuds cr´
e´
es
• la complexit´
e en m´
emoire : le nombre maximum de nœuds en
m´
emoire
• l’optimalit´
e : est ce que la strat´
egie trouve toujours la solution la
moins coˆ
uteuse ?
20
Strat´
egie de recherche
• La complexit´
e en temps et en m´
emoire se mesure en termes de :
• b : le facteur maximum de branchement de l’arbre de recherche,
i.e., le nombre maximum de fils des nœuds de l’arbre de recherche
• d : la profondeur de la solution la moins coˆ
uteuse
• m : la profondeur maximale de l’arbre de recherche
→attention peut ˆ
etre ∞
21
Strat´
egies de recherche
non-inform´
ees
Strat´
egies de recherche non-inform´
ees (aveugles)
• Les strat´
egies de recherche non-inform´
ees (dites aveugles) utilisent
seulement les informations disponibles dans le probl`
eme
• Il existe plusieurs strat´
egies :
• Recherche en largeur d’abord
• Recherche en coˆ
ut uniforme
• Recherche en profondeur d’abord
• Recherche en profondeur limit´
ee
• Recherche it´
erative en profondeur
22
Strat´
egies de recherche
non-inform´
ees
Recherche en largeur d’abord (BFS)
Recherche en largeur d’abord (BFS)
• InsertFn ajoute les successeurs en fin de liste (c’est une file)
• fringe = [E, F, G]
D
E
F
G
B
C
A
23
Recherche en largeur d’abord
• Complet, si b est fini
• Complexit´
e en temps :
1 + b + b2 + b3 + . . . + bd + (bd+1 −b) = O(bd+1)
• Complexit´
e en espace : O(bd+1) (garde tous les nœuds en m´
emoire)
• Optimale si coˆ
ut = 1 pour chaque pas, mais non optimale dans le
cas g´
en´
eral
⇒L’espace est le plus gros probl`
eme
24
Recherche en largeur d’abord
• b = 10
• 1 million de nœuds par seconde
• 1000 octets de m´
emoire pour un nœud
Profondeur
Nœuds
Temps
M´
emoire
5
106
1.1 secondes
1 Go
8
109
16 minutes
1 Teraoctet, 1024 Go
11
1012
13 jours
1 Petaoctets
13
1014
3.5 ans
99 Petaoctets
15
1016
350 ans
10 Exaoctets
25
Quand s’arrˆ
ete-t’on ?
• Supposons que le but est satisfait dans le nœud G
• On s’arrˆ
ete quand on d´
eveloppe le nœud G, soit apr`
es avoir
d´
evelopp´
e 7 nœuds : [A, B, C, D, E, F, G]
G
H
D
E
F
G
B
C
A
26
Strat´
egies de recherche
non-inform´
ees
Recherche en coˆ
ut uniforme
Recherche en coˆ
ut uniforme
• La fonction InsertFn ajoute les nœuds dans l’ordre du coˆ
ut g(x)
• fringe = [(G, 11), (B, 15)]
S
A
B
C
G
1
15
5
10
5
5
G, 11
G, 10
A, 1
B, 15
C, 5
S, 0
27
Recherche en coˆ
ut uniforme
• Equivalent `
a la largeur d’abord si le coˆ
ut est toujours le mˆ
eme
• Complet si le coˆ
ut de chaque pas est strictement sup´
erieur `
a 0
• Complexit´
e en temps : nombre de nœuds pour lesquels g ≤C ∗, o`
u
C ∗est le coˆ
ut de la solution optimale
• Complexit´
e en espace : idem que la complexit´
e en temps
• Optimale car les nœuds sont d´
evelopp´
es en fonction de g
28
Strat´
egies de recherche
non-inform´
ees
Recherche en profondeur d’abord (DFS)
Recherche en profondeur d’abord (DFS)
• InsertFn ajoute les successeurs en d´
ebut de liste (c’est une pile)
• fringe = []
D
E
F
G
H
I J
K
B
C
A
29
Recherche en profondeur d’abord
• Non complet dans les espaces d’´
etats infinis ou avec boucle
• Il est possible d’ajouter un test pour d´
etecter les r´
ep´
etitions
• Complexit´
e en temps : O(bm)
• Tr`
es mauvais si m est beaucoup plus grand que b
• Bien moins bon que la recherche en largeur d’abord si m est plus
grand que d
• Complexit´
e en espace : O(bm)
• Lin´
eaire !
• Non optimale
30
Quand s’arrˆ
ete-t’on ?
• Supposons que le but est satisfait dans le nœud G
• On s’arrˆ
ete quand on d´
eveloppe le nœud G, soit apr`
es avoir
d´
evelopp´
e 4 nœuds : [A, B, D, G]
G
H
D
E
F
G
B
C
A
31
Strat´
egies de recherche
non-inform´
ees
Recherche en profondeur limit´
ee
Recherche en profondeur limit´
ee
• Algorithme de recherche en profondeur d’abord, mais avec une limite
l sur la profondeur
• Les nœuds de profondeur l n’ont pas de successeurs
• Exemple pour l = 2
D
E
F
G
B
C
A
32
Recherche en profondeur limit´
ee
• Complet si l ≥d
• Complexit´
e en temps : O(bl)
• Complexit´
e en espace : O(bl)
• Non optimale
33
Strat´
egies de recherche
non-inform´
ees
Recherche en profondeur it´
erative
Recherche en profondeur it´
erative
• Profondeur limit´
ee, mais en essayant toutes les profondeurs : 0, 1, 2,
3, . . .
• ´
Evite le probl`
eme de trouver une limite pour la recherche profondeur
limit´
ee
• Combine les avantages de largeur d’abord (compl`
ete et optimale),
mais a la complexit´
e en espace de profondeur d’abord
34
Recherche en profondeur it´
erative : l = 0
A
A
35
Recherche en profondeur it´
erative : l = 1
A
A
B
C
A
B
C
A
B
C
36
Recherche en profondeur it´
erative : l = 2
A
A
B
C
A
B
C
D
E
A
B
C
D
E
A
B
C
D
E
A
B
C
D
E
F
G
A
B
C
D
E
F
G
A
B
C
D
E
F
G
37
Recherche en profondeur it´
erative
• Peut paraˆ
ıtre du gaspillage car beaucoup de nœuds sont ´
etendus de
multiples fois
• Mais la plupart des nouveaux nœuds ´
etant au niveau le plus bas, ce
n’est pas important d’´
etendre plusieurs fois les nœuds des niveaux
sup´
erieurs
• Complet
• Complexit´
e en temps :
(d + 1)b0 + db1 + (d −1)b2 + . . . + bd = O(bd)
• Complexit´
e en espace : O(bd)
• Optimale : oui, si le coˆ
ut de chaque action est de 1. Peut ˆ
etre
modifi´
ee pour une strat´
egie de coˆ
ut uniforme
38
Quand s’arrˆ
ete-t’on ?
• Supposons que le but est satisfait dans le nœud G
• On s’arrˆ
ete quand on d´
eveloppe le nœud G, soit apr`
es avoir
d´
evelopp´
e 11 nœuds : [A, A, B, C, A, B, D, E, C, F, G]
G
H
D
E
F
G
B
C
A
39
Strat´
egies de recherche
non-inform´
ees
Algorithmes de recherche non inform´
es
R´
esum´
e des algorithmes de recherche
Crit`
eres
Largeur
d’abord
Coˆ
ut
uniforme
Prof.
d’abord
Prof.
limit´
ee
Prof.
it´
erative
Compl´
etude
Oui
Oui
Non
Oui si
l ≥d
Oui
Temps
O(bd+1)
O(b⌈C ∗/ϵ⌉)
O(bm)
O(bl)
O(bd)
Espace
O(bd+1)
O(b⌈C ∗/ϵ⌉)
O(bm)
O(bl)
O(bd)
Optimalit´
e -
coˆ
ut d’une
action = 1
Oui
Oui
Non
Non
Oui
Optimalit´
e -
cas g´
en´
eral
Non
Oui
Non
Non
Non
40
