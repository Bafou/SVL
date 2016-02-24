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
		"""
		Permet d'effectuer un lancer de des, il y a plusieurs lancer de des dans un tour d'un joueur
		Le choix a ete fait que si une entree invalide a ete fait on met fin au lancer de des et 
		dans cela fera passer le tour au joueur (le joueur devra bien penser a son coup)
		"""
		score = 0
		fermee = []
		erreur = False
		coup=0
		for i in range (nb):
			score += self.generateur.generer_nombre()
		score_act = score
		while(score_act > 0 ):
			self.afficheur.notifier_demande_saisie()
			try:
				coup = self.lecteur.lire_saisie()
			except SaisieIncorrectError :
				erreur= True
			if coup <= score_act:
				if(self.est_fermee(coup)):
					erreur = True
				score_act -= coup
				self.fermer_tuile(coup)
				fermee.append(coup)
			else :
				erreur = True
			if erreur : 
				for tuile in fermee:
					self.ouvrir_tuile(tuile)
				self.afficheur.notifier_saisie_incorrect()
				raise LancerTerminerError()
		self.afficheur.notifier_lancer_terminer()

	def est_fermee(self, num_tuile):
		return self.plateau[num_tuile-1]

	def fermer_tuile(self, num_tuile):
		self.plateau[num_tuile-1]=True

	def ouvrir_tuile(self, num_tuile):
		self.plateau[num_tuile-1]=False

	"""
	def tuiles_disponible(self):
		res = []
		for i in range(len(self.plateau)):
			if not self.est_fermee(i+1):
				res.append(i+1)
		return res
	"""
class LancerTerminerError(Exception):
	pass
	
class SaisieIncorrectError(Exception):
	pass
