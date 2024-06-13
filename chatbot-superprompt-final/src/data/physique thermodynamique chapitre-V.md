CHAPITRE V
CYCLES THERMODYNAMIQUES.
APPLICATIONS AUX MACHINES THERMIQUES.
Chapitre V : Cycles thermodynamiques
1
2023-2024 – Stéphanie Moreau
SOMMAIRE
I – Transformations cycliques d’un système
II – Machines thermiques
III  – Machines monothermes
IV – Machines dithermes
V – Moteurs dithermes
VI – Machines frigorifiques
VII – Pompes à chaleur
VIII – EXERCICES
Chapitre V : Cycles thermodynamiques
2
2023-2024 – Stéphanie Moreau
•
Un fluide peut être soumis à 2 types de transformation, 
d’un point de vue mécanique :
Ø compression (son volume V diminue) => il reçoit du travail (W > 0)
Ø détente (son volume V augmente) => il fournit du travail (W < 0)
• Transformation quasi-statique : (Pext = P)
Le travail reçu par le système, W, est égal à l’opposé de l’aire 
algébrique hachurée dans le diagramme de Clapeyron (Ex ci-contre pour une transformation isobare : P = cste).
Ø Pour optimiser le travail récupéré, on peut utiliser le fait que le travail reçu par le système, W = - Wfourni
dépend du chemin suivi, puisque W n’est pas une fonction d’état => l’aire hachurée dépend de la relation      
P = f(V).
Ø Pour obtenir un travail conséquent, il faudrait que le volume atteigne des dimensions trop importantes => 
intérêt des machines thermiques où un retour cyclique à l’état initial permet d’obtenir un travail 
conséquent sans nécessiter de grandes variations de volumes.
I – TRANSFORMATIONS CYCLIQUES D’UN SYSTÈME
I-a) Etude mécanique (1)
2023-2024 – Stéphanie Moreau
Chapitre V : Cycles thermodynamiques
3
I – TRANSFORMATIONS CYCLIQUES D’UN SYSTÈME
I-a) Etude mécanique (2)
• Exemple d’un cycle quasi-statique,
constitué de 2 isobares et 2 isochores
Diagramme de Clapeyron ci-contre :
( = diagramme (P, V))
• L’aire algébrique hachurée en vert (seul)
correspond à Wfourni = - W. Sur le cycle
ABCDA (sens horaire), Wfourni > 0
=>  W < 0. C’est un cycle moteur.
2023-2024 – Stéphanie Moreau
Chapitre V : Cycles thermodynamiques
4
I – TRANSFORMATIONS CYCLIQUES D’UN SYSTÈME
I-a) Etude mécanique – Conclusion (3)
• Si le cycle est parcouru dans le sens ADCBA (sens trigonométrique)  l’aire 
algébrique hachurée en vert (seul) change de signe et devient négative. 
Sur le cycle ADCBA, Wfourni < 0 => W > 0 . C’est un cycle récepteur.
• CONCLUSION :
Ø Si un cycle est parcouru dans le sens horaire
(dans le diagramme de Clapeyron), il s’agit d’un 
cycle moteur : W = - │ aire du cycle │  < 0
Ø Si un cycle est parcouru dans le sens trigonométrique (dans le diagramme de 
Clapeyron), il s’agit d’un cycle récepteur : W = │ aire du cycle │  > 0
2023-2024 – Stéphanie Moreau
Chapitre V : Cycles thermodynamiques
5
I – TRANSFORMATIONS CYCLIQUES D’UN SYSTÈME
I-a) Etude mécanique – Exemples (4)
2023-2024 – Stéphanie Moreau
Chapitre V : Cycles thermodynamiques
6
I – TRANSFORMATIONS CYCLIQUES D’UN SYSTÈME
I-b) Etude thermique (1)
• Transformation réversible :
La chaleur reçue par le système durant 
une transformation réversible (Text= T )
est représentée par l’aire algébrique 
dans le diagramme (T, S) :
dS = dSéchangé + dScréé= dQ/Text + 0 = dQrév/T
d’où : Qrév = ∫1->2 dQrév = ∫1->2 T dS.
Sur le schéma ci-contre, Q = Qrév > 0.
2023-2024 – Stéphanie Moreau
Chapitre V : Cycles thermodynamiques
7
I – TRANSFORMATIONS CYCLIQUES D’UN SYSTÈME
I-b) Etude thermique (2)
• Cycle réversible : 
cycle => DUcycle = 0 = Wrév + Qrév => Wrév = - Qrév
• Exemple du cycle d’Otto ci-contre :
Qrév = aire algébrique du cycle 12341.
Le cycle est parcouru dans le sens horaire
=> aire > 0 => Qrév > 0 => Wrév < 0 => cycle moteur.
• NB : les aires sont égales dans les deux diagrammes !
• CONCLUSION :
Ø Si un cycle est parcouru dans le sens horaire (dans le diagramme (T,S)), il s’agit d’un cycle 
moteur : Qrév = aire du cycle > 0 => Wrév = - │ aire du cycle │  < 0 
Ø Si un cycle est parcouru dans le sens trigonométrique (dans le diagramme (T,S)), il s’agit d’un 
cycle récepteur : Qrév < 0 => Wrév = │ aire du cycle │ > 0
2023-2024 – Stéphanie Moreau
Chapitre V : Cycles thermodynamiques
8
T dS
cycle
!
∫
= Qrév = −Wrév =
PdV
cycle
!
∫
I – TRANSFORMATIONS CYCLIQUES D’UN SYSTÈME
I-b) Etude thermique – Exemples (3)
2023-2024 – Stéphanie Moreau
Chapitre V : Cycles thermodynamiques
9
• Cycle diesel :
Cycle de Stirling :
I – TRANSFORMATIONS CYCLIQUES D’UN SYSTÈME
I-c) Conclusion
2023-2024 – Stéphanie Moreau
Chapitre V : Cycles thermodynamiques
10
• Si un cycle est parcouru dans le sens horaire, dans 
le diagramme (T,S) ou dans le diagramme (P, V), il
s’agit d’un cycle moteur : 
Qrév = aire du cycle > 0 => Wrév = - │ aire du cycle │ < 0 
• Si un cycle est parcouru dans le sens trigonométrique,
dans le diagramme (T,S) ou dans le diagramme (P, V)), il 
s’agit d’un cycle récepteur : Wrév = │ aire du cycle │ > 0
II – MACHINES THERMIQUES 
II-a) Définition
• Une machine thermique (M) est un fluide qui subit des transformations cycliques au cours desquelles il 
échange du travail avec des systèmes mécaniques (S.M.) et de la chaleur avec des sources de chaleur ou 
thermostats (S.C).
•
Schéma général d’une machine thermique :
Ø Travail total reçu sur un cycle :
Ø Chaleur reçue de chaque thermostat i (ou source
de chaleur S.Ci) : Qi
•
Rappel de la convention : on compte positivement ce
qui est reçu par le fluide (M).
• Echange thermique avec les sources de chaleur :
Une source de chaleur (ou thermostat) est un système capable de fournir ou d’absorber de la chaleur tout en 
restant à la même température.
=> Cela nécessite une grande capacité calorifique (atmosphère, océans, …) ou un changement d’états.
2023-2024 – Stéphanie Moreau
Chapitre V : Cycles thermodynamiques
11
W =
Wj
j=1
m
∑
II – MACHINES THERMIQUES 
II-b) Bilans énergétique et entropique
•
Premier principe appliqué à (M), sur un cycle :
•
Second principe appliqué à {(M) + toutes les sources de chaleur} (= système isolé thermiquement) :
(2nd principe)
•
Pour la ième source de chaleur :
(transf° réversible pour les S.C. car elles sont très grandes et de température cste)         On tire : 
=>                          
•
Pour un cycle du fluide :
L’égalité correspond à un cycle réversible => Egalité de Clausius. 
L’inégalité stricte correspond à un cycle irréversible => Inégalité de Clausius.
2023-2024 – Stéphanie Moreau
Chapitre V : Cycles thermodynamiques
12
ΔUcycle =
Wj
j=1
m
∑
+
Qi
i=1
n
∑
= W +
Qi
i=1
n
∑
= 0 =>W = −
Qi
i=1
n
∑
ΔSi = Si,échangé + Si,créé = −Qi
Ti
+ 0 = −Qi
Ti
ΔStot = ΔS +
ΔSi
i=1
n
∑
= ΔS +
ΔSi
i=1
n
∑
≥0
ΔS = 0
ΔS −
Qi
Ti
i=1
n
∑
≥0
ΔS ≥
Qi
Ti
i=1
n
∑
Qi
Ti
i=1
n
∑
≤0
III – MACHINES MONOTHERMES
Þ machine en contact avec un seul thermostat durant son cycle.
• Bilan énergétique :
(1er principe)
• Bilan entropique : 
(inégalité de Clausius)
=> Q1 ≤ 0 => W ≥ 0
Une machine monotherme ne peut pas fournir de travail. Il n’existe pas de moteur monotherme.
• Principe de Carnot (formulation historique du second principe) :
Pour qu’un système décrivant un cycle fournisse du travail, il faut qu’il échange de la chaleur avec 
au moins deux sources de chaleur de températures différentes.
2023-2024 – Stéphanie Moreau
Chapitre V : Cycles thermodynamiques
13
W = −
Qi
i=1
n
∑
= −Q1
Qi
Ti
= Q1
T
1
i=1
n
∑
≤0
IV – MACHINES DITHERMES 
IV-a) Généralités
Þ machine en contact avec 2 thermostats de températures différentes       
(Tc > Tf) durant son cycle.
• Bilan énergétique (1er principe) :
• Bilan entropique (2nd principe) :
(inégalité de Clausius) 
2023-2024 – Stéphanie Moreau
Chapitre V : Cycles thermodynamiques
14
W = −
Qi
i=1
n
∑
= −(Qc + Qf )
Qi
Ti
= Qc
Tc
+
Qf
Tf
i=1
n
∑
≤0
IV – MACHINES DITHERMES 
IV-b) Cycle de Carnot (1)
• Il s’agit d’un cycle réversible ditherme composé de :
Ø 2 isothermes réversibles, correspondant aux 2 étapes du contact 
thermique du fluide avec chacune des deux sources de chaleur.
Ø 2 adiabatiques réversibles correspondant à des échanges 
mécaniques plutôt rapides.
• N.B. : ce cycle est un cycle idéalisé pour une machine thermique. La 
réversibilité nécessitant des transformations infiniment lentes, un tel 
cycle aurait une puissance tendant vers 0…
2023-2024 – Stéphanie Moreau
Chapitre V : Cycles thermodynamiques
15
IV – MACHINES DITHERMES 
IV-b) Cycle de Carnot (2)
• Ex d’un cycle récepteur :
Ø Calcul de Qc :
Ø Calcul de Qf :
Ø Calcul de W :
W = │ aire du cycle │ 
2023-2024 – Stéphanie Moreau
Chapitre V : Cycles thermodynamiques
16
W = −(Qc + Qf ) = (Tc −Tf )(SB −SC) > 0
Qc =
Tc dS
SB
SC
∫
= −Tc(SB −SC) < 0
Qf =
Tf dS
SD
SA
∫
= Tf (SA −SD) > 0
IV – MACHINES DITHERMES 
IV-c) Diagramme de Raveau (1)
• Il s’agit de la représentation dans un diagramme (Qc, Qf) des zones 
utilisables par une machine ditherme.
• Premier principe (cycle ditherme) 
=>
=> selon que W < 0 ou > 0, on sera au-dessus ou en 
dessous de la droite y = - x dans le diagramme (Qc , Qf) 
• Second principe (inégalité de Clausius pour un cycle ditherme) 
le 2nd principe interdit de se trouver au-dessus de la     
=>
droite y = - (Tc /Tf ) x dans le diagramme (Qc , Qf)
2023-2024 – Stéphanie Moreau
Chapitre V : Cycles thermodynamiques
17
Qc = −Qf −W
Qc ≤−Tc
Tf
Qf
IV – MACHINES DITHERMES 
IV-c) Diagramme de Raveau (2)
On peut distinguer 4 zones :
• zone I : W < 0 => moteur
Qc > 0 et Qf < 0
• zone II : W > 0 => récepteur
Qc < 0 et Qf > 0 => PAC, machines frigo
• zone III : W > 0 => récepteur
Qc > 0 et Qf < 0 => sans intérêt
• zone IV : W > 0 => récepteur
Qc < 0 et Qf < 0 => sans intérêt
2023-2024 – Stéphanie Moreau
Chapitre V : Cycles thermodynamiques
18
V – MOTEURS DITHERMES (zone I)
W < 0, Qc > 0 et Qf < 0
• Un moteur ditherme est un système qui permet au cours d’un cycle de fournir un travail 
Wfourni = – W > 0, en prélevant de l’énergie à la source chaude. 
L’inconvénient est qu’il faut transférer une partie de cette énergie à la source froide, ce qui limite 
le rendement du moteur.
• Le rendement h d’un moteur ditherme est le rapport entre le travail fourni par le moteur et la 
chaleur prélevée à la source chaude : 
• Le rendement maximal ou rendement de Carnot d’un moteur ditherme est :
=> Pour avoir le rendement le plus élevé possible, il faut : Tf << Tc
• Exercice : déterminer la température minimale Tc de la source chaude pour qu’un moteur 
ditherme ayant pour source froide un thermostat de température Tf = 27°C, ait un rendement de 
75%.
2023-2024 – Stéphanie Moreau
Chapitre V : Cycles thermodynamiques
19
0 < η =
Wfourni
Qc
= −W
Qc
<1
ηmax = 1−
Tf
Tc
VI – MACHINES FRIGORIFIQUES (zone II)
W > 0, Qf > 0 et Qc < 0
• Une machine frigorifique fonctionne en recevant du travail afin de prélever de la chaleur à la 
source froide et d’en fournir à la source chaude.
• Son intérêt est de maintenir la température de la source froide (qui n’est pas idéale) à une 
température constante, pour compenser les fuites thermiques.
• Définition de l’efficacité de cette machine : 
• L’efficacité maximale ou efficacité de Carnot d’une machine frigorifique est :
=> Pour que l’efficacité soit la plus grande possible, il faut : Tf ≈ Tc
• Remarque : le principe du réfrigérateur fait intervenir un changement d’état.
• Exercice : Un climatiseur sert à maintenir la température d’un bâtiment à 22°C tandis que 
l’atmosphère extérieure est à la température 35°C. Un bilan énergétique sur le bâtiment a montré 
qu’on devait lui prélever Pther = 4 kW pour maintenir sa température constante. Quelle doit être la 
puissance du climatiseur utilisé ?
2023-2024 – Stéphanie Moreau
Chapitre V : Cycles thermodynamiques
20
0 < ef =
Qf
W
emax = eCarnot =
Tf
Tc −Tf
VII – POMPES A CHALEUR (zone II)
W > 0, Qf > 0 et Qc < 0
• Une pompe à chaleur permet au cours d’un cycle de prélever de la chaleur à la source 
froide afin de restituer de l’énergie à la source chaude. Pour cela, il faut fournir un 
travail au système.
• Son intérêt est de maintenir la température de la source chaude (qui n’est pas idéale) 
à une température constante, pour compenser les fuites thermiques.
• Définition de l’efficacité de cette machine : 
NB : ep > 1
• L’efficacité maximale ou efficacité de Carnot d’une pompe à chaleur est :
=> Pour que l’efficacité soit la plus grande possible, il faut : Tf ≈ Tc
• Exercice : Une pompe à chaleur sert à maintenir la température d’un bâtiment à 20°C 
tandis que l’atmosphère extérieure est à la température de 0°C. Déterminer l’efficacité 
maximale de cette pompe à chaleur. Si on a fourni un travail Wélec, quel est la chaleur 
reçue par la source chaude ? Comparer avec un radiateur ordinaire.
2023-2024 – Stéphanie Moreau
Chapitre V : Cycles thermodynamiques
21
0 < ep = −Qc
W
emax = eCarnot =
Tc
Tc −Tf
VIII – EXERCICES
Exercice 1
On fait subir à une mole de gaz parfait diatomique le cycle de transformations suivant :
-
Etat initial = état (1) : P1 = 1 bar, T1 = 300K, V1. 
Le gaz subit d’abord une compression adiabatique réversible qui l’amène à l’état (2) :
-
Etat (2) : P2, T2, V2 = 10 L.
Le gaz subit ensuite une détente isotherme réversible qui ramène son volume à V1 :
-
Etat (3) : P3, T3, V3 = V1
Pour fermer le cycle, on met le gaz en contact avec une source de chaleur de température constante T1 et en maintenant son volume constant. 
On rappelle que R = 8,32 J/K/mol.
1) Représenter ce cycle dans le diagramme de Clapeyron.
2) Déterminer la pression P2, la température T2, le travail reçu par le gaz W12 et ses variations d’énergie interne et d’entropie lors de la première 
transformation, en fonction de P1, T1 et V2. 
3) Exprimer en fonction des grandeurs données ou calculées, la pression P3 et la température T3, la quantité de chaleur Q23 reçue par le gaz au cours de la 
seconde transformation, ses variations d’énergie interne, d’enthalpie et d’entropie.
4) Pour la dernière transformation, déterminer la quantité de chaleur Q31 reçue par le gaz, ses variations d’énergie interne, d’enthalpie et d’entropie.
5) On considère une machine thermique fonctionnant selon ce cycle. 
a) Le cycle est-il moteur ou récepteur ? Est-ce en accord avec l’énoncé de Carnot du second principe ?
b) Déterminer, selon le cas, le rendement ou l’efficacité de cette machine thermique.
c) Comparer au cas d’une machine thermique suivant un cycle ditherme réversible de Carnot fonctionnant entre les deux sources de chaleur 
précédentes. Conclure.
2023-2024 – Stéphanie Moreau
Chapitre V : Cycles thermodynamiques
22
VIII – EXERCICES
Exercice 2
Un moteur fonctionne entre une pseudo-source chaude constituée 
d’eau liquide de capacité thermique C = 4,18 kJ/K et de température 
initiale T01 = 320K et une pseudo-source froide constituée d’eau liquide 
de capacité thermique C et de température initiale T02 = 280K. 
Entre deux instants voisins, le moteur est approximativement un 
moteur cyclique ditherme réversible. 
1) Déterminer la température finale des pseudo-sources, le travail W 
récupéré et la chaleur Q1 fournie par la source chaude.
2) Calculer le rendement global et commenter.
2023-2024 – Stéphanie Moreau
Chapitre V : Cycles thermodynamiques
23
VIII – EXERCICES
Exercice 3
Une pompe à chaleur fonctionne suivant un cycle de Carnot décrit par un fluide qui reçoit du travail et échange de la chaleur avec 
deux thermostats. Ce cycle est constitué de deux transformations adiabatiques et de deux transformations isothermes, toutes les 
quatre réversibles. 
La pompe à chaleur utilise l’air comme fluide et est destinée à chauffer la carlingue d’un avion volant à haute altitude. La source 
froide est constituée par l’atmosphère extérieure à la pression P1 et à la température T1 = 245 K. La source chaude est l’atmosphère 
de la carlingue à la pression P2 et à la température T2 = 293 K. On assimilera l’air à un gaz parfait diatomique de masse molaire 
29g/mol. On désigne par VA et VD < VA les volumes de l’air aux extrémités A et D de l’isotherme T1 et par VB et VC < VB les volumes de 
l’air aux extrémités B et C de l’isotherme T2. On désigne par g le rapport CP/CV.
1) Représenter le cycle décrit par le fluide dans le diagramme de Clapeyron et dans le diagramme entropique (T,S).
2) Déterminer dans quel sens sont parcourus ces diagrammes en justifiant.
3) Déterminer en fonction du travail reçu W au cours du cycle, de T1 et T2, les quantités de chaleur Q1 et Q2 reçues par le fluide de la 
part des sources de chaleur. Déterminer leur signe.
4) Exprimer en fonction de VA, VB, VC, VD, T1 et T2, les travaux reçus par 1kg d’air lors de chacune des 4 transformations du cycle.
5) Déterminer en fonction de VA = 2,4m3, VC = 0,85m3,  T1 et T2, le travail total W reçu lors du cycle.
6) Calculer la quantité de chaleur fournie par la source froide et celle reçue par la carlingue.
7) Calculer l’efficacité de cette pompe à chaleur. Comment la déterminer sans calculs intermédiaires ?
8) Les déperditions de chaleur de l’avion étant de 6 kcal/s, quelle doit être la puissance minimale du compresseur de la pompe à
chaleur pour maintenir constante la température à l’intérieur de la carlingue à la valeur T2 = 293K, la température extérieure étant    
T1 = 245 K ?
2023-2024 – Stéphanie Moreau
Chapitre V : Cycles thermodynamiques
24
