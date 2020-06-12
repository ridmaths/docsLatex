# Quelques rappels sur les commandes 

## Sommaire 

**Mémo syntaxe**

- [Un vecteur](#un-vecteur)
- [Un système](#un-système)
- [Si et seulement si](#ssi)
- [Binomiale](#binomiale)
- [Algorithme](#algorithme)
- [Tailles](#tailles-)
- [Systèmes avancés](#systèmes-avancés)
- [Item alpha](#alphabet-dans-les-numérotations)
- [Item alpha 2](#alphabet-dans-les-numérotations-2)

**Pour les tableaux**

- [Tableau avec des cellules centrées à l'intérieur](#tableau-avec-des-cellules-centrées-à-lintérieur)
- [Tableau de variations](#tableau-avec-des-cellules-centrées-à-lintérieur)
- [Tableau de variations et signes](#tableau-de-variations--signes)
- [Trait plein dans les tableaux](#trait-plein-dans-les-tableaux-tkz-tab)
- [Tableau de signes fonction affine](#tableau-de-signes-fonction-affine)
- [Tableau de signes fonction affine](#tableau-de-signes-fonction-affine)
- [Signe d'un produit](#signe-dun-produit)
- [Signe d'un quotient](#signe-dun-quotient)

# Commandes usuelles

## Un vecteur

les coordonnées du vecteur `$\overrightarrow{AG}$` sont `$\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$`.

## Un système

Une représentation paramétrique de la droite `$(AG)$` est `$\begin{cases} x = t \\ y = t \\ z = t \end{cases}$`.

## SSI

si et seulement si : 	`\Longleftrightarrow`

## Binomiale

binomiale p parmi n : `\binom{n}{p}`

## Algorithme

algorithme :

```latex
\fbox{%
\begin{minipage}{3.7cm}
$N \leftarrow 0$ \\
$U \leftarrow 1$ \\
Tant que $U > 10^{-p}$ \\
\hspace*{0.5cm} $N \leftarrow N+1$\\
\hspace*{0.5cm} $U \leftarrow U-\ln(1+U)$\\
Fin Tant que
\end{minipage}%
}
```

## Tailles

`\tiny \scriptsize \footnotesize \small \normalsize \large \Large \LARGE \huge \Huge`

## Systèmes avancés 

```latex
$\left\{
\begin{array}{r c l}
y & = & 7-5x \\
-6x + 7 &=& 1
\end{array}
\right. 
```

## Vecteur

`\newcommand{\vecteur}[3]{\overrightarrow{#1} \begin{pmatrix} #2 \\ #3 \end{pmatrix}}`

Exemple : Le vecteur `$\vecteur{u}{-2}{5}$`.

# Numérotation

## Alphabet dans les numérotations

`\renewcommand{\theenumi}{\alph{enumi}}`

## Alphabet dans les numérotations 2

Avec le package enumitem ( `\usepackage[shortlabels]{enumitem}` ) :

```latex
\begin{enumerate}[a)]
\item 1
\item 2
\item 3
\end{enumerate}
```

# Les tableaux

## épaisseur ligne tableau

`\renewcommand{\arraystretch}{1.2}`

## Tableau avec des cellules centrées à l'intérieur

```latex
\begin{center}
\newcolumntype{M}[1]{>{\centering\arraybackslash}m{#1}}
\begin{tabular}{|l|M{2cm}|M{2cm}|p{2cm}|}
\cline{2-4}
\multicolumn{1}{c|}{} & \textbf{Machine à laver} & \textbf{Grille-pain} & \textbf{Total} \tabularnewline
\hline
\textbf{Allemagne} & & & \tabularnewline
\hline
\textbf{Chine} & & & \tabularnewline
\hline
\textbf{Total} & & & \tabularnewline
\hline
\end{tabular}
\end{center}
```

## Tableau de variations

```latex
\begin{tikzpicture}
   \tkzTabInit{$x$ /0.8,Variations de $f$ /1.2} {$-\infty$ , $+\infty$}
   \tkzTabVar{-/$-\infty$ , +/$+\infty$}
\end{tikzpicture}

## Tableau de signes

\begin{tikzpicture}
   \tkzTabInit[lgt = 2, espcl = 2.2, deltacl = 0.5]{$x$ /1, Signe de $f'(x)$ /1} {$-\pi$,$-\frac{\pi}{3}$,$\frac{\pi}{3}$,$\pi$}
   \tkzTabLine{,-,z,+,z,-,}
\end{tikzpicture}
```

## Tableau de variations + signes

```latex
\begin{tikzpicture}
   \tkzTabInit{$x$ /1, Signe de $f'(x)$ /1, Variations de $f$ /1.5} {$1$ , $e$, $+\infty$}
   \tkzTabLine{, +, z, -, } 
   \tkzTabVar{-/ $0$, +/$e^{-1}$ , -/ $0$}
\end{tikzpicture}
```

## Trait plein dans les tableaux tkz-tab

`\tikzset{t style/.append style ={solid}}`

## Tableau de signes fonction affine

```latex
\begin{tikzpicture}
   \tkzTabInit[lgt = 3, espcl = 3.5]{$x$ / 0.8 , Signe de $-6x+1$ / 1}{$-\infty$, $\frac{1}{6}$, $+\infty$}
   \tkzTabLine{, + , z, - , }
\end{tikzpicture}
```

Mode help pour tkz-tab (voir les noeuds) + exemple d'utilisation :

```latex
\begin{tikzpicture}
   \tkzTabInit[lgt = 3, espcl = 3.5,help]{$x$ / 0.8 , Signe de $-6x+1$ / 1}{$-\infty$, $\frac{1}{6}$, $+\infty$}
   \tkzTabLine{, + , z, - , }
\end{tikzpicture}

\begin{tikzpicture}
\draw[fill=red!20,opacity=.3] (N20) rectangle (N74);
   \tkzTabInit[lgt = 3, espcl = 3.5]{$x$ / 0.8 , Signe de $-6x+1$ / 1}{$-\infty$, $\frac{1}{6}$, $+\infty$}
   \tkzTabLine{, + , z, - , }
\end{tikzpicture}
```

## Signe d'un produit

```latex
\begin{center}
\tkzTabSetup[tstyle = solid]
\begin{tikzpicture}
\tkzTabInit[lgt=3.2,espcl=2]{$x$ / 1 , \footnotesize{Signe de $2x-1$} / 1, \footnotesize{Signe de $6x+24$} / 1, \scriptsize{Signe de \\ $(2x-1)(6x+24)$} / 1}{$-\infty$, $-4$ , $\frac{1}{2}$ ,$+\infty$}
\tkzTabLine{ , - , t , - , z , +,}
\tkzTabLine{ , - , z , + , t , +,}
\tkzTabLine{ , + , z , - , z , +}
\end{tikzpicture}
\end{center}
```

## Signe d'un quotient

```latex
\begin{center}
\tkzTabSetup[tstyle = solid]
\tikzset{double style/.style = {double,very thick,double distance=2pt}}
\begin{tikzpicture}
\tkzTabInit[lgt=3.2,espcl=2]{$x$ / 1 , \footnotesize{Signe de $2x-4$} / 1, \footnotesize{Signe de $6x+30$} / 1, \scriptsize{Signe de $\dfrac{2x-4}{6x+30}$} / 1}{$-\infty$, $-5$, $2$,$+\infty$}
\tkzTabLine{ , - , t , - , z , + ,}
\tkzTabLine{ , - , z , + , t , +	,}
\tkzTabLine{ , + , d , - , z , + }
\end{tikzpicture}
\end{center}
```