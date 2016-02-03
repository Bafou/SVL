"""
Test my_banque
"""
import unittest
from my_banque import *


class TestCreationCompte(unittest.TestCase):

	def test_un_compte_est_creer_avec_solde_nul(self):
		""" test un compte est creer avec solde nul pour my_banque """
		compte=Compte()
		self.assertEqual([0.0], compte.solde)

class TestCrediterCompte(unittest.TestCase):

	def test_crediter_un_compte_augmente_son_solde(self):
		""" test un compte crediter augmente son solde pour my_banque """
		compte=Compte()
		compte.crediter(12.0)
		self.assertEqual([0.0,12.0], compte.solde)

	def test_crediter_un_montant_negatif(self):
		""" test un compte crediter un montant negatif pour my_banque """
		compte=Compte()
		self.assertRaises(MontantIncorrectError,
						  compte.crediter,
						  -15.0)

	def test_crediter_un_compte_plusieur_fois(self):
		""" test un compte crediter un compte plusieur fois pour my_banque """
		compte=Compte()
		compte.crediter(12.0)
		compte.crediter(30.0)
		self.assertEqual([0.0,12.0,30.0], compte.solde)

	def test_crediter_un_compte_montant_strictement_positif(self):
		""" test un compte crediter montant strictement positif pour my_banque """
		compte=Compte()
		self.assertRaises(MontantIncorrectError,
						  compte.crediter,
						  0.0)