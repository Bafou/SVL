"""
Test le jeu "Fermer la boite"
PETIT Antoine & WISSOCQ Sarah
"""
import unittest
from mockito import *
from shut_the_box import *

class TestJeuFermerBoiteLancerDes(unittest.TestCase):

	def setUp(self):
		self.generateur_aleatoire_entre_1_et_6 = mock()
		self.afficheur = mock()
		self.lecteur = mock()
		self.jeu = JeuFermerBoite(self.generateur_aleatoire_entre_1_et_6, self.lecteur, self.afficheur)


	def test_lance_2_des(self):
		when(self.generateur_aleatoire_entre_1_et_6).generer_nombre().thenReturn(1).thenReturn(1)
		when(self.lecteur).lire_saisie().thenReturn(2)
		self.jeu.lancer_des(2)
		verify(self.generateur_aleatoire_entre_1_et_6, times = 2).generer_nombre()
		verify(self.generateur_aleatoire_entre_1_et_6, times = 2).generer_nombre()
	
	def test_lance_1_des(self):
		when(self.generateur_aleatoire_entre_1_et_6).generer_nombre().thenReturn(1).thenReturn(1)
		when(self.lecteur).lire_saisie().thenReturn(1)
		self.jeu.lancer_des(1)
		verify(self.generateur_aleatoire_entre_1_et_6, times = 1).generer_nombre()

	
	def test_demande_une_fois_si_joueur_consomme_tout_point(self):
		when(self.generateur_aleatoire_entre_1_et_6).generer_nombre().thenReturn(1).thenReturn(1)
		when(self.lecteur).lire_saisie().thenReturn(2)
		self.jeu.lancer_des(2)
		inorder.verify(self.afficheur, times=1).notifier_demande_saisie()
		inorder.verify(self.lecteur,times= 1).lire_saisie()
		inorder.verify(self.afficheur, times=1).notifier_lancer_terminer()

	def test_demande_deux_fois_si_joueur_consomme_pas_point(self):
		when(self.generateur_aleatoire_entre_1_et_6).generer_nombre().thenReturn(2).thenReturn(1)
		when(self.lecteur).lire_saisie().thenReturn(1).thenReturn(2)
		self.jeu.lancer_des(2)
		inorder.verify(self.afficheur, times=2).notifier_demande_saisie()
		inorder.verify(self.lecteur,times= 2).lire_saisie()
		inorder.verify(self.afficheur, times=2).notifier_demande_saisie()
		inorder.verify(self.lecteur,times= 2).lire_saisie()
		inorder.verify(self.afficheur, times=1).notifier_lancer_terminer()

	def test_redemande_saisie_si_saisie_nombre_trop_grand(self):
		when(self.generateur_aleatoire_entre_1_et_6).generer_nombre().thenReturn(1)
		when(self.lecteur).lire_saisie().thenReturn(5).thenReturn(2)
		self.jeu.lancer_des(2)
		inorder.verify(self.afficheur, times = 2).notifier_demande_saisie()
		inorder.verify(self.lecteur, times = 2).lire_saisie()
		inorder.verify(self.afficheur, times = 2).notifier_demande_saisie()
		inorder.verify(self.lecteur,times = 2).lire_saisie()
		inorder.verify(self.afficheur,times = 1).notifier_lancer_terminer()

	def test_les_tuiles_sont_toutes_debout_au_tout_debut(self):
		for i in range(9):
			self.assertFalse(self.jeu.est_fermee(i+1))

	def test_ferme_une_tuile_deja_ferme_erreur(self):
		self.jeu.fermer_tuile(3)
		self.assertRaises(DejaFermerError, self.jeu.fermer_tuile, 3)

	def test_lance_des_fermer_tuile_deja_fermee_erreur(self):
		when(self.generateur_aleatoire_entre_1_et_6).generer_nombre().thenReturn(1).thenReturn(1)
		when(self.lecteur).lire_saisie().thenReturn(2)
		self.jeu.fermer_tuile(2)
		self.assertRaises(DejaFermerError, self.jeu.lancer_des, 2)
		inorder.verify(self.afficheur, times=1).notifier_demande_saisie()
		inorder.verify(self.lecteur,times= 1).lire_saisie()

	def test_lance_des_ferme_la_tuile_demandee(self):
		when(self.generateur_aleatoire_entre_1_et_6).generer_nombre().thenReturn(1).thenReturn(1)
		when(self.lecteur).lire_saisie().thenReturn(2)
		self.jeu.lancer_des(2)
		self.assertTrue(self.jeu.est_fermee(2))
		
	def test_lance_des_fermes_les_tuiles_demandees(self):
		when(self.generateur_aleatoire_entre_1_et_6).generer_nombre().thenReturn(2).thenReturn(1)
		when(self.lecteur).lire_saisie().thenReturn(1).thenReturn(2)
		self.jeu.lancer_des(2)
		self.assertTrue(self.jeu.est_fermee(1))
		self.assertTrue(self.jeu.est_fermee(2))

	def test_lance_des_finit_avec_erreur_ne_ferme_pas(self):
		when(self.generateur_aleatoire_entre_1_et_6).generer_nombre().thenReturn(1).thenReturn(1)
		when(self.lecteur).lire_saisie().thenReturn(5).thenReturn(2)
		self.jeu.lancer_des(2)
		self.assertFalse(self.jeu.est_fermee(5))

class TestJeuFermerBoiteTour(unittest.TestCase):

	pass