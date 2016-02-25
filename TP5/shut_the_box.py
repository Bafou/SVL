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
			if not erreur and coup <= score_act:
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
		
	def ouvrir_toutes_tuiles(self):
		self.plateau = [False]*9
		
	def tour(self, joueur):
		termine = False
		while (not(termine)) :
			des = 2
			if self.est_fermee(7) and self.est_fermee(8) and self.est_fermee(9):
				self.afficheur.notifier_choix_lancer_des()
				des = self.lecteur.lire_des()
			try :
				self.lancer_des(des)
				break
			except LancerTerminerError: 
				termine = True
			if self.tuiles_disponible() == []:
				termine = True
		self.afficheur.notifier_tour_termine()
		joueur.augmente_score(sum(self.tuiles_disponible()))
	
	def tuiles_disponible(self):
		res = []
		for i in range(len(self.plateau)):
			if not self.est_fermee(i+1):
				res.append(i+1)
		return res
	
	def jouer(self, listJoueurs, nbTour):
		tour_restant = nbTour
		termine = False
		gagnant = None
		while not(termine) and tour_restant >0:
			for joueur in listJoueurs:
				self.afficheur.notifier_debut_tour(joueur)
				self.tour(joueur)
				if self.tuiles_disponible() == []:
					termine = True
					gagnant = joueur
					break
			tour_restant -= 1
		self.afficheur.notifier_jeu_termine()
		if gagnant != None :
			self.afficheur.notifier_joueur_gagnant(gagnant)
		else : 
			gagnant = listJoueurs[0]
			for joueur in listJoueurs :
				if joueur.score() < gagnant.score():
					gagnant = joueur
			self.afficheur.notifier_joueur_gagnant(gagnant)
	
class LancerTerminerError(Exception):
	pass
	
class SaisieIncorrectError(Exception):
	pass
