"""
PETIT Antoine & WISSOCQ Sarah

Test Bibliotheque
"""

import unittest
from mockito import *
from bibliotheque import *

class TestEmprunterUnLivre(unittest.TestCase):

	def test_livre_consultable_uniquement_l_emprunt_echoue(self):
		livre = mock()
		membre = mock()
		when(livre).est_empruntable().thenReturn(False)
		service_emprunts = ServiceEmprunt()
		self.assertRaises(LivreNonEmpruntable,service_emprunts.emprunter,livre,membre)

	def test_le_membre_a_atteint_son_quota_l_emprunt_echoue(self):
		livre = mock()
		membre = mock()
		when(membre).peut_emprunter().thenReturn(False)
		service_emprunts = ServiceEmprunt()
		self.assertRaises(QuotaAtteintError,service_emprunts.emprunter,livre,membre)

	def test_l_emprunt_est_cree(self):
		livre = mock()
		membre = mock()
		when(livre).est_empruntable().thenReturn(True)
		when(membre).peut_emprunter.thenReturn(True)
		service_emprunts = ServiceEmprunt()
		emprunt = service_emprunts.emprunter(livre,membre)
