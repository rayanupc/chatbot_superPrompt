Intelligence artificielle
Algorithmes et recherches heuristiques
Elise Bonzon
elise.bonzon@u-paris.fr
LIPADE - Universit´
e Paris Cit´
e
http://www.math-info.univ-paris5.fr/∽bonzon/
1
Algorithmes et recherches heuristiques
1. Recherche meilleur d’abord
2. Recherche gloutonne
3. L’algorithme A∗
4. Algorithmes de recherche locale
2
Recherche meilleur d’abord
Recherche meilleur d’abord
• Rappel : Une strat´
egie de recherche permet de choisir l’ordre dans
lequel les ´
etats sont d´
evelopp´
es
• Id´
ee : Utiliser une fonction d’´
evaluation f pour chaque nœud
→mesure l’utilit´
e d’un nœud
→introduction d’une fonction heuristique h(n) qui estime le coˆ
ut du
chemin le plus court pour se rendre au but
• Comme dans les algorithmes de recherche aveugle, g(n) mesure le
coˆ
ut du chemin de l’´
etat initial au nœud n
• InsertAll ins`
ere le nœud par ordre d´
ecroissant de la valeur de la
fonction d’´
evaluation
• Cas sp´
eciaux :
• Recherche gloutonne (un choix n’est jamais remis en cause)
• A∗
3
Recherche gloutonne
Recherche gloutonne
• Fonction d’´
evaluation f (n) = h(n) (heuristique)
• h(n) : estimation du coˆ
ut de n vers l’´
etat final
• Par exemple, hdd(n) est la distance `
a vol d’oiseau entre la ville n et
Bucharest
• La recherche gloutonne d´
eveloppe le nœud qui paraˆ
ıt le plus
proche de l’´
etat final, sans prendre en compte le coˆ
ut du chemin
d´
ej`
a parcouru
4
Le voyage en Roumanie
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
Ligne droite jusqu’`
a Bucharest
Arad
366
Bucharest
0
Craiova
160
Dobreta
242
Eforie
161
Fagaras
176
Giurgiu
77
Hirsova
151
Lasi
226
Lugoj
244
Mehadia
241
Neamt
234
Oradea
380
Pitesti
100
Rimnicu Vilcea
193
Sibiu
253
Timisoara
329
Urziceni
80
Vaslui
199
Zerind
374
5
Recherche gloutonne : un autre exemple
• Supposons que le but est satisfait dans le nœud G
• On s’arrˆ
ete quand on d´
eveloppe le nœud G, soit apr`
es avoir
d´
evelopp´
e 3 nœuds, dans l’ordre : [A, C, G]
G, h = 0
H, h = 5
D, h = 2
E, h = 12
F, h = 1
G, h = 0
B, h = 9
C, h = 1
A, h = 14
5
15
8
3
2
1
2
4
6
Recherche gloutonne
• Compl´
etude : Incomplet (peut rester bloqu´
e dans des boucles)
• Exemple : Arad →Zerind →Arad →. . .
• Complet si on ajoute un test pour ´
eviter les ´
etats r´
ep´
et´
es
• Temps : O(bm)
• Une bonne heuristique peut am´
eliorer grandement les performances
• Espace : O(bm) : Garde tous les nœuds en m´
emoire
• Optimale : Non
7
L’algorithme A∗
Algorithme A∗
• Id´
ee : ´
Eviter de d´
evelopper des chemins qui sont d´
ej`
a chers
• Fonction d’´
evaluation : f (n) = g(n) + h(n)
• g(n) est le coˆ
ut de l’´
etat initial `
a l’´
etat n
• h(n) est le coˆ
ut estim´
e pour atteindre l’´
etat final
• f (n) est le coˆ
ut total estim´
e pour aller de l’´
etat initial `
a l’´
etat final
en passant par n
• A∗utilise une heuristique admissible
• h(n) ≤h∗(n) o`
u h∗(n) est le coˆ
ut r´
eel pour aller de n jusqu’`
a l’´
etat
final
• Une heuristique admissible ne surestime jamais le coˆ
ut r´
eel pour
atteindre le but. Elle est optimiste
• Par exemple hdd ne surestime jamais la vraie distance
• Si h(n) = 0 pour tout n, alors A∗est ´
equivalent `
a l’algorithme de
Dijkstra de calcul du plus court chemin
• Th´
eor`
eme : A∗est optimale
8
Le voyage en Roumanie
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
Ligne droite jusqu’`
a Bucharest
Arad
366
Bucharest
0
Craiova
160
Dobreta
242
Eforie
161
Fagaras
176
Giurgiu
77
Hirsova
151
Lasi
226
Lugoj
244
Mehadia
241
Neamt
234
Oradea
380
Pitesti
100
Rimnicu Vilcea
193
Sibiu
253
Timisoara
329
Urziceni
80
Vaslui
199
Zerind
374
9
Algorithme A∗: un autre exemple
• Supposons que le but est satisfait dans le nœud G
• On s’arrˆ
ete quand on d´
eveloppe le nœud G, soit apr`
es avoir
d´
evelopp´
e 4 nœuds, dans l’ordre : [A, B, D, G]
f = h + g
G, f = 0 + 15 = 15
H
f = 5 + 17 = 22
D, f = 2 + 13 = 15
E
f = 12 + 8 = 20
F
f = 1 + 17 = 18
G, f = 0 + 16 = 16
B, f = 9 + 5 = 14
C, f = 1 + 15 = 16
A, f = 14 + 0 = 14
5
15
8
3
2
1
2
4
10
Preuve d’optimalit´
e de A∗
• Supposons qu’il y ait un ´
etat final non optimal G ′ g´
en´
er´
e dans la
liste des nœuds `
a traiter
• Soit n un nœud non d´
evelopp´
e sur le chemin le plus court vers un
´
etat final optimal G
start
n
G
G ′
f (G ′)
=
g(G ′) car h(G ′) = 0
>
g(G) car G ′ n’est pas optimale
≥
f (n) car h est admissible
• f (G ′) > f (n), donc A∗ne va pas choisir G ′
11
Algorithme A∗
• Compl´
etude : Oui, sauf s’il y a une infinit´
e de nœuds tels que
f ≤f (G)
• Temps : exponentielle selon la longueur de la solution
• Espace : exponentielle (garde tous les nœuds en m´
emoire)
• Habituellement, on manque d’espace bien avant de manquer de
temps
• Optimale : Oui
12
Que faire si f d´
ecroˆ
ıt ?
• Avec une heuristique admissible, f peut d´
ecroˆ
ıtre au cours du
chemin
• Par exemple, si p est un successeur de n, il est possible d’avoir
n
p
g = 4, h = 8, f = 12
g = 5, h = 4, f = 9
• On perd de l’information
• f (n) = 12, donc le vrai coˆ
ut d’un chemin `
a travers n est ≥12
• Donc le vrai coˆ
ut d’un chemin `
a travers p est aussi ≥12
⇒Au lieu de f (p) = g(p) + h(p), on utilise
f (p) = max(g(p) + h(p), f (n))
→f ne d´
ecroˆ
ıt jamais le long du chemin
13
Exemple d’heuristiques admissibles : le taquin
• h1(n) = le nombre de pi`
eces mal plac´
ees
→h1(S) = 8
• h2(n) = la distance de Manhattan totale (la distance de chaque pi`
ece
entre sa place actuelle et sa position finale en nombre de places)
→h2(S) = 3 + 1 + 2 + 2 + 2 + 3 + 3 + 2 = 18
14
Dominance
• h1 domine h2 si h1 et h2 sont admissibles et que h1(n) ≥h2(n) pour
tout n
• h1 est alors meilleure pour la recherche
• Exemple :
d = 12
IDS : 3644035 nœuds
A∗(h1) : 227 nœuds
A∗(h2) : 73 nœuds
d = 24
IDS : trop de nœuds
A∗(h1) : 39135 nœuds
A∗(h2) : 1641 nœuds
15
Comment trouver des heuristiques admissibles ?
• Consid´
erer une version simplifi´
ee du probl`
eme
• Le coˆ
ut exact d’une solution optimale du probl`
eme simplifi´
e est une
heuristique admissible pour le probl`
eme original
• Exemple : simplification des r`
egles du taquin
• une pi`
ece peut ˆ
etre d´
eplac´
ee partout
→h1(n) donne la plus petite solution
• une pi`
ece peut ˆ
etre d´
eplac´
ee vers toutes les places adjacentes
→h2(n) donne la plus petite solution
16
R´
eduire la m´
emoire utilis´
ee par A∗:SMA∗
• Au pire des cas, A∗doit m´
emoriser tous les nœuds
• Id´
ee : utiliser une m´
emoire limit´
ee pour stocker les nœuds
• SMA∗: Simplified memory-bounded A∗
• Proc`
ede comme A∗: ´
etend les meilleurs nœud en fonction de la
valeur de f , jusqu’`
a ce que la m´
emoire soit pleine
• ´
Eliminer le nœud ayant la plus grande valeur f , et rapatrier la valeur
de ce nœud `
a son p`
ere
→permet de garder en m´
emoire la valeur du chemin passant par ce
nœud oubli´
e
• SMA∗parcourt ce sous-arbre seulement si tous les autres chemins
´
etudi´
es se sont montr´
es comme ´
etant pires que celui oubli´
e
• Si tous les nœuds ont la mˆ
eme valeur f , SMA∗´
etend le nœud le plus
r´
ecent, et oublie le plus ancien
• Complet si une solution est `
a une profondeur inf´
erieure `
a la taille de
la m´
emoire
• Optimal si d est inf´
erieur `
a la taille de la m´
emoire
17
Algorithmes de recherche locale
Algorithmes de recherche locale
• Dans de nombreux probl`
emes d’optimisation, soit
• La solution recherch´
ee est juste l’´
etat optimal (ou proche de
l’optimalit´
e) et non le chemin qui y m`
ene ;
• Il y a une fonction objective `
a optimiser ;
• L’espace d’´
etats est trop grand pour ˆ
etre enregistr´
e.
• L’´
etat lui-mˆ
eme est la solution
• Id´
ee : Modifier l’´
etat en l’am´
eliorant au fur et `
a mesure
• Espace d’´
etats : ensemble des configurations possible des ´
etats
• Besoin de d´
efinir une fonction qui mesure l’utilit´
e d’un ´
etat
18
Exemple : les n reines
• Placer n reines sur un plateau de taille n × n, sans que deux reines se
trouvent sur la mˆ
eme ligne, colonne ou diagonale
• D´
eplacer une reine pour r´
eduire le nombre de conflits
h = 5
h = 2
h = 0
19
Algorithmes de recherche locale
• Une recherche locale garde juste certains ´
etats visit´
es en m´
emoire :
• Le cas le plus simple est hill-climbing qui garde juste un ´
etat (l’´
etat
courant) et l’am´
eliore it´
erativement jusqu’`
a converger `
a une solution.
• Le cas le plus ´
elabor´
e est celui des algorithmes g´
en´
etiques qui
gardent un ensemble d’´
etats (appel´
e population) et le fait ´
evoluer
jusqu’`
a obtenir une solution.
• Il y a souvent une fonction objective `
a optimiser (maximiser ou
minimiser)
• Dans le cas de hill-climbing, elle permet de d´
eterminer l’´
etat
successeur.
• Dans le cas des algorithmes g´
en´
etiques, on l’appelle la fonction de
fitness. Elle intervient dans le calcul de l’ensemble des ´
etats
successeurs de l’´
etat courant.
• En g´
en´
eral, une recherche locale ne garantie pas de solution
optimale, mais elle permet de trouver une solution acceptable
rapidement
20
Algorithmes de recherche locale
Les algorithmes d´
edi´
es
• Ascension/descente de gradient (hill climbing)
• Descente de gradient stochastique
• Recuit simul´
e (Simulated annealing)
• Recherche en faisceau (Beam search)
• Recherche en faisceau stochastique
• Algorithmes g´
en´
etiques
21
Algorithmes de recherche locale
Ascension du gradient
Algorithme d’ascension du gradient (Hill Climbing)
• Le nœud courant est initialis´
e `
a l’´
etat initial.
• It´
erativement, le nœud courant est compar´
e `
a ses successeurs
imm´
ediats.
• Le meilleur voisin imm´
ediat et ayant la plus grande valeur que le
nœud courant, devient le nœud courant
• Si un tel voisin n’existe pas, on arrˆ
ete et on retourne le nœud
courant comme solution.
22
Exemple : les n reines
• VALUE (ou h) : nombre de paires
de reines qui s’attaquent
mutuellement directement ou
indirectement
• On cherche `
a minimiser cette valeur
• ´
Etat actuel : h = 17
• Les chiffres dans chaque case
indiquent le nombre de cas de
conflits en mettant la reine de la
colonne sur cette case
• Encadr´
es : les meilleurs successeurs
23
Algorithme d’ascension du gradient (Hill Climbing)
On cherche un maximum global
current
state
objective function
state space
global maximum
local maximum
"flat" local maximum
shoulder
Comme monter l’Everest dans un ´
epais brouillard, en ´
etant amn´
esique
24
Ascension du gradient
• On peut aussi consid´
erer la descente du gradient
• On peut ˆ
etre bloqu´
e dans un maximum (ou un minimum) local, ou
sur un plateau
• Solution : on admet des mouvements de cˆ
ot´
e
25
Algorithmes de recherche locale
Recuit simil´
e
Recuit simil´
e (simulated annealing)
• Am´
elioration de l’algorithme hill-climbing pour minimiser le risque
d’ˆ
etre pi´
eg´
e dans des maxima/minima locaux
• Au lieu de regarder le meilleur voisin imm´
ediat du nœud courant, on
va regarder avec une certaine probabilit´
e un moins bon voisin
imm´
ediat
• On esp`
ere ainsi s’´
echapper des optima locaux
• La probabilit´
e de prendre un moins bon voisin diminue graduellement
26
Algorithmes de recherche locale
Recherche taboue
Tabu Search
• L’algorithme de recuit simul´
e minimise le risque d’ˆ
etre pi´
eg´
e dans
des optima locaux
• Mais il n’´
elimine pas la possibilit´
e d’osciller ind´
efiniment en revenant
`
a un nœud ant´
erieurement visit´
e
• Id´
ee : On pourrait enregistrer les nœuds visit´
es
• Impraticable si l’espace d’´
etats est trop grand
• L’algorithme Tabu Search (recherche taboue) enregistre seulement
les k derniers nœuds visit´
es
• L’ensemble Tabou est l’ensemble contenant les k nœuds
• Le param`
etre k est choisi empiriquement
• Cela n’´
elimine pas les oscillations, mais les r´
eduit
27
Algorithmes de recherche locale
Local beam search
Beam Search
• Id´
ee : plutˆ
ot que maintenir un seul nœud solution n, en pourrait
maintenir un ensemble de k nœuds diff´
erents
• Ensemble de k nœuds choisis initialement al´
eatoirement
• A chaque it´
eration, tous les successeurs des k nœuds sont g´
en´
er´
es
• On choisit les k meilleurs parmi ces nœuds et on recommence
• Cet algorithme est appel´
e Local Beam Search (exploration locale par
faisceau)
• A ne pas confondre avec Tabu Search
• Stochastic Beam Search : plutˆ
ot que prendre les k meilleurs, on
assigne une probabilit´
e de choisir chaque nœud, mˆ
eme s’il n’est pas
parmi les k meilleurs (comme dans Simulated Annealing)
28
Algorithmes de recherche locale
Algorithme g´
en´
etique
Algorithme g´
en´
etique
1. G´
en´
eration al´
eatoire de n de s´
equences de bits (la population
initiale (appel´
ee aussi soupe))
2. Mesure de l’adaptation (fitness) de chacune des s´
equences
3. Cr´
eer une nouvelle population de taille n
3.1 Croisement : S´
election de 2 s´
equences parents (chaque parent est
s´
electionn´
e avec une probabilit´
e proportionnelle `
a son adaptabilit´
e) et
en les croisant avec une certaine probabilit´
e
3.2 Mutation d’un bit choisi al´
eatoirement dans une ou plusieurs
s´
equences tir´
ees au sort.
3.3 Recommencer jusqu’`
a avoir une population de taille n
4. Si la population satisfait le crit`
ere d’arrˆ
et, arrˆ
eter. Sinon, retour `
a
l’´
etape 2.
29
Croisement : Exemple avec 8 reines
+
=
67247588 + 75251447 = 67251447
30
Algorithme g´
en´
etique : Exemple avec 8 reines
32252124
Selection
Cross−Over
Mutation
24748552
32752411
24415124
24
23
20
32543213
11
29%
31%
26%
14%
32752411
24748552
32752411
24415124
32748552
24752411
32752124
24415411
24752411
32748152
24415417
Fitness
Pairs
• Fonction de fitness : nombre de paires de reines qui ne s’attaquent
pas (min = 0, max = (8x7)/2 = 28)
• Pourcentage de fitness (c-`
a-d., probabilit´
e de s´
election de la
s´
equence) :
24/(24 + 23 + 20 + 11) = 31%
23/(24 + 23 + 20 + 11) = 29%
20/(24 + 23 + 20 + 11) = 26%
11/(24 + 23 + 20 + 11) = 14%
31
