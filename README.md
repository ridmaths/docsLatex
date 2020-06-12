# Création de documents avec LaTex (et autres...)

Quelques documents ou programmes pour la création de documents pour les cours de Mathématiques. 

## cheat-sheet

Anti-sèche pour les commandes usuelles !

## courbeTool

Outil pour générer un graphique dont les paramètres sont entrés dans un fichier JSON.

## templates_usuels

Les templates utilisés pour les cours / exercices.

* cours_seconde
* cours_terminale
* cours_beamer
* feuille_exos
* interro
* controle

## md_vers_pdf

**Pour la v1**

Écriture d'une feuille d'exercices *test.md* puis compilation avec `pandoc` pour obtenir le pdf. 

Les paramètres (geometry, fontsize) sont placés dans le fichier .md (au début du fichier).

On compile ensuite en lançant dans `cmd` le fichier `commande.bat`.

Cela génère un *pdf* et un *tex*.

Les paramètres (fontfamily, geometry) sont dans le fichier source.

**Pour la v2**

Le contenu est à écrire dans le fichier `feuille.md`. Puis on exécute le programme `comp_md2pdf.bat` pour compiler et obtenir le pdf. 

Le progamme `comp_md2pdf.bat` :
* exécute pandoc pour transformer le fichier `feuille.md` en un fichier `contenu.tex` (le tex sans le préanmbule.) 
* exécute ensuite le programme `makeLatex.py` qui contient le préanmbule utilisé pour le tex et génère le fichier `feuille.tex`
* execute latex en mode _quiet_ pour compiler ce tex et obtenir le pdf
* supprime les fichiers inutiles. 