# Outil pour générer un document tex/pdf avec des courbes (pstricks)

## Fonctionnement

Le fichier `params.json` contient les paramètres du graphique que l'on souhaite tracer. Le programme `makeGraph.py` permet, à partir du fichier json, de générer le *tex* du graphique que l'on souhaite obtenir. 

## Détails

* `makeGraph.py` : programme principal qui génère le tex en mode standalone du graphique. Ce programme utilise le fichier `params.json` (possible de changer).
* `params.json` : contient les paramètres du graphiques (fonctions, axes, etc). C'est le fichier à modifier avant de lancer le programme principal.
* `compilGraph.bat` : permet de lancer la compilation tex vers pdf et supprime les fichiers auxiliaires créés.
* `mongraphique.pdf` : pdf contenant le graphique.
* `mongraphique.tex` : tex du code généré.

## Exemples

Le dossier `exemples` contient quelques résultats obtenus avec ce programme. 