"""
PETIT Antoine & WISSOCQ Sarah

Application web calculant le poids idéal en fonction de la taille donnée en cm
"""

import cherrypy

PAGE_INDEX = """
<html>
<head>
<title>Calculateur de poids idéal</title>
</head>
<body>
	<h1 id="h1_information">Calculez votre poids idéal</h1>
	<form id='id_formulaire_calcul_poids' method='post'>
		<label id= 'id_label_taille'>Taille :</label>
		<input id='id_boite_saisie_taille' name='taille' type='text'/>
		<label id= 'id_label_metre'>mètres</label>
	</form>
</body>
</html>
"""

PAGE_RESULTAT_ERRONE  = """
<html>
<head>
<title>Calculateur de poids idéal</title>
</head>
<body>
	<h1 id="h1_information">Calculez votre poids idéal</h1>
	<form id='id_formulaire_calcul_poids' method='post'>
		<label id= 'id_label_taille'>Taille :</label>
		<input id='id_boite_saisie_taille' name='taille' type='text'/>
		<label id= 'id_label_metre'>mètres</label>
		</br>
		<label id='id_message_valeur_erronee'><font color="red">Valeur erronée</font></label>
	</form>
</body>
</html>
"""

class AppliPoids:

	@cherrypy.expose
	def index(self, taille = None):
		if(taille == None):
			return PAGE_INDEX
		else:
			return PAGE_RESULTAT_ERRONE

if __name__ == '__main__':
	cherrypy.quickstart(AppliPoids())


class CalculPoids():

	def calcul_poids(self,taille):
		try:
			float(taille)
		except ValueError:
			raise TailleInvalideError()
		if taille>0:
			#homme
			return taille * 100 - 100 - (taille * 100 - 150) / 4
		else:	
			raise TailleInvalideError()



class TailleInvalideError(Exception):
	pass