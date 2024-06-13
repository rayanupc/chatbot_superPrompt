 
Année 2020-2021 
 
UFR MATHS INFO 
 
U.E. MT06X110 : Physique 6 (Thermodynamique) 
Corrigé de l'épreuve 
L3 Semestre 6 
Session 1 
Jeudi 6 mai 2021 
 
Durée	  :	  1h30	  
 
• 
Le sujet comporte 12 pages, y compris la page de garde et la page de 
complément de réponse. 
  
• 
La réponse à chaque question devra être rédigée sur ce cahier-réponses, 
dans le cadre prévu à cet effet. 
 
• 
La notation tiendra compte de la présentation des résultats et de la clarté de la 
copie.  
 
• 
Tout résultat illisible ou sans son unité sera compté comme nul. 
 
• 
Les étapes intermédiaires de calcul devront apparaître et les formules de 
cours éventuellement utilisées devront être justifiées. 
 
• 
Les calculatrices sont interdites. 
 
• 
Les 4 exercices sont indépendants. 
 
 
 
NOTE :                                                       SOIT   :                      / 20 
 
 
 
Exercice 1 : question de cours 
Rappeler le nom, la définition et l'unité des 3 coefficients thermo-élastiques, ainsi que la relation existant entre eux. 
 
* Coefficient de dilatation isobare :  α = 1
V
∂V
∂T
⎛
⎝
⎜
⎞
⎠
⎟
P  
 en K-1 
 
* Coefficient de compressibilité isotherme : χT = −1
V
∂V
∂P
⎛
⎝
⎜
⎞
⎠
⎟
T  
 en Pa-1 
 
 
* Coefficient d'augmentation de pression isochore : β = 1
P
∂P
∂T
⎛
⎝
⎜
⎞
⎠
⎟
V   
 en K-1 
 
 
Ils doivent vérifier  la relation : α = βχTP  .  
 
 
Exercice 2 
On considère une enceinte cylindrique fermée en haut par un piston horizontal de masse négligeable et de 
section s = 100 cm2. On suppose que les frottements du piston sont négligeables lors de ses déplacements. 
On renferme n moles d’air (assimilé à un gaz parfait diatomique) dans l’enceinte. 
 
Aides de calcul : ln (2) = 0,69.  
 
On prendra g = 10 m.s-2 pour la pesanteur terrestre, R = 8,3 J.K-1.mol-1 pour la constante des gaz parfaits.  
 
Dans l’état initial : 
T1 = Text = 300 K (température ambiante supposée constante)  
P1 = Pext = 1,00 bar (pression atmosphérique ambiante supposée constante). 
V1 = 100 L. 
 
On suppose que toutes les parois sont diathermales, c'est à dire qu'elles laissent passer la chaleur. 
 
PARTIE A 
On pose sur le piston une masse de 100 kg et on attend qu’un nouvel état d’équilibre du gaz (P2, T2, V2) 
s’établisse. 
 
1) Quelle est la nature de la transformation ? 
 
Transformation irréversible (car brutale, donc non quasi-statique), monotherme (Text = constante), 
monobare (Pext + mg/s = constante, du début à la fin). 
 
 
2) Déterminer le taux de compression τ = P2/P1, T2 et V2. 
 
* La transformation s’arrête quand il y a équilibre mécanique avec le milieu extérieur, soit :  
 
P2 = Pext + mg/s = 2.105 Pa = 2 bars   
=> 
 τ = P2 / P1 = 2. 
 
* Par équilibre thermique (parois diathermales) : T2 = T1 = 300 K  => P1V1 = P2V2 (n cst). 
 
=> V2 =V1 / 2 = 50 L 
 
 
3) Calculer W12 le travail reçu par le gaz au cours de la transformation. 
 
La pression extérieure appliquée au système durant la transformation est égale à P2 = Pext + mg/s = τ P1 ; 
elle est constante, donc : 
W
12 = −P2(V2 −V
1) = P2V2(τ −1) = P
1V
1(τ −1) =10 kJ . 
 
 
4) Calculer la variation d’entropie du gaz, du milieu extérieur et de l’univers. Commenter. 
 
* Pour le gaz (= l'air emprisonné) : 
 
ΔS = n 7
2 R ln T2
T
1
−R ln P2
P
1
⎛
⎝
⎜
⎞
⎠
⎟= −nR lnτ = −P
1V
1
T
1
ln2 = −23 J / K . 
* Pour le milieu extérieur : 
 
ΔSext = −Q12
Text
= W
12
T
1
= 10000
300 = 33 J / K   car  ΔU = W
12 + Q12 = 0 . 
 
*  ΔSuniv = ΔS+ ΔSext = 10 J / K > 0  => le second principe est bien vérifié (transformation irréversible). 
 
 
PARTIE B 
On repart de l’état initial (P1, T1, V1) et on comprime réversiblement l’air jusqu’à la pression P2. 
 
5) Comment pourrait-on réaliser une telle transformation ? Quelle est la nature de cette transformation ? 
 
On rajoute peu à peu des masselottes jusqu’à m = 100 kg. La transformation est réversible (lente et pas de 
frottements) et il y a contact thermique avec l’extérieur = > transformation isotherme réversible. 
 
 
6) Calculer à nouveau T’2, V’2, et W’12 le travail reçu par le gaz au cours de la transformation. Comparer 
ce travail à W12.  
 
* A la fin de la transformation, P2 = P1 + mg/s = 2 bars => τ = P2 / P1 = 2 (inchangé). 
 
* Par équilibre thermique (parois diathermanes) : T’2 = T1 = T2 = 300K (inchangé). 
 
=> V’2 =V1 / 2 = 50 L  (inchangé)   => On arrive au même état final que précédemment. 
 
* Par contre, l'expression du travail n'est plus la même, car la pression appliquée au système durant la 
transformation n'est plus constante : 
 
W'12 = −
PdV
V
1
V'2
∫
= −
nRT
1
V
dV
V
1
V'2
∫
= −P
1V
1ln V'2
V
1
= 6900 J < W
12 . 
7) Calculer la variation d’entropie du gaz, du milieu extérieur et de l’univers. Commenter. 
 
* Pour le gaz emprisonné : ΔS = n 7
2 Rln T2
T
1
−Rln P2
P
1
⎛
⎝
⎜
⎞
⎠
⎟= −nRln τ = −23 J / K , inchangé car même 
transformation globale pour le système (S est une fonction d'état donc sa variation est indépendante du 
chemin suivi). 
 
* Pour le milieu extérieur : 
 
ΔSext = −Q'12
Text
= W'12
T
1
= 23 J / K  , car  ΔU = W'12+ Q'12 = 0 . 
 
* ΔSuniv = ΔS + ΔSext = 0 J / K  
  => le second principe est bien vérifié (transformation réversible). 
 
 
Exercice 3 
Un moteur fonctionne entre une pseudo-source chaude (capacité thermique C, température initiale T01 = 800K) et 
une pseudo-source froide (capacité thermique 3C et température initiale T02 = 200K). Entre deux instants voisins t 
et t + dt, le moteur est approximativement un moteur cyclique ditherme réversible (cycle de Carnot, constitué de 
deux isothermes et de deux adiabatiques, réversibles).  
 
1) Représenter un cycle ditherme réversible décrit par le fluide dans le diagramme de Clapeyron et dans le 
diagramme entropique (T, S). Indiquer le sens de parcours de ces cycles en le justifiant. 
 
 
* Dans le diagramme de Clapeyron 
           ou diagramme (P,V) : 
 
 
 
 
 
* Dans le diagramme (T,S) : 
 
 
 
Le cycle étant moteur, W < 0 sur un cycle et Q = – W > 0. 
Le cycle est donc décrit dans le sens horaire (sens 1234) dans les deux diagrammes (l'aire algébrique du cycle est 
bien positive pour les deux diagrammes, le premier donnant - W et le second Q). 
  
 
5 
2) Exprimer le premier principe et le second principe pour un cycle infinitésimal ditherme réversible. On donnera 
l’expression de dU et de dS pour le fluide parcourant le cycle moteur en fonction des chaleurs infinitésimales δQ1 
et δQ2 reçues des deux sources, du travail infinitésimal reçu δW et des températures des sources à cet instant, T1 et 
T2. En déduire deux relations entre δW, δQ1 et δQ2. 
 
Sur un cycle élémentaire (ou infinitésimal) : 
 
* 1er principe => dU  = δW + δQ1 + δQ2  = 0    (1) 
 
* 2nd principe : cas réversible => dS = δSéchangé = δQ1 /T1 + δQ2 /T2 = 0   (2) 
 
 
3) Sachant qu’au cours d’un cycle infinitésimal la température de la pseudo-source chaude varie de dT1 et celle de 
la pseudo-source froide de dT2, exprimer les quantités de chaleur δQ1 et δQ2 reçues par le fluide de la part des 
sources de chaleur en fonction de C et des variations dT1 et dT2.  
 
* Du point de vue de la source chaude : dU1 = C dT1 = - δQ1  => δQ1 = - C dT1   
(3) 
 
* Du point de vue de la source froide : dU2 = 3C dT2 = - δQ2 => δQ2 = - 3C dT2     
(4) 
 
 
4) A l’aide des questions précédentes, déterminer la température finale des pseudo-sources, le travail récupéré et la 
chaleur Q1 fournie par la source chaude jusqu'à l'arrêt du moteur. On prendra : C = 10 kJ/K. 
 
* En reportant les expressions (3) et (4) dans la relation (2), on a : - C dT1/T1 - 3C dT2/T2 = 0,   
d'où :  dT1/T1 +  3 dT2/T2 = 0 ó  d (lnT1) + 3 d (lnT2) = 0 ó d (ln (T1 T2
3)) = 0  ó T1 T2
3 = cste = T01 T02
3. 
 
Or dans l’état final, on aura T1 = T2 = Tf => 
 
 
Tf =
T
01T
02
3
4
=
800.2003
4
=
26.108
4
= 2.102 2 280 K  . 
 
* Pour le travail, on utilise la relation : δW = - δQ1 - δQ2 = C dT1 + 3C dT2 = C (dT1 + 3 dT2).  
Par intégration, on obtient : W = - Q1 - Q2 = C (Tf - T01 + 3Tf - 3T02)   
 
=> W = C 4T
f −(T
01 + 3T
02)
(
) = C(1120 −1400) = −280C = −2800 kJ  . 
 
Le travail récupéré par l'extérieur (ou cédé par le moteur) est donc de 2800 kJ. 
 
* Pour la chaleur fournie par la source chaude (ou reçue par le système de la part de la source chaude), on a :  
 
 
 
 
Q1 = - C (Tf – T01) = 520 C = 5200 kJ. 
 
Pour la chaleur fournie par la source froide (ou reçue par le système de la part de la source froide), on a :  
 
 
 
 
Q2 = - 3C (Tf – T02) =  -240 C = - 2400 kJ  (=> chaleur cédée par le système à la source froide = 2400 kJ). 
 
 
5) Définir et calculer le rendement global de ce moteur. Comparer à celui de Carnot, qui aurait été obtenu si les 
deux sources de chaleur avaient gardé leur température initiale constante. 
 
Le rendement global du moteur est : η = −W
Q1
= 2800
5200 = 7
13 = 0,54 < ηC = 1−T02
T01
= 1−200
800 = 3
4 = 0,75  . 
 
Il est bien inférieur au rendement de Carnot, qui aurait été obtenu si les deux sources de chaleur avaient gardé leur 
température initiale constante. 
 
 
6 
Exercice 4 : Bilans énergétique et entropique de deux solides métalliques mis en contact 
On met en contact deux solides (1) et (2), l'un en fer, l'autre en cuivre, de masses respectives m1 = 0,4 kg et  
m2 = 0,05 kg et de températures correspondantes T10 = 500 K et T20 = 300 K. Les variations de volume des solides 
sont négligeables et l'ensemble forme un système isolé. En outre, les capacités thermiques massiques, à volume 
constant, de ces deux solides sont respectivement c1 = 450 J.K-1.kg-1 et c2 = 400 J.K-1.kg-1. 
 
1) Ecrire le bilan énergétique pour l'ensemble des deux solides, entre l'instant initial et l'état d'équilibre final. En 
déduire la température finale de l'ensemble des deux solides. Faire l'application numérique. 
 
Entre l'instant initial et l'instant final, nous avons, pour l’ensemble des deux solides : ΔU = W+ Q, où W est le 
travail reçu et Q la chaleur reçue par l'ensemble des deux solides. 
 
Comme le système est isolé thermiquement, il n’y a pas d’échange thermique avec l’extérieur : Q = 0. 
Comme le système est incompressible, son volume ne varie pas et il n'y a donc pas de travail reçu : W = 0. 
 
D’autre part : ΔU = ΔU1 + ΔU2 = m1 c1 ΔT1 + m2 c2 ΔT2 = 0. 
On en déduit, entre l'instant initial et l'état d'équilibre final : 0 = ΔU = m1 c1 (Tf - T10) + m2 c2 (Tf - T20). 
 
On a finalement :   Tf = m1 c1 T
10 + m2 c2 T20
m1 c1 + m2 c2
    soit : Tf = 480 K. 
 
 
2) Effectuer, entre l'instant initial et l'instant final, le bilan entropique pour l'ensemble des deux solides, en 
distinguant le terme d'échange et le terme de production éventuel. Quelle est la variation d'entropie du système ? 
Application numérique : ln(0,96) = - 0,041 et ln(1,6) = 0,47. Commenter le signe de cette variation. 
 
Entre l'instant initial et l'instant final, la variation d’entropie s’écrit : ΔS = Se + Sc , où Se est l’entropie échangée.  
Ici Se = 0 (système isolé thermiquement). Sc  est l’entropie produite (ou créée). 
De plus, ΔS = ΔS1 + ΔS2, avec : ΔS1 = 
m1c1
dT
T
T10
Tf
∫
 = m1 c1 ln Tf
T10
⎛
⎝
⎜
⎞
⎠
⎟ et ΔS2 = 
m2c2
dT
T
T20
Tf
∫
 = m2 c2 ln
Tf
T20
⎛
⎝
⎜
⎞
⎠
⎟.  
(S étant une fonction d’état, on peut imaginer une autre transformation, réversible, pour faire le calcul de sa 
variation). 
 
Donc : ΔS = Sc = m1 c1 ln Tf
T10
⎛
⎝
⎜
⎞
⎠
⎟ + m2 c2 ln
Tf
T20
⎛
⎝
⎜
⎞
⎠
⎟      ΔS = 2,0 J.K-1. 
 
On vérifie que : ΔS > 0 car le système isolé subit une transformation irréversible. 
 
