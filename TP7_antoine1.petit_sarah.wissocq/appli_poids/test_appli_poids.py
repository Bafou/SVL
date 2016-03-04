"""
PETIT Antoine & WISSOCQ Sarah
Test de l'application d'affichage de poids idéal
"""

from selenium import webdriver
import unittest
from appli_poids import *


class TestPageCalculPoids(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.navigateur = webdriver.Firefox()
		cls.navigateur.get('http://localhost:8080')

	@classmethod
	def tearDownClass(cls):
		cls.navigateur.quit()

	def test_la_page_a_un_titre(self):
		titre = self.navigateur.title

		self.assertEqual("Calculateur de poids idéal",titre)

	def test_la_page_a_un_titre_h1(self):
		h1 = self.navigateur.find_element_by_id("h1_information")
		text= h1.text
		self.assertEqual("Calculez votre poids idéal",text)

	def test_la_page_contient_une_boite_de_saisie(self):
		boite = self.navigateur.find_element_by_id('id_boite_saisie_taille')
		type = boite.get_attribute('type')
		self.assertEqual("text", type)

	def test_la_page_contient_un_label_avec_taille(self):
		label = self.navigateur.find_element_by_id('id_label_taille')
		text = label.text
		self.assertEqual("Taille :", text)
		
	def test_la_page_contient_un_label_sexe(self):
		label = self.navigateur.find_element_by_id('id_label_sexe')
		text = label.text
		self.assertEqual("Sexe :", text)

	def test_la_page_contient_un_label_metre(self):
		label = self.navigateur.find_element_by_id('id_label_metre')
		text = label.text
		self.assertEqual("mètres", text)
	
	def test_la_page_contient_un_bouton_homme(self):
		bouton = self.navigateur.find_element_by_id('id_bouton_homme')
		type = bouton.get_attribute('type')
		self.assertEqual("radio", type)
		
	def test_la_page_contient_un_bouton_homme_check_par_defaut(self):
		bouton = self.navigateur.find_element_by_id('id_bouton_homme')
		check = bouton.get_attribute('checked')
		self.assertEqual("true", check)
		
	def test_la_page_contient_un_bouton_femme(self):
		bouton = self.navigateur.find_element_by_id('id_bouton_femme')
		type = bouton.get_attribute('type')
		self.assertEqual("radio", type)
	
	def test_affiche_le_poids(self):
		boite = self.navigateur.find_element_by_id('id_boite_saisie_taille')
		boite.send_keys("1.60\n")
		message = self.navigateur.find_element_by_id('id_resultat')
		self.assertEqual(message.text, "Votre poids idéal est 57.5 kg")
		
	def test_index_retourne_quand_page_par_defaut(self):
		appli_poids = AppliPoids()
		self.assertEqual(PAGE_INDEX,appli_poids.index())
		
	def test_index_retourne_bon_resultat_quand_donne_correct(self):
		appli_poids = AppliPoids()
		result = PAGE_RESULTAT_DEBUT + '57.5' + PAGE_RESULTAT_FIN
		self.assertEqual(result,appli_poids.index(1.60,0))
		
	def test_index_retourne_erreur_quand_donnee_incorrect(self):
		appli_poids = AppliPoids()
		self.assertEqual(PAGE_RESULTAT_ERRONE,appli_poids.index("erreur",0))


class TestPageCalculPoidsErronee(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.navigateur = webdriver.Firefox()
		cls.navigateur.get('http://localhost:8080')

	@classmethod
	def tearDownClass(cls):
		cls.navigateur.quit()

	def test_la_valeur_entree_est_erronee_affichage_message_erreur(self):        
         boite = self.navigateur.find_element_by_id('id_boite_saisie_taille')
         boite.send_keys("&é(\n")
         message = self.navigateur.find_element_by_id('id_message_valeur_erronee')
         self.assertEqual(message.text, "Valeur erronée")


class TestCalculPoids(unittest.TestCase):
	
	def test_calcul_poid_taille_inferieur_a_zero_error(self):
		cp = CalculPoids()
		self.assertRaises(TailleInvalideError,cp.calcul_poids,-5)

	def test_calcul_poid_taille_egal_a_zero_error(self):
		cp = CalculPoids()
		self.assertRaises(TailleInvalideError,cp.calcul_poids,0)	

	def test_saisie_texte_invalide_error(self):
		cp = CalculPoids()
		self.assertRaises(TailleInvalideError,cp.calcul_poids,"Cacahuete")		
		
	def test_Calcul_poids(self):
		cp = CalculPoids()
		self.assertEqual(57.5,cp.calcul_poids(1.60))
		
	def test_Calcul_poids_homme(self):
		cp = CalculPoids()
		self.assertEqual(57.5,cp.calcul_poids(1.60,0))
		
	def test_Calcul_poids_femme(self):
		cp = CalculPoids()
		self.assertEqual(56.,cp.calcul_poids(1.60,1))				
