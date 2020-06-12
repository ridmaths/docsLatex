import json

## Mes fonctions 

def makeHeader():
	return r'''\documentclass{standalone}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{fourier}
\usepackage[scaled=0.875]{helvet} 
\renewcommand{\ttdefault}{lmtt} 
\usepackage{eurosym}
\usepackage[french]{babel}
\usepackage[np]{numprint}
\usepackage{amsmath,amssymb,mathrsfs}
\usepackage{pstricks,pst-plot,pstricks-add}

\definecolor{vert}{RGB}{24,128,48}

'''

def makeDocument(content):
	doc = makeHeader()
	doc += "\\begin{document}\n\n"
	doc += content
	doc += "\n\\end{document}"
	return doc

def tracerFonct(objFct):
	trace = "% Fonction\n"
	trace += f"\\psplot[linewidth=2.pt,linecolor={objFct['couleur']}]{{{objFct['definition'][0]}}}{{{objFct['definition'][1]}}}{{{objFct['expression']}}}\n"
	if 'nom' in objFct.keys():
		trace += f"\\rput[bl]({objFct['coordNom'][0]},{objFct['coordNom'][1]}){{\\textcolor{{{objFct['couleur']}}}{{${objFct['nom']}$}}}}\n"
	return trace

def makeGraph(params):
	# Config générale
	content = "%% Configuration\n"
	content += "\\psset{algebraic=true,dimen=middle,dotstyle=o,dotsize=5pt 0,linewidth=1.6pt,arrowsize=3pt 2,arrowinset=0.25}\n\n"
	# Début graphique
	content += f"\\begin{{pspicture*}}({params['axes']['xmin']},{params['axes']['ymin']})({params['axes']['xmax']},{params['axes']['ymax']})\n\n"
	# Grille
	content += "%% Grille\n"
	content += "% Lignes horizontales\n"
	content += f"\\multips(0,{params['axes']['ymin']})(0,{params['pasGrille']['ypas']}){{{int((params['axes']['ymax']-params['axes']['ymin'])/params['pasGrille']['ypas'])+1}}}{{\\psline[linestyle=dashed,linecap=1,dash=1.5pt 1.5pt,linewidth=1pt,linecolor=lightgray]{{c-c}}({params['axes']['xmin']},0)({params['axes']['xmax']},0)}}\n"
	content += "% Lignes verticales\n"
	content += f"\\multips({params['axes']['xmin']},0)({params['pasGrille']['xpas']},0){{{int((params['axes']['xmax']-params['axes']['xmin'])/params['pasGrille']['xpas'])+1}}}{{\\psline[linestyle=dashed,linecap=1,dash=1.5pt 1.5pt,linewidth=1pt,linecolor=lightgray]{{c-c}}(0,{params['axes']['ymin']})(0,{params['axes']['ymax']})}}\n\n"
	# Axes
	content += "%% Axes\n"
	content += f"\\psaxes[labelFontSize=\\scriptstyle,xAxis=true,yAxis=true,Dx=1.,Dy=1.,ticksize=-2pt 0,subticks=1]{{->}}(0,0)({params['axes']['xmin']},{params['axes']['ymin']})({params['axes']['xmax']},{params['axes']['ymax']})\n\n"
	# Tracé des fonctions
	content += "%% Tracé des fonctions\n"
	#TESTS#
	for objFct in params['fonctions']:
		if not 'definition' in objFct.keys():
			objFct["definition"] = [params['axes']['xmin'],params['axes']['xmax']]
		content += tracerFonct(objFct)
	content += "\\end{pspicture*}"
	return content

## Début script

# Chargement du fichier JSON contenant les paramètres 

paramsFile = open("params.json","r")
params = json.loads(paramsFile.read())
paramsFile.close()

# Création du document tex

nom = params["nom"]
file = open(nom+".tex","w")
codeGraphe = makeGraph(params)
document = makeDocument(codeGraphe)
file.write(document)
file.close()