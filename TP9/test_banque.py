# CTD9 SVL - M. Nebut - 03/2016
# property-based testing

import unittest

from hypothesis import given, assume, example
from hypothesis.strategies import floats

from banque import *

class TestTomCrediteUnCompte(unittest.TestCase):

    def test_echec_si_somme_negative_classique(self):
        compte = Compte()
        self.assertRaises(ValueError,
                            compte.crediter,
                            -10)

    @given(somme=floats(max_value=0.0))
    @example(somme=0.0)
    def test_echec_si_somme_negative(self, somme):
        compte = Compte()
        self.assertRaises(ValueError,
                            compte.crediter,
                            somme)

    @given(somme=floats(min_value=0.0))
    #@example(somme=float("inf"))
    def test_le_solde_est_augmente(self, somme):
        compte = Compte()

        assume(somme > 0)
        
        compte.crediter(somme)
        self.assertEqual(compte.montant, somme)

class TestDebiterUnCompte(unittest.TestCase):

    @given(somme=floats(max_value=0.0))
    @example(somme=0.0)
    def test_echec_si_somme_negative(self, somme):
        compte = Compte()
        self.assertRaises(ValueError,
                            compte.debiter,
                            somme)

    @given(somme=floats(min_value=0.0))
    def test_le_solde_est_diminue(self, somme):
        compte = Compte()
        assume(somme > 0)
        compte.debiter(somme)
        self.assertEqual(compte.montant, -somme)