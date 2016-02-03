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