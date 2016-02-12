"""
Shut the box
PETIT Antoine & WISSOCQ Sarah
"""

class JeuFermerBoite():

	def __init__(self, generateur, lecteur, afficheur):
		self.generateur = generateur
		self.lecteur = lecteur
		self.afficheur = afficheur
		self.plateau = [False]*9

	def lancer_des(self, nb):
		score = 0
		a_fermer = []
		for i in range (nb):
			score += self.generateur.generer_nombre()
		while(score > 0 ):
			self.afficheur.notifier_demande_saisie()
			coup = self.lecteur.lire_saisie()
			if coup <= score:
				if(self.est_fermee(coup)):
					raise DejaFermerError()
				score -= coup
				a_fermer.append(coup)

		for tuile in a_fermer:
			self.fermer_tuile(tuile)
		self.afficheur.notifier_lancer_terminer()

	def est_fermee(self, num_tuile):
		return self.plateau[num_tuile-1]

	def fermer_tuile(self, num_tuile):
		if self.est_fermee(num_tuile):
			raise DejaFermerError()
		self.plateau[num_tuile-1]=True


class DejaFermerError(Exception):
	pass