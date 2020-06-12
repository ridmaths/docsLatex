@echo off

pandoc feuille.md -o contenu.tex
python makeLatex.py

pdflatex -quiet feuille.tex

del contenu.tex

del feuille.aux
del feuille.log
del feuille.out
del feuille.thm