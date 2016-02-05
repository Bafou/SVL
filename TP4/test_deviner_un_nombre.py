"""
Petit Antoine & Wissocq Sarah


"""


import unittest
import io
from mockito import *
from deviner_un_nombre import *

class TestJeuDevinerUnNombre(unittest.TestCase):
	"""
	Scénarios à tester :
		- le joueur gagne du premier coup
		- le joueur gagne en plusieurs coups
		- le joueur gagne en exactement N tentatives
		- le joueur perd


	(	- Respect nombre de tours
		- Repond correctement à n'importe quel information:	- trop grand
															- trop petit
															- juste)

	"""

	def setUp(self):
		self.generateur_nombre_entre_0_et_9 = mock()
		self.lecteur = mock()
		self.afficheur = mock()
		self.jeu = JeuDevinerUnNombre(self.generateur_nombre_entre_0_et_9, self.lecteur, self.afficheur)



	def test_le_joueur_gagne_du_premier_coup(self):

		A_DEVINER = 4
		when(self.generateur_nombre_entre_0_et_9).genere_nombre_a_deviner().thenReturn(A_DEVINER)
		when(self.lecteur).lire_un_nombre().thenReturn(A_DEVINER)
		self.jeu.jouer()
		verify(self.afficheur).notifier_invitation_choisir_un_nombre()
		verify(self.afficheur).notifier_joueur_a_gagne()
		#verify(self.afficheur).notifier_joueur_a_perdu()

	def test_le_joueur_gagne_en_plusieurs_coup(self):

		A_DEVINER = 4
		TROP_PETIT = 3
		TROP_GRAND = 6
		when(self.generateur_nombre_entre_0_et_9).genere_nombre_a_deviner().thenReturn(A_DEVINER)
		when(self.lecteur).lire_un_nombre().thenReturn(TROP_PETIT).thenReturn(TROP_GRAND).thenReturn(A_DEVINER)
		self.jeu.jouer()
		inorder.verify(self.afficheur, times = 3).notifier_invitation_choisir_un_nombre()
		inorder.verify(self.afficheur).notifier_nombre_trop_petit()
		inorder.verify(self.afficheur, times = 3).notifier_invitation_choisir_un_nombre()
		inorder.verify(self.afficheur).notifier_nombre_trop_grand()
		inorder.verify(self.afficheur, times = 3).notifier_invitation_choisir_un_nombre()
		inorder.verify(self.afficheur).notifier_joueur_a_gagne()

class TestLecteurSurEntreeStrandard(unittest.TestCase):
	"""
	fonctionnalité à tester : lire_un_nombre
		- nominal : renvoie bien un nombre entre 0 et 9 
		  correspondant à l'entrée au clavier
		- exception : echec si entree erronee
	"""

	def setUp(self):
		self.flot_entree =  io.StringIO("5\n")
		self.lecteur = LecteurSurEntreeStrandard(self.flot_entree)

	def test_le_nombre_retourne_correspond_a_l_entre(self):
		self.assertEqual(5, self.lecteur.lire_un_nombre())

"""
class TestIntegration:

	def test_joueur_avec_un_vrai_lecteur(self):
		#/!\ pas un vrai test /!\ Attends une entrée
		A_DEVINER = 4
		generateur_nombre_entre_0_et_9 = mock()
		when(generateur_nombre_entre_0_et_9).genere_nombre_a_deviner().thenReturn(A_DEVINER)
		lecteur = LecteurSurEntreeStrandard()
		afficheur = mock()
		jeu = JeuDevinerUnNombre(generateur_nombre_entre_0_et_9, lecteur, afficheur)
		jeu.jouer()
		verify(afficheur).notifier_invitation_choisir_un_nombre()
		verify(afficheur).notifier_joueur_a_gagne()
"""