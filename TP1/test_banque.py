"""
Test banque
"""
import unittest
from banque import *


class TestCreationCompte(unittest.TestCase):

	def test_un_compte_est_creer_avec_solde_nul(self):
		""" test un compte est creer avec solde nul """
		compte=Compte()
		self.assertEqual(0.0, compte.solde)

	def test_un_compte_est_creer_avec_solde_non_nul(self):
		""" test un compte est creer avec solde non nul """
		compte=Compte(50.0)
		self.assertEqual(50.0, compte.solde)

class TestCrediterCompte(unittest.TestCase):

	def test_crediter_un_compte_augmente_son_solde(self):
		""" test un compte crediter augmente son solde  """
		compte=Compte()
		compte.crediter(12.0)
		self.assertEqual(12.0, compte.solde)

	def test_crediter_un_montant_negatif(self):
		""" test un compte crediter un montant negatif """
		compte=Compte()
		self.assertRaises(MontantIncorrectError,
						  compte.crediter,
						  -15.0)

	def test_crediter_un_compte_plusieur_fois(self):
		""" test un compte crediter plusieur fois """
		compte=Compte()
		compte.crediter(12.0)
		compte.crediter(30.0)
		self.assertEqual(42.0, compte.solde)

	def test_crediter_un_compte_montant_strictement_positif(self):
		""" test un compte crediter un montant strictement positif """
		compte=Compte()
		self.assertRaises(MontantIncorrectError,
						  compte.crediter,
						  0.0)

class TestDebiterCompte(unittest.TestCase):

	def test_debiter_un_compte_debite_son_solde(self):
		""" test un compte debiter diminue son solde """
		compte=Compte(50)
		compte.debiter(10.0)
		self.assertEqual(40.0,compte.solde)

	def test_debiter_un_compte_debite_solde_negatif(self):
		""" test un compte debiter diminue son solde negatif donne erreur """
		compte=Compte()
		self.assertRaises(SoldeNegatifError,
						  compte.debiter,
						  10)

	def test_debiter_un_montant_negatif(self):
		""" test un compte debiter un montant negatif """
		compte=Compte()
		self.assertRaises(MontantIncorrectError,compte.debiter,-10.0)

	def test_debiter_un_compte_plusieur_fois(self):
		""" test un compte debiter plusieur fois """
		compte=Compte(50)
		compte.debiter(20.0)
		compte.debiter(5.0)
		self.assertEqual(25.0,compte.solde)	

	def test_debiter_un_montant_strictement_positif(self):
		""" test un compte debiter un montant strictement positif"""
		compte=Compte()
		self.assertRaises(MontantIncorrectError,compte.debiter,0.0)

	def test_debiter_un_montant_egal_au_solde(self):
		""" test un compte debiter un montant egal au solde"""
		compte=Compte(42.0)
		compte.debiter(42.0)
		self.assertEqual(0.0, compte.solde)


