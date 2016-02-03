"""
PETIT Antoine & WISSOCQ Sarah

Test Login
"""

import unittest
from mockito import *
from login import *

class TestCreationUtilisateur(unittest.TestCase):

	def setUp(self):
		self.nom = "nom"
		self.prenom = "prenom"
		self.login = "login"
		self.fabrique_utilisateur = mock()
		self.service_creation = ServiceCreationUtilisateur(self.fabrique_utilisateur)

	def test_login_trop_long_echoue(self):
		login = "nomprenom"
		self.assertRaises(LoginTropLongError, self.service_creation.creer_utilisateur, self.nom, self.prenom, login)

	def test_login_mauvais_format_echoue(self):
		login = "NOM"
		self.assertRaises(LoginMauvaisFormatError, self.service_creation.creer_utilisateur, self.nom, self.prenom, login)

	def test_prenom_mauvais_format_echoue(self):
		prenom = "457"
		self.assertRaises(PrenomMauvaisFormatError, self.service_creation.creer_utilisateur, self.nom, prenom, self.login)

	def test_nom_mauvais_format_echoue(self):
		nom = "42"
		self.assertRaises(NomMauvaisFormatError, self.service_creation.creer_utilisateur, nom, self.prenom, self.login)

	def test_login_vide_echoue(self):
		login = ""
		self.assertRaises(LoginVideError, self.service_creation.creer_utilisateur, self.nom, self.prenom, login)

	def test_nom_vide_echoue(self):
		nom = ""
		self.assertRaises(NomVideError, self.service_creation.creer_utilisateur, nom, self.prenom, self.login)

	def test_prenom_vide_echoue(self):
		prenom = ""
		self.assertRaises(PrenomVideError, self.service_creation.creer_utilisateur, self.nom, prenom, self.login)
	
	def test_utilisateur_est_cree(self):
		utilisateur = mock()
		when(self.fabrique_utilisateur).creation_utilisateur(self.nom, self.prenom, self.login).thenReturn(utilisateur)
		self.assertEqual(self.service_creation.creer_utilisateur(self.nom, self.prenom, self.login), utilisateur)
		
	def test_utilisateur_login_deja_existant_echoue(self):
		when(self.fabrique_utilisateur).creation_utilisateur(self.nom, self.prenom, self.login).thenRaise(LoginDejaExistantError)
		self.assertRaises(LoginDejaExistantError, self.service_creation.creer_utilisateur, self.nom, self.prenom, self.login)
		
class TestCreeLogin(unittest.TestCase):

	def setUp(self):
		self.bdd = mock()
		self.service_login = ServiceCreationLogin(self.bdd)
		self.nom = "nom"
		self.prenom = "prenom"

	def test_creer_login_methodeA_nom_court_donne_nom(self):
		when(self.bdd).existe_deja(self.nom).thenReturn(False)
		self.assertEqual("nom",self.service_login.creer_login(self.nom, self.prenom))
		
	def test_creer_login_methodeA_nom_court_retourne_bon_format(self):
		when(self.bdd).existe_deja(self.nom).thenReturn(False)
		nomMaj= "Nom"
		self.assertTrue(self.service_login.creer_login(nomMaj, self.prenom).islower())
		
	def test_creer_login_methodeA_nom_taille8_donne_nom(self):
		when(self.bdd).existe_deja(self.nom).thenReturn(False)
		taille8 = "nomtaill"
		self.assertEqual("nomtaill", self.service_login.creer_login(taille8, self.prenom))
		
	def test_creer_login_methodeA_nom_taille_sup_a_8_donne_nom_coupe(self):
		when(self.bdd).existe_deja(self.nom).thenReturn(False)
		nomlong = "nomtroplong"
		self.assertEqual("nomtropl", self.service_login.creer_login(nomlong, self.prenom))
		
	def test_creer_login_methodeA_nom_taille_sup_a_8_donne_bon_format(self):
		when(self.bdd).existe_deja(self.nom).thenReturn(False)
		nomlong = "NomTroplong"
		self.assertTrue(self.service_login.creer_login(nomlong, self.prenom).islower())
		
	def test_creer_login_utilise_methodeB_si_utilisateur_existe_deja_en_base(self):
		when(self.bdd).existe_deja(self.nom).thenReturn(True)
		self.assertEqual("nomp",self.service_login.creer_login(self.nom, self.prenom))
		
	def test_creer_login_utilise_methodeB_bon_format_nom_taille7(self):
		taille7 = "nomtail"
		when(self.bdd).existe_deja(taille7).thenReturn(True)
		self.assertEqual("nomtailp",self.service_login.creer_login(taille7, self.prenom))
		
	def test_creer_login_utilise_methodeB_bon_format_trop_long(self):
		nomlong = "nomtroplong"
		when(self.bdd).existe_deja("nomtropl").thenReturn(True)
		self.assertEqual("nomtropp",self.service_login.creer_login(nomlong, self.prenom))
		
	def test_creer_login_echoue_deux_fois_renvoie_erreur(self):
		nomlong = "nomtroplong"
		when(self.bdd).existe_deja("nomtropl").thenReturn(True)
		when(self.bdd).existe_deja("nomtropp").thenReturn(True)
		self.assertRaises(MethodeAEtBOnEchoueError, self.service_login.creer_login, nomlong, self.prenom)
