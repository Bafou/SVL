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
		fermee = []
		erreur = False
		for i in range (nb):
			score += self.generateur.generer_nombre()
		if not peut_jouer(score,self.tuiles_disponible()):
			raise PeutPlusJouer()
		score_act = score
		while(not(erreur) and score_act > 0 ):
			self.afficheur.notifier_demande_saisie()
			coup = self.lecteur.lire_saisie()
			if coup <= score_act:
				if(self.est_fermee(coup)):
					erreur = True
				score_act -= coup
				self.fermer_tuile(coup)
				fermee.append(coup)
			if erreur : #rollback
				for tuile in fermee:
					self.ouvrir_tuile(tuile)
				self.afficheur.notifier_saisie_incorrect()
				erreur = False
				score_act = score
		else :
			self.afficheur.notifier_lancer_terminer()

	def est_fermee(self, num_tuile):
		return self.plateau[num_tuile-1]

	def fermer_tuile(self, num_tuile):
		self.plateau[num_tuile-1]=True

	def ouvrir_tuile(self, num_tuile):
		self.plateau[num_tuile-1]=False

	def peut_jouer(self,des, tuiles_disponible):
		if des <=9:
			if des in tuiles_disponible:
				return True
		res = False
		for i in tuiles_disponible:
			tuiles_disponible.remove(i)
			res = res or self.peut_jouer(des-i,tuiles_disponible)
			tuiles_disponible.append(i)
		return res

		

	def tuiles_disponible(self):
		res = []
		for i in range(len(self.plateau)):
			if not self.est_fermee(i+1):
				res.append(i+1)
		return res

class PeutPlusJouer(Exception):
	pass