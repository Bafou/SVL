"""
PETIT Antoine & WISSOCQ Sarah

Application web calculant le poids idéal en fonction de la taille donnée en mètres
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
		<label id='id_label_metre'>mètres</label>
		</br>
		<label id='id_label_sexe'>Sexe :</label>
		<input id='id_bouton_homme' checked="true" type=radio name=sexe value=0> Homme 
		<input id='id_bouton_femme' type=radio name=sexe value=1> Femme </br>
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
		<label id= 'id_label_sexe'>Sexe :</label>
		<input id='id_bouton_homme' checked="true" type=radio name=sexe value=0> Homme 
		<input id='id_bouton_femme' type=radio name=sexe value=1> Femme </br>
		<label id='id_message_valeur_erronee'><font color="red">Valeur erronée</font></label>
	</form>
</body>
</html>
"""

PAGE_RESULTAT_DEBUT  = """
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
		<label id= 'id_label_sexe'>Sexe :</label>
		<input id='id_bouton_homme' checked="true" type=radio name=sexe value=0> Homme 
		<input id='id_bouton_femme' type=radio name=sexe value=1> Femme </br>
		<label id='id_resultat'>Votre poids idéal est 
"""

PAGE_RESULTAT_FIN = """
 kg<label>
	</form>
</body>
</html>
"""

class AppliPoids:

	@cherrypy.expose
	def index(self, taille = None, sexe = None):
		if(taille == None):
			return PAGE_INDEX
		else:
			cp = CalculPoids()
			try:
				resultat=cp.calcul_poids(taille, sexe)
				return PAGE_RESULTAT_DEBUT + str(resultat)  + PAGE_RESULTAT_FIN
			except TailleInvalideError:
				return PAGE_RESULTAT_ERRONE


class CalculPoids():

	def __init__(self):
		pass

	def calcul_poids(self,taille, sexe = 0):
		try:
			ftaille = float(taille)
		except ValueError:
			raise TailleInvalideError()
		if ftaille>0:
			if (int(sexe) == 0) :#homme
				return ftaille * 100 - 100 - (ftaille * 100 - 150) / 4
			else :
				return ftaille * 100 - 100 - (ftaille * 100 - 150) / 2.5
		else:	
			raise TailleInvalideError()



class TailleInvalideError(Exception):
	pass

if __name__ == '__main__':
	cherrypy.quickstart(AppliPoids())


