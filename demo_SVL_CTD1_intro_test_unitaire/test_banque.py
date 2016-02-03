"""
Test banque
demo SVL CTD1 - M. Nebut - 1516
"""
# que teste-t-on ?
# - création d'un compte
#   * avec solde nul
#   * avec solde paramétré 
# - crediter
#   * cas nominal : mettre à jour le solde
#   * cas exceptionnel : montant negatif
#   * cas limite / aux bornes : montant nul
# - debiter
# - consultation solde : non

import unittest
from banque import Compte
from banque import MontantIncorrectError

class TestCreationCompte(unittest.TestCase):

    def test_un_compte_est_cree_avec_solde_nul(self):
        compte = Compte()
        self.assertEqual(compte.solde, 0.0)

class TestCrediterCompte(unittest.TestCase):
    
    def test_crediter_un_compte_augmente_son_solde(self):
        """crediter un compte met a jour son solde"""
        compte = Compte()
        compte.crediter(20.0)
        self.assertEqual(compte.solde, 20.0)

    def test_le_montant_est_positif(self):
        compte = Compte()
        #compte.crediter(-10.0)
        self.assertRaises(MontantIncorrectError,
                          compte.crediter,
                          -10.0)

    def test_on_peut_crediter_plusieurs_fois(self):
        compte = Compte()
        compte.crediter(10.0)
        compte.crediter(30.0)
        self.assertEqual(compte.solde, 40.0)

    def test_le_montant_est_strictement_positif(self):
        compte = Compte()
        self.assertRaises(MontantIncorrectError,
                          compte.crediter,
                          0.0)
        
# si exec des tests directement par python3            
#if __name__ == '__main__':
#    unittest.main()
