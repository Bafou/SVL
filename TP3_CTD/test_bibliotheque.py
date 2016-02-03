"""
PETIT Antoine & WISSOCQ Sarah

Test Bibliotheque

emprunter un livre
 - si le livre n'est que consultable l'emprunt échoue
 - si le membre a atteint son quota l'emprunt échoue
 - sinon un emprunt est créé et disponible pour affichage

rendre un livre
 - le livre est bien rendu
 - si le membre a depasse les 30 jours alors signale au service litige
"""

import unittest
from mockito import *
from bibliotheque import *

class TestEmprunterUnLivre(unittest.TestCase):
    def setUp(self):
        self.livre=mock()
        self.membre = mock()
        self.fabrique_emprunts = mock()
        self.fabrique_litiges = mock()
        self.service_emprunts = ServiceEmprunt(self.fabrique_emprunts,self.fabrique_litiges)

    def test_livre_consultable_uniquement_l_emprunt_echoue(self):
        when(self.livre).est_empruntable().thenReturn(False)
        self.assertRaises(LivreNonEmpruntableError,self.service_emprunts.emprunter,self.livre,self.membre)
        

    def test_le_membre_a_atteint_son_quota_l_emprunt_echoue(self):
        when(self.livre).est_empruntable().thenReturn(True)
        when(self.membre).peut_emprunter().thenReturn(False)
        self.assertRaises(QuotaAtteintError,self.service_emprunts.emprunter,self.livre,self.membre)
        
    def test_l_emprunt_est_cree(self):
        when(self.livre).est_empruntable().thenReturn(True)
        when(self.membre).peut_emprunter().thenReturn(True)
        emprunt = mock()
        when(self.fabrique_emprunts).creer_emprunt(self.livre, self.membre).thenReturn(emprunt)
        self.assertEqual(self.service_emprunts.emprunter(self.livre,self.membre), emprunt)
        
class TestRendreUnLivre(unittest.TestCase):
    def setUp(self):
        self.livre=mock()
        self.membre = mock()
        self.fabrique_emprunts = mock()
        self.fabrique_litiges = mock()
        self.service_emprunts = ServiceEmprunt(self.fabrique_emprunts,self.fabrique_litiges)

    def test_livre_bien_rendu(self):
        self.service_emprunts.rendre(self.livre,self.membre)
        verify(self.membre).rendre(self.livre)

    def test_livre_plus_30_jours_creer_litige(self):
        when(self.membre).limiteDepasse(self.livre).thenReturn(True)
        litige=mock()
        when(self.fabrique_litiges).creer_litige(self.livre,self.membre).thenReturn(litige)
        self.assertEqual(self.service_emprunts.rendre(self.livre,self.membre), litige)

    def test_livre_plus_30_jours_livre_bien_rendu(self):
        when(self.membre).limiteDepasse(self.livre).thenReturn(True)
        self.service_emprunts.rendre(self.livre,self.membre)
        verify(self.membre).rendre(self.livre)