"""
Test Zorglang

>>> traducteur = TradZorglang()
>>> traducteur.zorglang("Hello world!")
'olleH dlrow!'
"""

import unittest
from zorglang import TradZorglang

class TestTraducteur(unittest.TestCase):

	def test_la_chaine_vide_est_traduite_en_chaine_vide(self):
		""" test la chaine vide est traduite en chaine vide """
		traducteur = TradZorglang()
		self.assertEqual("", traducteur.zorglang(""))

	def test_la_chaine_de_taille_1_reste_telle_quelle(self):
		""" test la chaine de taille 1 reste telle quelle """
		traducteur = TradZorglang()
		self.assertEqual("a", traducteur.zorglang("a"))

	def test_la_chaine_de_un_mot_est_inversee(self):
		""" test la chaine de un mot est inversee """
		traducteur = TradZorglang()
		self.assertEqual("esrever", traducteur.zorglang("reverse"))

	def test_la_chaine_composee_de_deux_mots_simples(self):
		""" test la chaine composee de deux mots simples """
		traducteur = TradZorglang()
		self.assertEqual("olleH dlrow", traducteur.zorglang("Hello world"))

	def test_la_chaine_composee_de_deux_mots_avec_caracteres_speciaux(self):
		""" test la chaine composee de deux mots avec caracteres speciaux """
		traducteur = TradZorglang()
		self.assertEqual("olleH dlrow!", traducteur.zorglang("Hello world!"))

	def test_la_chaine_composee_de_trois_mots(self):
		""" test la chaine composee de trois mots """
		traducteur = TradZorglang()
		self.assertEqual("I ma tooR", traducteur.zorglang("I am Root"))