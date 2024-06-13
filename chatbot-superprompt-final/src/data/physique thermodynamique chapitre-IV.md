CHAPITRE IV
NOTION D’ENTROPIE
2nd PRINCIPE DE LA THERMODYNAMIQUE
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
1
2023-2024 – Stéphanie Moreau
SOMMAIRE
I – Irréversibilité et entropie
II – Construction de l’entropie d’un gaz parfait
III  – L’entropie du point de vue microscopique
IV – Identités thermodynamiques
V – Expressions de la variation de l’entropie d’un système
VI – Second principe de la thermodynamique
VII – Réversibilité et irréversibilité
VIII – EXERCICES
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
2
2023-2024 – Stéphanie Moreau
• Premier principe = principe de conservation de l’énergie, qui ne prédit 
pas dans quel sens s’effectue spontanément une transformation et qui
n’interdit pas la transformation inverse.
Þ il  manque un principe d’évolution => principe d’extremum
Þ trouver une grandeur du système qui ne peut varier que dans un 
seul sens et qui est donc extrémale à l’équilibre.
• Exemple de principe d’extremum : en mécanique, pour un système 
fermé, c’est l’énergie potentielle qui joue ce rôle. Elle ne peut que 
décroître et est minimale à l’équilibre.
I – IRREVERSIBILITÉ ET ENTROPIE
I-a) Irréversibilité macroscopique
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
3
I – IRREVERSIBILITÉ ET ENTROPIE
I-b) Rappels sur les positions d’équilibre en méca
• Etat d’équilibre stable ó minimum d’énergie potentielle Ep
• Etat d’équilibre métastable ó minimum secondaire d’Ep
• Etat d’équilibre contraint ó ce n’est pas un minimum de la fonction 
Ep mais correspond à la valeur minimale de Ep, étant donné les 
contraintes imposées au système.
• Etat d’équilibre instable ó maximum d’Ep
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
4
I – IRREVERSIBILITÉ ET ENTROPIE
I-c) Principe d’évolution en thermodynamique
Þ rendre compte de l’évolution à sens unique des transformations 
irréversibles + notions de réversibilité et d’irréversibilité d’une transformat°
Þ On cherche une fonction d’état du système, notée S et appelée entropie :
üextensive (par analogie avec l’énergie interne)
üqui augmente pour toute transformation spontanée d’un système 
(thermiquement) isolé
üqui est constante pour un système fermé à l’équilibre.
Þ s’assurer de son unicité (à une constante additive près, comme pour 
toutes les autres fonctions d’état de type énergétique : U, H, etc).
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
5
II – CONSTRUCTION DE L’ENTROPIE D’UN GP
II-a) Transformation réversible d’un GP
• Transf. élémentaire réversible d’un GP soumis uniquement aux forces de pression :  
dU = dWrév + dQrév = – P dV + dQrév = n cVmol dT
• dQrév = n cVmol dT + P dV n’est pas une différentielle totale exacte (dépend du
chemin suivi, donné par la relation P = f(V) durant la transformation élémentaire).
• dQrév / T = n (cVmol dT/T + R dV/V) = dS est la différentielle totale exacte de la 
fonction entropie, notée S.
ü Cette fonction d’état est bien extensive.
• Transformation d’un système fermé menant d’un E.I. (P1, T1, V1) à un E.F. (P2, T2, V2) :
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
6
S(T,V,n) = n R ln V
V0
+ cv
mol ln T
T0
+ S(T0,V0,n)
n
⎛
⎝
⎜
⎞
⎠
⎟
ΔS = n R ln V2
V
1
+ cv
mol ln T2
T
1
⎛
⎝
⎜
⎞
⎠
⎟
II – CONSTRUCTION DE L’ENTROPIE D’UN GP
II-b) Variation d’entropie d’un GP pour une détente 
adiabatique réversible
• E.I.  (P1, T1, V1) –> E.F (P2 =  P0, T2, V2). On pose x = P0/P1. Parois adiabatiques. Milieu extérieur de pression 
constante P0 mais l’opérateur retient le piston de façon à obtenir une transformation lente (donc quasi-
statique). 
=> on peut appliquer les lois de Laplace : 
=>
=> La transformation est donc isentropique (S = cste).
• De plus, à tout moment de la transformation, dS = 0 or dQ = 0 (adiabatique), donc dS = dQrév/T est vérifié :
Þ la transformation est également réversible.
Une transformation adiabatique quasi-statique d’un gaz parfait est isentropique (adiabatique réversible) : 
S = cste durant la transformation (ou DS = 0)
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
7
P
1V1
γ = P
0V2
γ =>V2 = V1x
−1
γ
et
T2 = T
1x
γ −1
γ
ΔS = n cV
mol ln
T
2
T
1
+ Rln
V
2
V1
⎛
⎝
⎜
⎞
⎠
⎟= n cV
mol ln x
γ −1
γ + Rln x
−1
γ
⎛
⎝
⎜
⎞
⎠
⎟= n
R
γ −1
γ −1
γ
ln x −1
γ Rln x
⎛
⎝
⎜
⎞
⎠
⎟= 0
II – CONSTRUCTION DE L’ENTROPIE D’UN GP
II-c) Variation d’entropie du GP pour une détente 
adiabatique irréversible
•
E.I.  (P1, T1, V1) –> E.F (P2 =  P0, T2, V2). On pose x = P0/P1. Parois adiabatiques. Milieu extérieur de pression constante P0 (transform°
monobare). Le piston est relâché d’un coup => transformation irréversible. Le système évolue vers un état d’équilibre final, 
différent de celui obtenu dans le cas précédent.
•
Bilan énergétique : 1er principe de la thermo =>
=> 
=> 
•
Bilan entropique :
Etude de sa variation en fct de x : 
Cette dérivée s’annule en x = 1, est négative pour 0 < x < 1 et positive pour x > 1.
DS admet donc un minimum, de valeur DS = 0, pour x = 1, cas limite de la « transformation réversible » (P1 = P0) : le système est déjà à 
l’équilibre avec le milieu extérieur dans l’état initial et il n’y a pas de transformation.
DS > 0 pour toute transformation adiabatique irréversible d’un GP.
•
La fonction S ainsi définie vérifie bien les 3 critères choisis : extensive, maximale à l’équilibre et constante à l’équilibre.
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
8
ΔU = ncV
mol(T2 −T
1) = W + Q = −P
0(V2 −V1) + 0
n R
γ −1(T2 −T
1) = −nRT2 + x nRT
1 <=>
1
γ −1(T2 −T
1) = −T2 + xT
1
T2 = T
1
(γ −1)x +1
γ
et
V2 = V1
(γ −1)x +1
γ x
ΔS = n cV
mol ln
T
2
T
1
+ Rln
V
2
V1
⎛
⎝
⎜
⎞
⎠
⎟= n
R
γ −1ln (γ −1)x +1
γ
+ Rln (γ −1)x +1
γ x
⎛
⎝
⎜
⎞
⎠
⎟= nR
γ
γ −1ln (γ −1)x +1
γ
−ln x
⎛
⎝
⎜
⎞
⎠
⎟
dΔS
dx = nR
γ
γ −1
(γ −1)
(γ −1)x +1 −1
x
⎛
⎝
⎜
⎞
⎠
⎟= nR
γ
(γ −1)x +1 −1
x
⎛
⎝
⎜
⎞
⎠
⎟= nR γ x −(γ −1)x −1
((γ −1)x +1)x
⎛
⎝
⎜
⎞
⎠
⎟= nR
x −1
((γ −1)x +1)x
II – CONSTRUCTION DE L’ENTROPIE D’UN GP
II-d) Généralisation aux autres systèmes
• Pour un système fermé évoluant au cours d’une transformation élémentaire 
réversible, la variation élémentaire de son entropie sera définie par :
(on a alors : Text = T)
• Pour une transformation élémentaire quelconque, l’entropie peut évoluer :
- par suite d’échanges thermiques avec le milieu extérieur de température Text : 
dSéchangé = dQ/Text
- par création à l’intérieur du système, en raison de phénomènes irréversibles : 
dScréé > 0
• Pour une transformation réversible d'un système fermé (n = cste) : 
dU = dWrév + dQrév = – P dV + T dS
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
9
dS = dSrév = δQrév
T
III – L’ENTROPIE DU POINT DE VUE MICROSCOPIQUE
III-a) Introduction
• Le premier principe de la thermodynamique limite les micro-états accessibles à un 
système thermodynamique isolé en évolution, puisque l’énergie interne d’un système 
isolé reste constante.
• Néanmoins, parmi tous les micro-états possibles correspondant à une même valeur de 
l’énergie interne, certains sont similaires (particules indiscernables) et donnent un seul 
macro-état. Ainsi certains macro-états sont fréquemment atteints tandis que d’autres ne 
le sont pratiquement jamais, à énergie interne fixe.
• Pour un macro-état donné d’un système de N particules, il existe W micro-états possibles.
• On supposera que pour un système isolé, tous les micro-états accessibles sont 
équiprobables.
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
10
III – L’ENTROPIE DU POINT DE VUE MICROSCOPIQUE
III-b) Système à 2 niveaux (1)
• Cas de la détente de Joule-Gay Lussac : 
N particules dans une enceinte rigide et calorifugée, divisée en 2 compartiments de 
même volume par une paroi médiane.
Initialement, les N particules se trouvent dans le compartiment (1). 
A t = 0, on pratique dans la paroi séparatrice un orifice, permettant aux particules 
de circuler librement dans les deux compartiments.
• Un macro-état sera donné par le nombre total N1 de particules dans le 
compartiment (1), N étant fixé (système isolé, donc fermé), tandis qu’un micro-
état sera donné par la position (1) ou (2) de chacune des N particules.
• Exercice : déterminer W(N1) pour N = 2 puis N = 4. Représenter P(N1) la probabilité 
de chaque macro-état, dans chacun de ces 2 cas.
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
11
III – L’ENTROPIE DU POINT DE VUE MICROSCOPIQUE
III-b) Système à 2 niveaux (2)
• Cas N quelconque : W(N) = W(0) = 1  et
• Si N1 = N/2,
pour N très grand en utilisant la
formule de Stirling : 
C’est ce macro-état qui domine la distribution des W(N1).
• P(N1) = W(N1)/Wtot où                             est le nombre total de micro-
états possibles.
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
12
Ω(N1) = CN1
N =
N!
N1!(N −N1)!
Ω(N
2 ) =
N!
N
2 !
⎛
⎝
⎜
⎞
⎠
⎟
2 ! 2N
lnN!= NlnN −N
Ωtot =
Ω(Ni)
i=0
N
∑
III – L’ENTROPIE DU POINT DE VUE MICROSCOPIQUE
III-b) Système à 2 niveaux (3)
• Quand le système évolue, au niveau microscopique, on a 2N fois plus 
de chances de se retrouver dans un micro-état correspondant au 
macro-état N1 = N/2 que dans le seul micro-état correspondant à 
N1 = N. 
• L’évolution spontanée du système se fait naturellement vers le macro-
état le plus probable, c’est-à-dire celui auquel correspond le plus 
grand nb de micro-états, ou encore celui pour lequel W(N1) est 
maximum. 
Dans le cas de la détente de Joule-Gay Lussac, il s’agit de N1 = N/2.
• Ce résultat est généralisable à tout système à 2 niveaux.
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
13
III – L’ENTROPIE DU POINT DE VUE MICROSCOPIQUE
III-c) Mise en commun de 2 sous-systèmes à 2 nivx
• Cas de la détente de Joule-Gay Lussac, avec deux gaz A et B mélangés. 
Soit : NA = 2 et NB = 4. 
• Exemple : 
le nombre de micro-états de ce système correspondant au macro-état 
(N1A = 1 ; N1B = 3) est : 2 x 4 = 8. 
• De manière générale, le nombre total de micro-états accessibles est :
W = WA x WB
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
14
III – L’ENTROPIE DU POINT DE VUE MICROSCOPIQUE
III-d) Relation de Boltzmann
• W augmente lors de l’évolution spontanée d’un système isolé et est maximum à 
l’état d’équilibre. Or W n’est pas une grandeur additive mais multiplicative. 
• ln W présente de plus l’intérêt d’être une grandeur additive tout en étant aussi 
maximale à l’équilibre :
• Pour obtenir une grandeur dimensionnée thermodynamiquement, on pose : 
où kB = 1,38.10-23 J/K est la constante de Boltzmann. 
C’est la relation de Boltzmann. 
S s’exprime en J/K (tout comme la fonction entropie définie dans le II).
• A T = 0 K, l’entropie est nulle : S = 0, car W = 1 (pas d’agitation thermique) 
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
15
lnΩ = lnΩA + lnΩB
S = kB lnΩ
IV – IDENTITÉS THERMODYNAMIQUES
IV-a) Définition de la température thermo
• Cas des 2 solides en contact thermique, l’ensemble constituant un système isolé. Dans 
l’état initial, ils n’ont pas la même température mais à l’état d’équilibre final, ils ont la 
même température.
• L’énergie interne de l’ensemble est : U = U1 + U2 = cste (système isolé) => U = U1éq + U2éq.
• Le nombre de micro-états accessibles est :
soit : 
• A l’équilibre, U1 = U1éq, et ln W(U1) est maximale, donc aussi :
=> à l’équilibre :
• La quantité      est donc uniforme pour un système à l’équilibre thermodynamique, tout 
comme la pression P et la température T. Cette grandeur est homogène à l’inverse d’une 
température.
On pose donc :     
ou
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
16
Ω(U1) = Ω1(U1)Ω2(U2) = Ω1(U1)Ω2(U −U1)
lnΩ(U1) = lnΩ1(U1) + lnΩ2(U −U1)
S = kB lnΩ(U1) = S1 +S2
∂S
∂U1
= ∂S1
∂U1
+ ∂S2
∂U1
= ∂S1
∂U1
−∂S2
∂U2
= 0 => ∂S1
∂U1
= ∂S2
∂U2
∂S
∂U
1
T =
∂S
∂U
⎛
⎝
⎜
⎞
⎠
⎟
V,N
T =
∂U
∂S
⎛
⎝
⎜
⎞
⎠
⎟
V,N
IV – IDENTITÉS THERMODYNAMIQUES
IV-b) Différentielle totale de U(S,V,N)
• D’après le premier principe, pour un système fermé (N constant) :  
dU = dQ + dW = dQrév + dWrév = T dS – P dV
=> Pression thermo :
et  température thermo :
• Différentielle totale exacte de l’énergie interne U(S,V,N) : dU = T dS – P dV + µ dN où : 
Ø S = entropie du système (grandeur extensive)
Ø µ = potentiel chimique du système (grandeur intensive), avec : 
• Pour un système fermé ne subissant ni réaction chimique, ni réaction nucléaire, ni 
changement d’état : dN = 0
=>
dU = T dS – P dV
(différentielle partielle)
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
17
P = −∂U
∂V
⎛
⎝
⎜
⎞
⎠
⎟
S,N
µ =
∂U
∂N
⎛
⎝
⎜
⎞
⎠
⎟
S,V
T =
∂U
∂S
⎛
⎝
⎜
⎞
⎠
⎟
V,N
IV – IDENTITÉS THERMODYNAMIQUES
IV-c) Différentielle totale de S(U,V,N)
• De l’identité thermodynamique pour dU, on tire :
• Pression thermodynamique :
• Température thermodynamique  :
• Potentiel chimique :  
La connaissance de la fonction S(U,V,N) permet de déterminer la température T,
la pression P et le potentiel chimique µ en fonction des variables U, V et N : ce
sont les 3 équations d’état d’un corps pur se trouvant sous une seule phase.
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
18
dS = 1
T dU + P
T dV −µ
T dN
P = T
∂S
∂V
⎛
⎝
⎜
⎞
⎠
⎟
U,N
T =
1
∂S
∂U
⎛
⎝
⎜
⎞
⎠
⎟
V ,N
µ = −T
∂S
∂N
⎛
⎝
⎜
⎞
⎠
⎟
U,V
IV – IDENTITÉS THERMODYNAMIQUES
IV-d) Différentielle totale de H(S,P,N)
• Fonction enthalpie H(S,P,N) : 
H = U + PV
• Différentielle totale de la fonction enthalpie H :
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
19
dH = TdS +VdP + µdN
IV – IDENTITÉS THERMODYNAMIQUES
IV-e) Fonctions F(T,V,N) et G(T,P,N)
• Fonction énergie libre F(T,V,N) : 
F = U – TS 
• Différentielle totale de la fonction énergie libre :
• Fonction enthalpie libre G(T,P,N) : G = H – TS = F + PV = U –TS + PV
• Différentielle totale de la fonction énergie libre :
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
20
dF = −SdT −PdV + µdN
dG = −SdT +VdP + µdN
V – EXPRESSIONS DE LA VARIATION DE S
V-a) Cas d’une phase condensée 
• phase condensée = solides, liquides => N = cste et V varie peu donc :
• Formule générale pour les phases condensées : 
• Si C = m c = cste (indép. de T) alors : 
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
21
dS = 1
T dU + P
T dV −µ
T dN ! 1
T dU = C(T) dT
T = m c(T) dT
T
ΔS =
C(T ) dT
T
Ti
Tf
∫
ΔS =
mc dT
T
Ti
Tf
∫
= mcln
T
f
Ti
V – EXPRESSIONS DE LA VARIATION DE S
V-b) Cas d’un gaz parfait dans une enceinte fermée
• Système fermé, GP  =>
• Par intégration, on a :
• En utilisant PV = nRT et sa différentielle logarithmique, on obtient : 
=>
=>
• Exercice : retrouver les 3 lois de Laplace (DS = 0 pour adiabatique réversible)
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
22
dS = 1
T dU + P
T dV −µ
T dN = CV
dT
T + nR dV
V
ΔS = CV ln
Tf
Ti
+ nRln
V f
Vi
dS = CP
dT
T −nR dP
P
ΔS = CP ln
Tf
Ti
−nRln
Pf
P
i
ΔS = CV ln
Pf
P
i
+ CP ln
V f
Vi
dS = CV
dP
P + CP
dV
V
V – EXPRESSIONS DE LA VARIATION DE S
V-c) Exemples d’applications
• Détente de Joule-Gay Lussac pour un gaz parfait :
E.I.  (P1, T1, V1= V) –> E.F (P2 = P1/2, T2 = T1, V2 = 2V)
• Détente de Joule-Thomson (ou Joule-Kelvin) pour un gaz parfait :
E.I.  (P1, T1, V1) –> E.F (P2 < P1, T2 = T1, V2)
• Ces 2 transformations sont adiabatiques et irréversibles => DS > 0 vérifié. 
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
23
ΔS = CV ln T2
T
1
+ nRlnV2
V1
= nRln2 > 0
ΔS = CP ln T2
T
1
−nRln P
2
P
1
= −nRln P
2
P
1
> 0
VI – 2ND PRINCIPE DE LA THERMODYNAMIQUE
VI-a) Enoncé
• 2nd Principe de la thermodynamique
Pour tout système thermodynamique fermé, il existe une fonction d’état, appelée entropie
et notée S :
Ø extensive
Ø non conservative
Ø qui augmente pour toute transformation ADIABATIQUE d’un système fermé : DS ≥ 0
=> L’état d’équilibre thermodynamique d’un système isolé (thermiquement) est régi par 
le principe d’entropie maximale :
L'ENTROPIE D'UN SYSTÈME ISOLÉ EST MAXIMALE À L'EQUILIBRE.
• 3ème principe de la thermodynamique : L'ENTROPIE EST NULLE À T = 0 K (zéro absolu).
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
24
VI – 2ND PRINCIPE DE LA THERMODYNAMIQUE
VI-b) Ecriture du bilan entropique
• Lors d’une transformation quelconque d’un système fermé, on peut 
décomposer la variation d’entropie en 2 termes :
DS     
= 
Séchangé
+
Scréé
où    
et   Scréé > 0 si irréversible ou Scréé = 0 si réversible
• Pour une transformation élémentaire (quasi-statique) :
dS = dSéchangé
+ dScréé
où    
et    dScréé > 0 si irréversible ou dScréé = 0 si réversible
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
25
δSéchangé = δQ
Text
Séchangé =
δQ
Text
E.I
E.F
∫
VI – 2ND PRINCIPE DE LA THERMODYNAMIQUE
VI-c) Exemples
• Transformation adiabatique :
Q = 0 => Séchangé= 0 
DS  =  Scréé > 0 si adiabatique irréversible 
ou DS = Scréé = 0 si adiabatique réversible (= isentropique => S =cste) 
• Transformation monotherme :
Le système (fermé) échange de l’énergie avec un unique thermostat de température cste = 
Text.
q Pour une transform° monotherme quelconque :
q Pour une transform° monotherme réversible (isotherme) :
(Text = T = cste = Ti = Tf)
• Transformation cyclique : DScycle = SA - SA = 0 (fct d’état => variat° indép. du chemin suivi)
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
26
Séchangé =
δQ
Text
∫
= Q
Text
ΔS = Séchangé = Q
Text
= Q
T
VII – REVERSIBILITÉ ET IRREVERSIBILITÉ
VII-a) Transformation monotherme d’un GP (1)
• Cas de la transformation réversible => Pext = P et Text = T = T0 (isotherme)
Gaz parfait enfermé dans une enceinte fermée par un piston mobile. Milieu extérieur = 
thermostat de température T0 et de pression P0 constantes. On ajoute des masselottes sur 
le piston, de manière à augmenter très lentement la pression extérieure appliquée au 
piston. La pression finale est Pf = P0 + mg/S = (1 + x)P0 avec x = mg/SP0 ≥ 0.
E.I (P0, T0,Vi,n) –> E.F (Pf =(1 + x)P0, T0,Vf,n) 
q Bilan énergétique : DU = Wrév + Qrév = 0 (Tf = Ti = cste)
q Bilan entropique : 
N.B. : on retrouverait le même résultat avec la formule 
puisque la variation de S est indépendante du chemin suivi.
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
27
Qrév = −Wrév = −
−PdV
EI
EF
∫
= nRT0
dV
V
Vi
V f
∫
= nRT0 ln
V f
Vi
= −nRT0 ln
Pf
P
i
= −nRT0 ln(1+ x)
ΔS = CP ln
Tf
Ti
−nRln
Pf
P
i
= −nRln
Pf
P
i
ΔS = Séchangé + Scréé = Séchangé + 0 = Qrév
T0
= −nRln(1+ x)
VII – REVERSIBILITÉ ET IRREVERSIBILITÉ
VII-a) Transformation monotherme d’un GP (2)
• Cas de la transformation irréversible => Pext = cste ≠ P et Text = T0 (monotherme) ≠ T
Gaz parfait enfermé dans une enceinte fermée par un piston mobile. Milieu extérieur = 
thermostat de température T0 et de pression P0 constantes. On ajoute une masse m sur le 
piston, de manière à augmenter la pression extérieure appliquée au piston. La pression 
extérieure appliquée durant toute la transformation est  Pext = Pf = P0 + mg/S = (1 + x)P0
E.I (P0, T0,Vi,n) –> E.F (Pf =(1 + x)P0, T0,Vf,n) 
q Bilan énergétique : DU = Wirrév + Qirrév = 0 (Tf = Ti = cste)
q Bilan entropique :  
La variation de S est indépendante du chemin suivi :
On en déduit :
Cette grandeur est nulle pour x = 0 uniquement et > 0 pour x > 0.
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
28
Qirrév = −Wirrév = −
−P
ext dV
EI
EF
∫
= (1+ x)P
0
dV
Vi
V f
∫
= (1+ x)P
0(V f −Vi) = (1+ x)P
0nRT0(
1
(1+ x)P
0
−1
P
0
) = −xnRT0
ΔS = Séchangé + Scréé = −nRln(1+ x)
Séchangé = Qirrév
T0
= −xnR
ΔS −Séchangé = Scréé = −nRln(1+ x) + xnR = nR(x −ln(1+ x)) > 0
VII – REVERSIBILITÉ ET IRREVERSIBILITÉ
VII-b) Contact thermique entre deux solides
• Soit un ensemble de 2 solides isolés thermiquement du milieu extérieur. 
Initialement ils ont des températures différentes, T1 et T2. A l’équilibre ils 
ont la même température Téq.
qBilan énergétique : DU = Wirrév + Qirrév = 0 = DU1 + DU2
=> m1c1(Téq-T1) + m2c2(Téq-T2) = 0 => 
q Bilan entropique : DS = DS1 + DS2
La variation de S est indépendante du chemin suivi => 
• Cas particulier : m1c1 = m2c2 => Téq = (T1 + T2)/2
=> 
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
29
Téq = m
1c1T
1 + m2c2T2
m
1c1 + m2c2
ΔS = m
1c1ln
Téq
T
1
+ m2c2 ln
Téq
T2
ΔS = mcln
Téq
2
T
1T2
= mcln(1+ (T
1 −T2)2
4T
1T2
) > 0
VII – REVERSIBILITÉ ET IRREVERSIBILITÉ
VII-c) Causes d’irréversibilité
• Phénomènes diffusifs : dûs au gradient (inhomogénéité) d'une 
grandeur intensive, comme la température (diffusion thermique), la 
concentration (diffusion de particules).
• Frottements (solides, fluides), fluides visqueux, phénomènes non 
linéaires, etc.
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
30
VIII – EXERCICES
Exercice 1 : Étude de qq phénomènes irréversibles (1)
Les 3 parties sont indépendantes.
1. Préliminaire. Définir ce qu'est une transformation réversible. Donner deux exemples de phénomènes à l'origine de l'irréversibilité 
d'une transformation.
2. Illustration du principe d'entropie maximale
Deux cylindres de même section S, contenant deux gaz (supposés parfaits) 
qui peuvent être différents, sont fermés par deux pistons étanches. 
Ces deux pistons sont solidaires en ce sens que leurs axes restent verticaux
et sont attachés aux bras d'un levier dont le point fixe est deux fois plus près 
du premier cylindre que du second, comme indiqué sur la figure ci-contre. 
Les deux cylindres reposent sur une table qui conduit la chaleur (une table 
métallique) et a pour seul effet de permettre les échanges de chaleur entre 
les deux systèmes, c'est-à-dire entre les gaz contenus dans les deux cylindres. 
Le système complet formé par ces deux cylindres est isolé et n'est pas soumis à une pression extérieure.
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
31
VIII – EXERCICES
Exercice 1 : Étude de qq phénomènes irréversibles (2)
2.1) Déterminer la relation imposée par la présence du levier sur les variations de 
volumes dV1 et dV2 des deux cylindres.
2.2) Écrire l'expression de la variation infinitésimale d'entropie dS du système 
complet formé par les deux cylindres en fonction des températures T1 et T2 des gaz 
contenus dans les deux cylindres, des pressions P1 et P2 qui règnent dans les deux 
cylindres et des seules variations dV1 (variation de volume du gaz contenu dans le 
cylindre 1) et dU1 (variation de l'énergie interne du gaz contenu dans le cylindre 1). 
Les capacités thermiques des cylindres et de la table sont négligeables.
2.3) Que vaut dS lorsque le système complet est à l'équilibre ? En déduire la 
relation entre les températures T1 et T2, puis celle entre les pressions P1 et P2 des 
gaz dans les cylindres 1 et 2 lorsque l'équilibre est atteint. 
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
32
VIII – EXERCICES
Exercice 1 : Étude de qq phénomènes irréversibles (3)
3. Échauflement d'un solide 
3.1) On considère un solide de masse m = 1,0 kg, de capacité thermique massique c = 10 
J/kg/K se trouvant initialement à la température T1 = 273 K, placé dans une grande 
quantité d'eau (constituant un thermostat) à la température T2 = 373 K. 
Lorsque l'équilibre thermodynamique est atteint :
• quelle est la température du solide ? 
• quelle est la température du thermostat ?
3.2) Déterminer la variation d'entropie du solide lors de ce processus, en fonction de m, c, 
T1 et T2. Faire l’application numérique.
3.3) Déterminer la variation d'entropie de l’eau (« thermostat ou réservoir/source de 
chaleur ici) lors de ce processus, en fonction de m, c, T1 et T2. Faire l’application numérique.
3.4) En déduire la variation de l'entropie de l'univers constitué par l'ensemble {solide + 
thermostat}, lors de ce processus puis faites l'application numérique. Commentez votre 
résultat.
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
33
VIII – EXERCICES
Exercice 1 : Étude de qq phénomènes irréversibles (4)
3.5) On découpe le processus précédent en une infinité de petits processus au cours 
desquels on élève la température du solide de T à T + DT (avec DT << T) par contact 
avec une infinité de thermostats de températures infiniment proches les unes des 
autres. Montrer que, pour une étape intermédiaire, on peut écrire :
En développant ce résultat au deuxième ordre en        , montrer que 
est proportionnelle à         . 
En déduire que ce processus peut être rendu réversible à la limite où la variation de 
température entre deux thermostats successifs tend vers zéro.
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
34
ΔSunivers = mc ln 1+ ΔT
T
⎛
⎝
⎜
⎞
⎠
⎟−
ΔT
T + ΔT
⎛
⎝
⎜
⎞
⎠
⎟
ΔT
T
ΔSunivers
ΔT
T
⎛
⎝
⎜
⎞
⎠
⎟
2
VIII – EXERCICES
Exercice 2
On considère une enceinte cylindrique fermée en haut par un piston horizontal de 
masse négligeable et de section s = 100 cm2. On suppose que les frottements du 
piston sont négligeables lors de ses déplacements.
On renferme une masse m = 7,25 g d’air (assimilé à un gaz parfait de masse molaire 
M = 29 g/mol) dans l’enceinte.
Dans l’état initial :
• T1 = Text = 300 K (température ambiante supposée constante) 
• P1 = Pext = 1 bar (pression atmosphérique ambiante supposée constante).
1) Calculer le volume V1 et la hauteur h1 du piston par rapport au fond du cylindre 
dans l’état d’équilibre initial.
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
35
VIII – EXERCICES
Exercice 2 : A) Toutes les parois sont diathermales.
On pose sur le piston une masse de 100 kg et on attend qu’un nouvel état d’équilibre 
(P2, T2, V2) s’établisse.
A.1) Quelle est la nature de la transformation ?
A.2) Déterminer le taux de compression t = P2/P1, T2, V2 et h2, la hauteur finale du piston.
A.3) Calculer W12 le travail reçu par le système au cours de la transformation.
A.4) Calculer la variation d’entropie de l’air, du milieu extérieur et de l’univers.
On repart de l’état initial et on comprime réversiblement l’air jusqu’à la pression P2.
A.5) Comment pourrait-on réaliser une telle transformation ? Quelle est la nature de cette 
transformation ?
A.6) Calculer à nouveau T’2, V’2, h’2, la hauteur finale du piston, et W’12 le travail reçu par le 
système au cours de la transformation.
A.7) Calculer la variation d’entropie de l’air, du milieu extérieur et de l’univers.
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
36
VIII – EXERCICES
Exercice 2 : B) Toutes les parois sont adiabatiques.
On pose sur le piston une masse de 100 kg et on attend qu’un nouvel état d’équilibre 
(P3, T3, V3) s’établisse.
B.1) Quelle est la nature de la transformation ?
B.2) Déterminer le taux de compression t’ = P3/P1, T3, V3 et h3, la hauteur finale du piston.
B.3) Calculer W13 le travail reçu par le système au cours de la transformation.
B.4) Calculer la variation d’entropie de l’air, du milieu extérieur et de l’univers.
On repart de l’état initial et on comprime réversiblement l’air jusqu’à la pression P3.
B.5) Comment pourrait-on réaliser une telle transformation ? Quelle est la nature de cette 
transformation ?
B.6) Calculer à nouveau T’3, V’3, h’3, la hauteur finale du piston, et W’13 le travail reçu par le 
système au cours de la transformation.
B.7) Calculer la variation d’entropie de l’air, du milieu extérieur et de l’univers.
2023-2024 – Stéphanie Moreau
Chapitre IV : Notion d'entropie  - 2nd principe de la thermo
37
