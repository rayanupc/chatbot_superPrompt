	  
 
UFR de Mathématiques  
et d'Informatique  
 
Licence de Mathématiques 
Licence d'Informatique 
 
L3 Semestre 6 
 Année 2021-2022 
Session initiale 
 
UE	  MT06X110	  
Corrigé	  de	  l'épreuve	  de	  Thermodynamique	  
	  
	  
NB	  :	  Tout	  signe	  distinctif	  porté	  sur	  la	  copie	  pouvant	  indiquer	  sa	  provenance	  constitue	  
une	  fraude.	  
	  
	  
Document	  et/ou	  matériel	  autorisés	  :	  AUCUN	  
	  
	  
Durée	  totale	  de	  l’épreuve	  :	  1h30	  
 
• 
Le sujet comporte 12 pages (page de garde et de 
complément de réponse incluses). 
 
• 
La réponse à chaque question devra être rédigée sur ce 
cahier-réponses, dans le cadre prévu à cet effet. Si nécessaire, la 
copie de couverture pourra être utilisée comme complément de 
réponse, à condition de bien préciser le numéro de l'exercice et 
de la question et d'indiquer le report au niveau de la case 
correspondante. 
 
• 
On prendra soin de faire apparaître les étapes 
intermédiaires principales des calculs dans les réponses 
données. 
 
• Les calculatrices sont interdites.	  
	  
2	  
Exercice 1 
On considère un fluide d’équation d’état : P(Vm −b) = RT , où P est sa pression, Vm son 
volume molaire,  T sa température, R la constante des gaz parfaits et b une constante positive 
et dimensionnée. 
 
1) Définir et calculer les 3 coefficients thermoélastiques de ce fluide. Préciser leur unité. 
 
* α = 1
Vm
∂Vm
∂T
⎛
⎝
⎜
⎞
⎠
⎟
P
 est le coefficient de dilatation isobare. Il s'exprime en K-1. 
Or, d'après l'équation d'état : Vm = RT
P + b   
donc : α = 1
Vm
∂Vm
∂T
⎛
⎝
⎜
⎞
⎠
⎟
P
= 1
Vm
R
P  =>  α = 1
Vm
R
P =
R
RT + Pb . 
 
* β = 1
P
∂P
∂T
⎛
⎝
⎜
⎞
⎠
⎟
Vm
 est le coefficient d’augmentation de pression isochore. Il s'exprime en K-1. 
Or, d'après l'équation d'état : 
 
P =
RT
Vm −b   
donc : 
 
β = 1
P
∂P
∂T
⎛
⎝
⎜
⎞
⎠
⎟
Vm
= 1
P
R
Vm −b = 1
T  =>  β = 1
T  . 
 
* 
 
χT = −1
Vm
∂Vm
∂P
⎛
⎝
⎜
⎞
⎠
⎟
T
 est le coefficient de compressibilité isotherme. Il s'exprime en Pa-1. 
 
=>  
 
χT = −1
Vm
∂Vm
∂P
⎛
⎝
⎜
⎞
⎠
⎟
T
= −1
Vm
−RT
P2 	   => 
 
χT = 1
Vm
RT
P2 =
RT
P(RT + Pb)  . 
 
 
2) Quelle relation existe-t-il entre ces 3 coefficients ? La vérifier. 
 
On peut vérifier la relation qui lie ces trois coefficients : α = βχTP . 
En effet, 
 
βχTP = 1
T
1
Vm
RT
P2 P = 1
Vm
R
P = α . 
 
3) Quelle est la signification physique du coefficient b ? Expliquer. 
 
Le coefficient b représente le covolume, c'est-à-dire ici le volume d'une mole de particules. 
Ainsi b/NA représente le volume propre d'une particule (atome ou molécule). En effet, les 
particules constituant le fluide ne sont pas ponctuelles, donc possèdent un volume propre. Ce 
volume réduit le volume effectivement accessible aux autres particules. 
 
	  
3	  
Exercice 2 : calorimétrie 
On admettra que les capacités calorifiques du calorimètre, de ses accessoires et de l'eau sont 
indépendantes de la température, donc constantes. 
 
1) Etalonnage du calorimètre 
Le calorimètre et ses accessoires sont initialement en équilibre thermique avec une masse 
d’eau froide m, à la température T1. On ajoute une masse d’eau chaude identique, m, mais de 
température T2. Une fois l’équilibre thermique réalisé, la température est Téq.  
a) A l’aide d’un bilan thermique sur le système {calorimètre-accessoires + masse d’eau froide 
+ masse d’eau chaude} considéré comme isolé, déterminer l'expression de la masse 
équivalente en eau du calorimètre et de ses accessoires, meau. On notera c la capacité 
calorifique de l'eau. 
 
* Premier principe appliqué à l'ensemble {calorimètre-accessoires + masse d’eau froide + 
masse d’eau chaude}, U étant une fonction d'état extensive : 
ΔUsyst = ΔUeau chaude + ΔUeau froide + ΔUcalorimètre = W +Q = 0 . 
 
W = 0 car les systèmes sont de volume constant (phases condensées (solides et liquides)). 
Q = 0 car le système total est isolé thermiquement de l'extérieur. 
 
* Pour une phase condensée : dU = mcdT , d'où :  ΔU = mcΔT 
Cette formule est à appliquer à chaque sous-système du système considéré. 
 
* Ainsi : mc(Téq −T2)+ mc(Téq −T
1)+ meauc(Téq −T
1) = 0  
=> m(2Téq −T2 −T
1)+ meau(Téq −T
1) = 0 
 
 
d'où : meau = m(T2 + T
1 −2Téq)
Téq −T
1
. 
 
 
b) Faire l'application numérique pour : m = 100g, T1 = 20°C, T2 = 100°C, Téq = 55°C. 
 
meau = 100(100 + 20 −110)
55 −20
= 1000
35 = 200
7 = 29g . 
 
 
c) Déterminer l'expression littérale de la variation d'entropie du système {calorimètre-
accessoires + masse d’eau froide + masse d’eau chaude}. Que nous dit le second principe sur 
cette variation ? (on ne cherchera pas à faire le calcul numérique). 
 
* Par extensivité de la fonction d'état entropie, on a : ΔSsyst = ΔSeau chaude + ΔSeau froide + ΔScalorimètre  
* Pour une phase condensée : dS = dU/T = mc dT/T  d'où : ΔS = mcln Tf
Ti
 (pour faire le calcul 
de la variation de S, on imagine une autre transformation, réversible, menant du même état 
initial au même état final. Sur ce chemin réversible, pour un système incompressible (ou 
phase condensée), on a :  dU = mc dT = TdS car dV = 0 et dN = 0).	  
 
	  
4	  
* Ainsi : ΔSsyst = ΔSeau chaude + ΔSeau froide + ΔScalorimètre = mcln Téq
T2
+ mcln Téq
T
1
+ meaucln Téq
T
1
 
=> ΔSsyst = c mln Téq
T2
+ mln Téq
T1
+ meau ln Téq
T1
⎛
⎝
⎜
⎞
⎠
⎟= mc ln Téq
2
T2T1
+ T2 +T1 −2Téq
Téq −T1
ln Téq
T1
⎛
⎝
⎜
⎞
⎠
⎟ > 0. 
Le second principe nous dit que cette variation est strictement positive, car le système total est 
isolé et la transformation irréversible si T2 ≠ T1. 
 
 
2) Détermination de la capacité calorifique c de l'eau 
Une masse m connue d'eau de température initiale T1 est en équilibre thermique avec un 
calorimètre dont on connaît la masse équivalente en eau meau. On immerge une résistance 
électrique (de résistance R) et on la relie pendant un temps t à une source de tension continue 
U. A l'aide du 1er principe, déterminer l'expression de la capacité calorifique c de l'eau en 
fonction de la température finale d'équilibre Tf de l'ensemble {eau + calorimètre} de T1, m, 
meau, R, U et t. 
 
Premier principe appliqué à l'ensemble {calorimètre-accessoires + eau} :  
ΔUsyst = ΔUeau + ΔUcalorimètre = W + Q = 0 + U 2
R t = U 2
R t . 
On a donc : mc(Tf −T1)+ meauc(Tf −T1) = U 2
R t  , d'où : c =
U 2t
R(m + meai)(Tf −T1) . 
 
 
3) Le calorimètre précédent est rempli d'une masse m d'eau à la température ambiante 
T0 = 20°C. On ajoute une masse de glace M de température Ts = 0°C. Le thermomètre se 
stabilise à la température Tf. Soit LF la chaleur latente massique de fusion de la glace. On 
supposera que toute la glace a fondu. 
a) Exprimer Tf en fonction de c, M, m, meau, T0, Ts et LF. 
 
* Premier principe appliqué à l'ensemble {calorimètre + eau + glace}, isolé : 
 
ΔUsyst = ΔUeau + ΔUglace + ΔUcalorimètre = mc(Tf −T0)+ meauc(Tf −T0)+ MLF + Mc(Tf −Ts) = 0  
 
d'où : (m + meau)c(Tf −T0)+ MLF + Mc(Tf −Ts) = 0  => Tf = (m + meau)cT0 + McTs −MLF
(m + meau + M )c
. 
 
 
b) Quel doit être le signe de Tf - Ts pour que toute la glace ait fondu ? En déduire la condition 
sur la masse de glace ajoutée M pour qu'elle soit bien toute fondue. 
 
Il faut que Tf - Ts > 0 pour que toute la glace ait fondu. A partir du résultat de la question 
précédente, on a : 
	  
5	  
	  
Tf −Ts = (m + meau)cT0 + McTs −MLF
(m + meau + M )c
−Ts = (m + meau)cT0 + McTs −MLF −(m + meau + M )cTs
(m + meau + M )c
 
 
Tf −Ts = (m + meau)c(T0 −Ts)−MLF
(m + meau + M )c
> 0  <=> (m + meau)c(T0 −Ts) > MLF  
 
soit : M < (m + meau) c (T0 −Ts)
LF
. 
 
 
Exercice 3 
Un moteur fonctionne entre une pseudo-source chaude de capacité thermique C = 10 kJ/K et 
de température initiale T01 = 360K et une pseudo-source froide de capacité thermique C et de 
température initiale T02 = 250K. Entre deux instants voisins, le moteur est approximativement 
un moteur cyclique ditherme réversible.  Aide de calcul : 25/36 = 0,69. 
 
1) Déterminer la température finale des pseudo-sources, le travail W' récupéré et la chaleur Q1 
fournie par la source chaude. 
 
* Sur un cycle élémentaire du moteur : 
 
1er principe  => 
 dU = 0 = δW + δQC + δQF  (1) 
 
2nd principe (cas réversible)  => 
 δQC /TC + δQF /TF = 0    (2)  
 
* Du point de vue de la source chaude (non idéale) : dUC = C dTC = - δQC  (3) 
 
* Du point de vue de la source froide (non idéale) : dUF = C dTF = - δQF  (4) 
 
En remplaçant dans (2), on a : - C dTC/TC - C dTF/TF = 0 ó d (lnTC ) + d (lnTF) = 0 
 
ó d(ln(TC TF)) = 0  ó  TC TF = cste = T01 T02 
 
Or dans l’état final, on aura TC = TF = Tf  
=>  Tf =
T
01T
02 =
360 × 250 = 300 K  
 
* Pour le travail reçu par le système :  δW = - δQC - δQF = C dTC + C dTF = C (dTC + dTF)  
 
=>  
 
W = C
dT
C
T01
Tf
∫
+
dTF
T02
Tf
∫
⎛
⎝
⎜
⎞
⎠
⎟== C 2Tf −T
01 −T
02
(
) = −100 kJ  . 
 
Le travail W' récupéré est donc de 100 kJ. 
 
* La chaleur fournie par la source chaude est : Q1 = QC = - C (Tf – T01) = 600 kJ. 
 
 
	  
6	  
2) Calculer le rendement global de ce moteur et comparer au rendement de Carnot si les deux 
sources de chaleur étaient idéales. 
 
* Le rendement global du moteur est : 
 
η = −W
QC
= W'
Q1
= 0,17 = 17% . 
 
* Le rendement de Carnot, si les deux sources de chaleur gardaient une température constante, 
serait : 
 
ηCarnot = 1−T
02
T
01
= 1−250
360 = 0,31= 31%  . 
 
* On vérifie que le rendement réel est inférieur au rendement de Carnot (moteur idéal). 
 
 
Exercice 4 : cycle de Joule 
Une mole d'air (assimilé à un gaz parfait diatomique, de rapport γ = CP/CV = 7/5 = 1,4) décrit 
le cycle suivant ABCDA : 
Etat A : T0 = 300 K, P0 = 1 bar   
 
 
 
 
Etat B : T1, P1 = k P0  
Etat C : T2 = 1000 K, P1  
 
 
 
 
 
Etat D : T3, P0  
 
Les transformations AB et CD sont adiabatiques réversibles. 
Les transformations BC et DA sont isobares. 
 
1) Déterminer les températures T1 et T3 en fonction de k, T0 et T2. Tracer l'allure du cycle 
dans le diagramme de Clapeyron, pour k > 1 (on supposera que k est tel que VD > VA). De 
quel type de cycle s'agit-il ? Justifier. 
 
Les transformations AB et CD sont adiabatiques réversibles et il s'agit d'un GP diatomique  
=> on utilise les lois de Laplace :  TγP1−γ = cste . 
 
* Sur AB, on a :  T
0
γP0
1−γ = T
1
γP
1
1−γ  => 
 
T
1 = T
0
P0
P
1
⎛
⎝
⎜
⎞
⎠
⎟
1−γ
γ
= T
0
1
k
⎛
⎝
⎜
⎞
⎠
⎟
1−γ
γ
= T
0k
γ−1
γ = T
0k
1−1
γ = T
0k
2
7  . 
 
* Sur CD, on a :  T2
γP
1
1−γ = T
3
γP0
1−γ  => 
 
T
3 = T2
P
1
P0
⎛
⎝
⎜
⎞
⎠
⎟
1−γ
γ
= T2k
1−γ
γ = T2k
1
γ −1
= T2k
−2
7  . 
 
* Allure du cycle dans le diagramme de Clapeyron (diagramme (P,V)) pour k > 1 : 
(ici exemple tracé pour k = 2) 
 
	  
7	  
 
* Le cycle étant parcouru dans le sens horaire, il s'agit d'un cycle moteur : W > 0. 
 
 
2) Déterminer littéralement puis numériquement (mais en fonction de R) les quantités de 
chaleur reçues par le gaz au cours de chaque transformation du cycle. En déduire le travail 
total reçu par le gaz au cours d'un cycle. De quel type de cycle s'agit-il ? Définir et déterminer 
son rendement (ou son efficacité). On donne pour k = 10 : T1 = 580 K, T3 = 520 K. 
 
* Sur les transformations AB et CD, adiabatiques, on a : QAB = QCD = 0. 
 
* Sur les transformations isobares BC et DA, on a :  
QBC = ΔUBC −WBC = 5
2 R(TC −TB)+ P
B(VC −VB) = 7
2 R(TC −TB) = ΔH BC  
soit : QBC = 7
2 R(T2 −T1) = 7
2 R(1000 −580) = 1470R  . 
 
De même sur DA : QDA = ΔUDA −WDA = 5
2 R(TA −TD)+ P
D(VA −VD) = 7
2 R(TA −TD) = ΔH DA  
soit : QDA = 7
2 R(T0 −T3) = 7
2 R(300 −520) = −770R  . 
 
* Travail reçu sur un cycle tel que : ΔUcycle = 0 = W +QAB +QBC +QCD +QDA  
On en déduit : W = −700R   < 0 => cycle moteur, comme trouvé à la question 1. 
 
* Rendement du cycle : η = −W
QBC
= 700R
1470R = 1
2,1 0,5 = 50% . 
 
 
	  
8	  
3) Les échanges thermiques du fluide ont uniquement lieu avec deux sources : une source 
chaude de température T2 et une source froide de température T0. Le cycle étudié est-il 
réversible ? Déterminer le rendement du cycle de Carnot qui fonctionnerait entre ces deux 
sources de chaleur. Commenter. 
 
Le cycle n'est pas réversible car les transformations où il y a échange avec les sources de 
chaleur (transformations monothermes) ne se font pas à température du système constante : 
elles ne se sont pas isothermes. 
 
Pour les rendre réversibles, pour chaque transformation isobare, il faudrait mettre le système 
en contact avec une infinité de sources de chaleur, de températures variant continûment 
depuis la température initiale du système jusqu'à celle finale. 
 
Le rendement du cycle de Carnot (cycle ditherme réversible) qui fonctionnerait entre ces deux 
sources de chaleur est : 
 
ηCarnot =1−T0
T2
=1−0,3 = 0,7 >η = 0,5  . 
 
 
4) Déterminer pour chaque transformation la variation d'entropie de l'air, l'entropie échangée 
et l'entropie créée, littéralement puis numériquement (en fonction de R). Le second principe 
est-il vérifié ? Le cycle est-il réversible ? 
On donne : ln 1000 = 6,9 ; ln 580 = 6,4 ; ln 520 =6,2 ; ln 300 = 5,7. 
 
* Sur les transformations AB et CD, adiabatiques réversibles, on a : ΔSAB = 0 = ΔSCD   
 
De même, sur ces transformations, Séchangé = 0 = Scréé. 
 
* Sur une transformation isobare réversible d'un GP :  
dH = Cp dT = d(U + PV) = dU + P dV = T dS - P dV + P dV = T dS 
 
d'où : dS = Cp dT /T, puis par intégration, de l'état initial à l'état final : ΔS = CP ln Tf
Ti
. 
 
* Sur la transformation isobare BC :  
ΔSBC = CP ln TC
TB
= 7
2 Rln T2
T
1
= 7
2 R(6,9 −6,4) = 7
4 R =1,75R . 
Par ailleurs, SBC
e = QBC
T2
= 1,47R  et SBC
c = ΔSBC −SBC
e = 0,28R . 
 
* Sur la transformation isobare DA :  
ΔSDA = CP ln TA
TD
= 7
2 Rln T0
T3
= 7
2 R(5,7 −6,2) = −7
4 R = −1,75R . 
Par ailleurs, SDA
e = QDA
T0
= −770
300 R = −2,6R   et SDA
c = ΔSDA −SDA
e = 0,85R . 
	  
9	  
 
* Sur l'ensemble du cycle, ΔScycle = 0 mais ΔScycle
univers = Scycle
créé = 0,28R + 0,85R = 1,13R > 0 . 
 
La variation d'entropie de l'univers (système isolé) est strictement positive, en accord avec le 
second principe pour une transformation irréversible. On vérifie ainsi que le cycle était bien 
irréversible. 
 
