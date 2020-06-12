## Le template

debut = r'''\documentclass[12pt,a4paper]{article}

% Packages Ecriture
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{fourier}
\usepackage[scaled=0.875]{helvet} 
\renewcommand{\ttdefault}{lmtt} 
\usepackage{eurosym}
\usepackage[french]{babel}
\usepackage[np]{numprint}

% Packages Mise en page
\usepackage{geometry} % Permet la mise en page
\geometry{lmargin=1cm,rmargin=1cm,tmargin=1cm,bmargin=1cm} % Choix format et  des marges
\usepackage{fancyhdr}
\usepackage{framed} % Création d'environnements
\usepackage[framed,thmmarks]{ntheorem} % Gestions des environnements theorem
\usepackage{lastpage}

\usepackage{amsmath,amssymb,makeidx}
\usepackage{enumerate}
\usepackage[normalem]{ulem}
\usepackage{fancybox,graphicx}
\usepackage{tabularx}
\usepackage{ulem}
\usepackage{dcolumn}
\usepackage{textcomp}
\usepackage{diagbox}
\usepackage{tabularx}
\usepackage{lscape}
\usepackage{pstricks,pst-plot,pst-text,pst-tree,pstricks-add,pst-grad,pst-coil,pst-blur}
\usepackage[pstricks]{bclogo} % Logo
%\setlength\paperheight{297mm}
%\setlength\paperwidth{210mm}
%\setlength{\textbfheight}{25cm}

\usepackage{multicol}

\usepackage{hyperref}

\usepackage{pgf,tikz,tkz-tab}
\usepackage{mathrsfs}
\usepackage{pifont}
\usetikzlibrary{arrows}

\usepackage{xcolor}
\usepackage{multicol}
\usepackage{multirow}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\DecimalMathComma	% Définit la virgule comme séparateur entre la partie entière et la partie décimale


\def\Oij{$\left(\textbfrm{O},~\vec{\imath},~\vec{\jmath}\right)$}
\def\Oijk{$\left(\textbfrm{O},~\vec{\imath},~\vec{\jmath},~\vec{k}\right)$}
\def\Ouv{$\left(\textbfrm{O},~\vec{u},~\vec{v}\right)$}

\newcommand{\vect}[1]{\mathchoice%
{\overrightarrow{\displaystyle\mathstrut#1\,\,}}%
{\overrightarrow{\textbfstyle\mathstrut#1\,\,}}%
{\overrightarrow{\scriptstyle\mathstrut#1\,\,}}%
{\overrightarrow{\scriptscriptstyle\mathstrut#1\,\,}}}

\newcommand{\equi}{\Leftrightarrow}
\newcommand{\pg}{\geqslant}
\newcommand{\pp}{\leqslant}
\newcommand{\dt}{\,\mathrm{d}t}
\newcommand{\dx}{\,\mathrm{d}x}

\newcommand{\N}{\mbox{${\mathbb N}$}}
\newcommand{\Z}{\mbox{${\mathbb Z}$}}
\newcommand{\Q}{\mbox{${\mathbb Q}$}}
\newcommand{\R}{\mbox{${\mathbb R}$}}
\newcommand{\C}{\mbox{${\mathbb C}$}}

%Commande pour créer des lignes de pointillés
\newcommand{\Pointilles}[1][3]{%
\multido{}{#1}{\makebox[\linewidth]{\dotfill}\\[\parskip]
}}

\DeclareMathOperator{\e}{e} %Permet d'écrire "droit" le e de l'exponentielle

\let\oldarray=\array
\def\array{\small\oldarray} % Permet d'écrire plus petit dans le tableau

\renewcommand{\arraystretch}{1.2} % Permet de gérer la hauteur des lignes des tableaux

\parindent=0mm % Supprime l'alinéa

\setlength{\fboxsep}{2mm} % Gère l'espacement entre un cadre et son contenu

\renewcommand{\thesection}{\Roman{section}.} % Numérote les sections en chiffre romain
\renewcommand{\thesubsection}{\Alph{subsection}.}

\newcounter{nexo}
\setcounter{nexo}{0}
\newcommand{\exo}{%
\stepcounter{nexo}
{\textbf{\underline{\textsc{Exercice \arabic{nexo}}}}%
\medskip%
}
}

\newcommand{\titre}[1]{\begin{center} {\large \framebox{\textbf{#1}}} \end{center} \medskip}


\providecommand{\tightlist}{%
  \setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
%\providecommand{\tightlist}{\setlength{\itemsep}{25pt}\setlength{\parskip}{10pt}}

\begin{document}

\setlength\parindent{0mm}

\fancyhf{\footnotesize{}}
\fancyhead[L]{\footnotesize{}}
\fancyhead[R]{\footnotesize{}}
\fancyfoot[L]{\small{\textbf{}}}
\fancyfoot[R]{\small{\textbf{}}}

%\cfoot{Page \thepage\ sur \pageref{LastPage}}

\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

\renewcommand{\labelitemi}{$\bullet$}

\pagestyle{fancy}

'''

fin = r'''

\end{document}'''


## Le script

fichier = open("contenu.tex","r",encoding="utf-8")
contenu = fichier.read()
fichier.close()

fichier = open("feuille.tex","w",encoding="utf-8")
fichier.write(debut)
fichier.write(contenu)
fichier.write(fin)
fichier.close()