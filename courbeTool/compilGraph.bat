@echo off
python makeGraph.py

latex mongraphique.tex
dvips mongraphique.dvi
ps2pdf mongraphique.ps

del mongraphique.dvi
del mongraphique.ps
del mongraphique.log
del mongraphique.aux

mongraphique.pdf