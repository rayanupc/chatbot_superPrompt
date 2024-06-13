 
 
UFR de Mathématiques  
et d'Informatique  
 
Licence de Mathématiques 
Licence d'Informatique 
 
L3 Semestre 6 
 Année 2022-2023 
Session initiale 
 
UE MT06X110 
Corrigé de l’épreuve de Thermodynamique 
 
 
NB : Tout signe distinctif porté sur la copie pouvant indiquer sa provenance constitue 
une fraude. 
 
Document et/ou matériel autorisés :  
calculatrice non programmable et non graphique 
 
 
Durée totale de l’épreuve : 1h30 
 
• 
Le sujet comporte 12 pages (page de garde et de 
complément de réponse incluses). 
 
• 
La réponse à chaque question devra être rédigée sur ce 
cahier-réponses, dans le cadre prévu à cet effet. Si nécessaire, la 
copie de couverture pourra être utilisée comme complément de 
réponse, à condition de bien préciser le numéro de l'exercice et de 
la question et d'indiquer le report au niveau de la case 
correspondante. 
 
• 
On prendra soin de faire apparaître les étapes 
intermédiaires principales des calculs dans les réponses 
données. 
 
 
 
2 
Exercice 1 
On considère un fluide d’équation d’état : 
, où P est sa pression, v son 
volume molaire, T sa température, R la constante des gaz parfaits et a une constante positive et 
dimensionnée. 
 
1) Définir et déterminer les 3 coefficients thermoélastiques de ce fluide. Préciser leur unité. 
 
* Coefficient de dilatation isobare : 
    en K-1.  
 
* Coefficient de compressibilité isotherme : 
   en Pa-1. 
 
* Coefficient d’augmentation de pression isochore : 
    en K-1.  
 
 
2) Quelle relation existe-t-il entre ces 3 coefficients ? La vérifier. 
 
On a la relation : 
 . 
On peut par exemple calculer à partir de cette relation : 
=> 
. 
On retrouve bien la même formule. La relation est donc vérifiée. 
 
Exercice 2 : calorimétrie  
On admettra que les capacités calorifiques du calorimètre, de ses accessoires et de l'eau sont 
indépendantes de la température, donc constantes. 
 
Les 3 questions sont indépendantes. 
 
1) Un calorimètre contient une masse m1 = 200g d'eau. La température initiale de l'ensemble 
est T1 = 20°C. On ajoute une masse m2 = 300g d'eau à la température T2 = 80°C.  
a) Quelle serait la température d'équilibre thermique Te de l'ensemble si la capacité calorifique 
du calorimètre et de ses accessoires était négligeable ?  
 
* Premier principe appliqué à l'ensemble {calorimètre-accessoires + masse d’eau froide + 
masse d’eau chaude}, U étant une fonction d'état extensive : 
v(T,P) = RT
P −a
2 P
α = 1
v
∂v
∂T
⎛
⎝
⎜
⎞
⎠
⎟
P
= R
Pv
χT = −1
v
∂v
∂P
⎛
⎝
⎜
⎞
⎠
⎟
T
= 1
v
RT
P2 + a
2
⎛
⎝
⎜
⎞
⎠
⎟= 1
P + a
v
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
v
=
R
v + aP
(
)P
α = βχTP
 
β =
α
χTP =
R
Pv
1
P + a
v
⎛
⎝
⎜
⎞
⎠
⎟P
β =
R
v + aP
(
)P
 
3 
. 
 
W = 0 car les systèmes sont de volume constant (phases condensées (solides et liquides)). 
Q = 0 car le système total est isolé thermiquement de l'extérieur (calorimètre). 
 
* Pour une phase condensée : dU = mcdT, d'où :  DU = mcDT. 
Cette formule est à appliquer à chaque sous-système du système considéré. 
 
* Ainsi : 
. 
 
La capacité calorifique du calorimètre étant supposée négligeable, on a : 
 
 <=> 
 
 
d'où :  
 . 
 
 
b) On mesure en fait une température d'équilibre thermique Te = 50°C. Déterminer la masse 
équivalente en eau du calorimètre et de ses accessoires.  
 
Cela signifie que la capacité calorifique du calorimètre n’est pas négligeable. Ainsi : 
 
 
ó 
 
 
ó 
 . 
 
 
2) On plonge un échantillon de laiton de masse m2 = 200g de température T2 = 90°C dans un 
nouveau calorimètre de capacité calorifique totale C = 200 J.K-1 contenant une masse m1 = 300g 
d'eau. L'ensemble est à la température initiale T1 = 39°C. On mesure la température d'équilibre 
thermique final : Te = 89°C. Déterminer la capacité calorifique massique du laiton. 
Données : capacité calorifique massique de l'eau : ce = 4,18 J.g-1.K-1.  
 
* Premier principe appliqué à l'ensemble {calorimètre-accessoires + masse d’eau froide + 
échantillon de laiton}, U étant une fonction d'état extensive : 
 
 
ó 
 
 
ó 
 . 
 
ΔUsyst = ΔUeau chaude + ΔUeau froide + ΔUcalorimètre = W +Q = 0
m2ce(Te −T2)+ m1ce(Te −T1)+ Ccalorimètre(Te −T1) = 0
m2ce(Te −T2)+ m1ce(Te −T1) = 0
m2(Te −T2)+ m1(Te −T1) = 0
Te = m2T2 + m1T1
m2 + m1
= 280
5
= 56°C
m2ce(Te −T2)+ m1ce(Te −T1)+ Ccalorimètre(Te −T1) = 0
m2 ce (Te −T2)+ m1 ce (Te −T1)+ µ ce (Te −T1) = 0
µ = m2(T2 −Te)+ m1(T1 −Te)
(Te −T1)
= 100g
ΔUsyst = ΔUlaiton + ΔUeau froide + ΔUcalorimètre = W +Q = 0
m2claiton(Te −T2)+ m1ce(Te −T1)+ C(Te −T1) = 0
claiton = (m1ce + C)(Te −T1)
m2(T2 −Te)
= 363,5 J / K / g
 
4 
3) Un calorimètre de capacité calorifique C = 200 J.K-1 contient une masse m1 = 200g d'eau à 
la température initiale T1 = 80°C. On y place un glaçon de masse m2 = 80g sortant du 
congélateur à la température T2 = – 20°C.  
Données : capacité calorifique massique de la glace : cg = 2,09 J.g-1.K-1 ; chaleur latente 
massique de fusion de la glace : Lf  = 334 J.g-1 ; capacité calorifique massique de l'eau : 
ce = 4,18 J.g-1.K-1. 
a) En supposant que le glaçon fond totalement, déterminer la température finale d'équilibre du 
système. 
 
Premier principe appliqué à l'ensemble {calorimètre + eau + glace}, isolé : 
 
ó 
   
(avec toutes les températures en °C). 
D'où :  
 
 
 
=>   
. 
 
 
b) Avec une température T1 ≤ 29°C le même calcul conduirait à une température d’équilibre 
négative. Que peut-on en conclure sur l’état d’équilibre final ? Expliquer quelle température  
finale on peut obtenir et pourquoi (aucun calcul n’est demandé). 
 
Cela signifie que l’hypothèse que tout le glaçon est fondu n’est plus bonne. 
 
* Soit il reste encore de la glace et de l’eau, et la température finale est celle de fusion de la 
glace :  Tf = 0°C. 
* Soit il ne reste que de la glace et l’eau liquide s’est transformée en glace et Tf  ≤ 0°C. 
 
 
Exercice 3 : Cycles moteurs de Carnot et de Beau de Rochas 
Après une étude graphique des machines dithermes, à l'aide du diagramme de Raveau, on 
compare le rendement des cycles moteurs de Carnot et de Beau de Rochas.  
 
Les parties I et II sont indépendantes 
PARTIE I - Machine ditherme 
Une masse m de gaz, constituée principalement d'air, subit un cycle moteur entre deux sources 
thermiques, l'une est la source froide de température Tf = 290 K, l'autre la source chaude de 
température Tc = 1450 K. 
 
1) Exprimer les bilans d'énergie et d'entropie pour le gaz au cours d'un cycle réel. On introduira 
les quantités algébriques suivantes, relatives à un cycle : W, Qf , Qc , Scréé.  
W est le travail reçu (algébriquement) par le fluide. De même, Qf est la chaleur reçue par le 
fluide de la part de la source froide et Qc est la chaleur reçue par le fluide de la part de la 
source chaude. Enfin, Scréé  désigne l'entropie créée au cours d'un cycle. 
 
* Bilan d'énergie du gaz sur un cycle : 0 = DUcycle = W + Qf + Qc (premier principe). 
ΔUsyst = ΔUeau + ΔUglace + ΔUcalorimètre = 0
m1ce(Tf −T1)+ C(Tf −T1)+ m2cg(0°C −T2)+ m2L f + m2ce(Tf −0°C) = 0
(m1ce + C)(Tf −T1)−m2cgT2 + m2L f + m2ceTf = 0
Tf = (m1ce + C)T1 + m2cgT2 −m2L f
(m1 + m2)ce + C
= 38,5°C
 
5 
* Bilan d’entropie du gaz sur un cycle : 0 = DScycle = Scréé + Séch. 
Or 
 , donc : 
. 
 
 
2) En déduire l'équation de deux droites Qc = f(Qf), puis les représenter sur un même graphe 
(diagramme de Raveau), W et Scréé étant des quantités supposées déterminées dont on précisera 
le signe. Quelle est la position du point de fonctionnement, ainsi que le sens des échanges 
thermiques correspondants (signes de Qc et Qf) ? 
 
* Le premier principe implique : 
 avec W < 0 pour un moteur. 
Il s'agit d'une droite de pente - 1 et d'ordonnée à l'origine Wfourni = – W > 0. 
 
* Le bilan d'entropie implique : 
 avec Scréé ≥ 0 (2nd principe). 
Il s'agit d'une droite de pente 
 plus grande que 1 en valeur absolue car 
 et d'ordonnée 
à l'origine 
 < 0. 
 
 
 
 
 
 
 
 
 
 
 
 
 
Le point de fonctionnement, intersection des deux droites, est donc dans le quadrant : Qc > 0 et 
Qf  < 0 : le gaz reçoit effectivement de la chaleur de la source chaude et fournit effectivement 
de la chaleur à la source froide. 
N.B. : sur le graphique Scréé est noté Sp. 
 
 
3) Montrer que l'expression du rendement h du moteur s'écrit : 
. 
 
Le rendement du moteur est par définition : 
 => 
. 
D'après le bilan entropique : 
 => 
 
 
 
Séch =
δQ
Text
=
cycle

∫
Qf
Tf
+ Qc
Tc
Scréé + Qf
Tf
+ Qc
Tc
=  0
 Qc = − Qf − W 
 
Qc = −Tc
Tf
Qf −TcScréé
 
−Tc
Tf
 Tc > Tf
 −TcScréé
 
η = 1−Tf
Tc
−TfScréé
Qc
 
η = −W
Qc
> 0
η = Qc + Qf
Qc
= 1+ Qf
Qc
Scréé + Qf
Tf
+ Qc
Tc
=  0
Qf
Qc
= −Tf
Tc
−TfScréé
Qc
 
6 
On en déduit bien : 
  car Tf, Qc et Scréé sont positifs. 
 
 
4) Que devient ce rendement lorsque la machine ditherme fonctionne selon un cycle de Carnot ? 
Calculer sa valeur hc. Ce résultat, sensiblement inférieur à 1, doit-il être attribué à une 
imperfection de la machine (frottements divers) ou provient-il d'une limitation fondamentale ? 
Dans ce dernier cas, préciser la nature de cette limitation. 
 
* Pour le cycle de Carnot, qui est un cycle réversible : Scréé = 0, donc : 
. 
* hc < 1 à cause d’une limitation fondamentale : il faut bien transférer de l’énergie à la source 
froide : un moteur ne peut pas fonctionner avec une seule source de chaleur (pas de cycle moteur 
monotherme). De plus, la température de la source froide ne peut pas être égale à O K (zéro 
absolu), seule valeur qui permettrait d’obtenir hc = 1. 
 
 
5) On définit le degré d'irréversibilité du cycle à l'aide du rapport r = h / hc.  
Sachant que r = 0,94 et que le moteur fournit un travail de 15 kJ par cycle, trouver Qc , Qf et 
Scréé.  
 
* h = r hc = 0,94 x hc = 0,94 x 0,80 = 0,752  
* 
. 
* Qf = – Qc – W = – 20 + 15 = – 5 kJ/cycle < 0. 
* 
 => en accord avec le 2nd principe. 
 
 
PARTIE II - Cycle de Beau de Rochas et Otto 
Dans un moteur à explosion, le fluide, de masse m = 2,9 g, assimilé à un gaz parfait 
diatomique, de masse molaire M = 29 g/mol, suit une évolution cyclique réversible ABCD, 
constituée de deux portions isentropiques, AB et CD, séparées par deux portions isochores, 
BC et DA. Le cycle n'est plus ditherme : il y a mise en contact du fluide avec une succession 
de sources chaudes et froides au cours des transformations isochores. 
Les températures et les pressions aux points A et C sont respectivement : TA = 290 K, 
PA = 1 bar, TC = 1450 K, PC = 40 bar. En outre, le taux de compression a = VA / VC est égal à 
8. On rappelle : g = 1,4 et R = 8,31 J.K-1.mol-1. 
 
η = 1−Tf
Tc
−TfScréé
Qc
≤1−Tf
Tc
 
ηc = 1−Tf
Tc
= 1−290
1450 = 1−1
5 = 0,80
 
Qc = −W
η =
15
0,752 = 20 kJ / cycle > 0
Scréé = −Qf
Tf
−Qc
Tc
=  
5
290 −20
1450
⎛
⎝
⎜
⎞
⎠
⎟.103 = 3,44 J / K / cycle > 0
 
7 
6) Quelle équation (loi de Laplace) relie la pression et le volume le long des courbes AB et 
CD ? A l'aide des volumes VB, VC et VD, exprimés en fonction de a  et de VA, exprimer puis 
calculer (en bar) les pressions PB et PD en B et D respectivement. On donne 81,4 =18,4. 
* DA est une isochore => VD = VA  
* BC est une isochore => VB = VC = VA/a 
* AB et CD sont deux isentropiques pour le gaz supposé parfait  
=> la loi de Laplace s'applique : PVg = cste. 
On en déduit : PB VBg  = PA VAg => PB = PA a g  = 18,4 bar  
 
et   PC VCg = PD VDg => PD = PC a –g = 2,2 bar. 
 
 
7) Représenter avec soin le cycle ABCD dans le diagramme de Clapeyron. Justifier le sens de 
description du cycle. A quoi correspond l’aire du cycle ? 
 
Le cycle est décrit dans le sens horaire ABCD car c’est un cycle moteur (W < 0 et 
). 
 
 
 
 
 
 
 
 
 
 
 
 
 
L’aire du cycle, ici positive en raison du sens de parcours, correspond au travail fourni au milieu 
extérieur durant un cycle, soit Wfourni = – W. 
 
 
8) Exprimer puis calculer (en kJ) le travail et la chaleur reçus (algébriquement) par le gaz sur 
chaque portion du cycle. Vérifier l'existence d'une relation simple entre toutes les grandeurs 
calculées.  
On donne : TB = 666 K ; TD = 631 K ; Cv, mol = 20,8 J.mol-1.K-1. 
 
* Sur AB isentropique = adiabatique réversible => QAB = 0  
et WAB = DUAB = n cv (TB - TA) = 0,1 x 20,8 x(666 - 290) = 0,78 kJ > 0. 
 
* De même sur CD isentropique => QCD = 0  
et WCD = DUCD = n cv (TD - TC) = 0,1 x 20,8 x(631 - 1450) = - 1,7 kJ < 0. 
 
 
PdV
cycle

∫
= −W > 0
 
8 
* Sur BC isochore => WBC = 0 et QBC = DUBC = n cv (TC - TB) = 1,63 kJ > 0. 
 
* De même, sur DA isochore : WDA = 0  et QDA = DUDA = n cv (TA - TD) = - 0,71 kJ. 
 
* On trouve bien pour un cycle complet : DUcycle = Wtot + Qtot = 0.  
 
 
9) Quel est le rendement hBO de ce cycle moteur, c'est-à-dire le rapport du travail fourni au 
milieu extérieur sur la chaleur reçue de la part des sources chaudes (portion BC du 
diagramme) ? Comparer hBO au rendement hC d'un cycle moteur ditherme fonctionnant entre les 
températures TA et TC. Commenter. 
 
* W = WAB + WBC + WCD + WDA = - 920 J 
 
* QBC = 1630 J 
 
* 
. 
 
Ceci est en accord avec le fait que bien que les deux isochores soient ici des transformations 
réversibles (tout le cycle est réversible), ce ne sont pas des évolutions isothermes, donc il ne 
s’agit pas d’un moteur ditherme réversible fonctionnant selon un cycle de Carnot. 
 
 
ηBO = 920
1630 = 0,56 < ηc = 0,80
