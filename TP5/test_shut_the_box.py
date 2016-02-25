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

	def test_si_saisie_nombre_trop_grand_rollback_et_finis_sur_error(self):
		when(self.generateur_aleatoire_entre_1_et_6).generer_nombre().thenReturn(1)
		when(self.lecteur).lire_saisie().thenReturn(5).thenReturn(2)
		self.assertRaises(LancerTerminerError,self.jeu.lancer_des,2)
		inorder.verify(self.afficheur, times = 1).notifier_demande_saisie()
		inorder.verify(self.lecteur, times = 1).lire_saisie()
		inorder.verify(self.afficheur, times =1).notifier_saisie_incorrect()
		


	def test_les_tuiles_sont_toutes_debout_au_tout_debut(self):
		for i in range(9):
			self.assertFalse(self.jeu.est_fermee(i+1))

	def test_lance_des_fermer_tuile_deja_fermee_rollback_et_finis_sur_error(self):
		when(self.generateur_aleatoire_entre_1_et_6).generer_nombre().thenReturn(1).thenReturn(2)
		when(self.lecteur).lire_saisie().thenReturn(2).thenReturn(3)
		self.jeu.fermer_tuile(2)
		self.assertRaises(LancerTerminerError,self.jeu.lancer_des,2)
		inorder.verify(self.afficheur, times=1).notifier_demande_saisie()
		inorder.verify(self.lecteur,times= 1).lire_saisie()
		inorder.verify(self.afficheur, times =1).notifier_saisie_incorrect()
		

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
		self.assertRaises(LancerTerminerError,self.jeu.lancer_des,2)
		self.assertFalse(self.jeu.est_fermee(5))

	def test_saisie_incorrect_finit_avec_erreur(self):
		when(self.lecteur).lire_saisie().thenRaise(SaisieIncorrectError)
		when(self.generateur_aleatoire_entre_1_et_6).generer_nombre().thenReturn(1)
		self.assertRaises(LancerTerminerError, self.jeu.lancer_des,2)
		
	def test_tuile_disponible_retourne_tout_au_depart(self):
		self.assertEquals([1,2,3,4,5,6,7,8,9], self.jeu.tuiles_disponible())
		
	def test_tuile_disponible_retourne_bonne_tuile_quand_tuile_ferme(self):
		self.jeu.fermer_tuile(5)
		self.jeu.fermer_tuile(7)
		self.assertEquals([1,2,3,4,6,8,9], self.jeu.tuiles_disponible())
		
	def test_tuile_disponible_retourne_liste_vide_si_plus_de_tuile_jouable(self):
		for i in range(9):
			self.jeu.fermer_tuile(i+1)
		self.assertEquals([], self.jeu.tuiles_disponible())


class TestJeuFermerBoiteTour(unittest.TestCase):

	def setUp(self):
		self.generateur_aleatoire_entre_1_et_6 = mock()
		self.afficheur = mock()
		self.lecteur = mock()
		self.jeu = JeuFermerBoite(self.generateur_aleatoire_entre_1_et_6, self.lecteur, self.afficheur)
		self.joueur = mock()

	def test_tour_arrete_si_saisie_errone(self):
		when(self.lecteur).lire_saisie().thenRaise(SaisieIncorrectError)
		when(self.generateur_aleatoire_entre_1_et_6).generer_nombre().thenReturn(1)
		self.jeu.tour(self.joueur)
		verify(self.afficheur).notifier_tour_termine
		
	def test_tour_arrete_si_toutes_tuiles_fermee(self):
		for i in range(8):
			self.jeu.fermer_tuile(i+1)
		when(self.generateur_aleatoire_entre_1_et_6).generer_nombre().thenReturn(5).thenReturn(4)
		when(self.lecteur).lire_saisie().thenReturn(9)
		self.jeu.tour(self.joueur)
		verify(self.afficheur, times = 1).notifier_lancer_terminer()
		verify(self.afficheur, times = 1).notifier_tour_termine()
		
	def test_tour_terminer_au_deuxieme_lancer(self):
		when(self.generateur_aleatoire_entre_1_et_6).generer_nombre().thenReturn(5).thenReturn(4)
		when(self.lecteur).lire_saisie().thenReturn(9).thenRaise(SaisieIncorrectError)
		self.jeu.tour(self.joueur)
		verify(self.afficheur, times = 1).notifier_lancer_terminer()
		verify(self.afficheur, times = 1).notifier_tour_termine()
		
	def test_tour_si_tuile_7_8_9_ferme_demande_a_combien_de_des_lance(self):
		self.jeu.fermer_tuile(7)
		self.jeu.fermer_tuile(8)
		self.jeu.fermer_tuile(9)
		when(self.generateur_aleatoire_entre_1_et_6).generer_nombre().thenReturn(1)
		when(self.lecteur).lire_des().thenReturn(2)
		when(self.lecteur).lire_saisie().thenReturn(2)
		self.jeu.tour(self.joueur)
		verify(self.afficheur).notifier_choix_lancer_des()
		verify(self.lecteur).lire_des()
	
	def test_fin_tour_ajout_des_points_au_score_du_joueur(self):
		self.jeu.fermer_tuile(7)
		self.jeu.fermer_tuile(8)
		self.jeu.fermer_tuile(9)
		when(self.generateur_aleatoire_entre_1_et_6).generer_nombre().thenReturn(1)
		when(self.lecteur).lire_des().thenReturn(2)
		when(self.lecteur).lire_saisie().thenRaise(SaisieIncorrectError)
		self.jeu.tour(self.joueur)
		verify(self.joueur).augmente_score(21)
		
	def test_ouvrir_toutes_tuiles_remet_a_zero_les_tuiles(self):
		self.jeu.fermer_tuile(7)
		self.jeu.fermer_tuile(8)
		self.jeu.fermer_tuile(9)
		self.jeu.ouvrir_toutes_tuiles()
		self.assertEquals([1,2,3,4,5,6,7,8,9], self.jeu.tuiles_disponible())
		
class TestJeuFermerBoiteJouer(unittest.TestCase):
	
	def setUp(self):
		self.generateur_aleatoire_entre_1_et_6 = mock()
		self.afficheur = mock()
		self.lecteur = mock()
		self.jeu = JeuFermerBoite(self.generateur_aleatoire_entre_1_et_6, self.lecteur, self.afficheur)
		self.joueur1 = mock()
		self.joueur2 = mock()
		
	def test_jeu_arrete_apres_deux_joueurs_ont_joues_quand_on_indique_un_tour(self):
		when(self.generateur_aleatoire_entre_1_et_6).generer_nombre().thenReturn(1)
		when(self.lecteur).lire_des().thenReturn(2)
		when(self.lecteur).lire_saisie().thenRaise(SaisieIncorrectError)
		when(self.joueur1).score().thenReturn(15)
		when(self.joueur2).score().thenReturn(10)
		self.jeu.jouer([self.joueur1,self.joueur2],1)
		verify(self.afficheur,times = 1).notifier_debut_tour(self.joueur1)
		verify(self.afficheur,times = 1).notifier_debut_tour(self.joueur2)
		verify(self.afficheur,times = 1).notifier_jeu_termine()
		
	def test_jeu_arrete_si_tuile_toute_ferme_et_declare_vainqueur_celui_qui_a_ferme_les_tuiles(self):
		when(self.generateur_aleatoire_entre_1_et_6).generer_nombre().thenReturn(1)
		when(self.lecteur).lire_des().thenReturn(2)
		when(self.lecteur).lire_saisie().thenRaise(SaisieIncorrectError)
		for i in range(9):
			self.jeu.fermer_tuile(i+1)
		self.jeu.jouer([self.joueur1,self.joueur2],2)
		verify(self.afficheur,times = 1).notifier_debut_tour(self.joueur1)
		verify(self.afficheur,times = 0).notifier_debut_tour(self.joueur2)
		verify(self.afficheur,times = 1).notifier_jeu_termine()
		verify(self.afficheur,times = 1).notifier_joueur_gagnant(self.joueur1)
		
	def test_jeu_a_fin_tour_calcul_gagnant(self):
		when(self.generateur_aleatoire_entre_1_et_6).generer_nombre().thenReturn(1)
		when(self.lecteur).lire_des().thenReturn(2)
		when(self.lecteur).lire_saisie().thenRaise(SaisieIncorrectError)
		when(self.joueur1).score().thenReturn(15)
		when(self.joueur2).score().thenReturn(10)
		self.jeu.jouer([self.joueur1,self.joueur2],2)
		verify(self.afficheur,times = 1).notifier_joueur_gagnant(self.joueur2)
