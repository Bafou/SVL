"""
Petit Antoine & Wissocq Sarah


Deviner un nombre - jeu

	- Nombre à deviner entre 0 et 9
	- un joueur essaie de deviner ce nombre en faisant
	  des propositions au clavier, en au max N tentatives
"""
import sys

class JeuDevinerUnNombre:

	def __init__(self, generateur, lecteur, afficheur):
		self.generateur = generateur
		self.lecteur = lecteur
		self.afficheur = afficheur

	def jouer(self):
		a_deviner = self.generateur.genere_nombre_a_deviner()
		gagne = False
		while not gagne :
			self.afficheur.notifier_invitation_choisir_un_nombre()
			proposition = self.lecteur.lire_un_nombre()
			if proposition == a_deviner:
				gagne = True
			elif proposition < a_deviner:
				self.afficheur.notifier_nombre_trop_petit()
			else : 
				self.afficheur.notifier_nombre_trop_grand()

		self.afficheur.notifier_joueur_a_gagne()

class LecteurSurEntreeStrandard:
	"""
	>>> lecteur = LecteurSurEntreeStrandard()
	>>> lecteur.lire_un_nombre()
	"""
	
	def __init__(self, flot_entree = sys.stdin):
		self.flot_entree = flot_entree

	def lire_un_nombre(self):
		return int(self.flot_entree.readline())