"""
PETIT Antoine & WISSOCQ Sarah

Test Restaurant Entreprise
"""

import unittest
from mockito import *
from restaurant_entreprise import *

class TestVisualiserSoldeCaisse(unittest.TestCase):

	def test_le_solde_est_celui_de_la_carte(self):
		caisse = Caisse()
		LE_SOLDE = 42
		carte = mock()
		when(carte).solde().thenReturn(LE_SOLDE)
		caisse.inserer_carte(carte)
		self.assertEqual(caisse.solde(), LE_SOLDE)

	def test_solde_pas_de_carte_erreur(self):
		caisse = Caisse()
		self.assertRaises(CarteManquanteError, caisse.solde)

class TestVisualiserNbTicketCaisse(unittest.TestCase):
	
	def test_le_nb_ticket_est_celui_de_la_carte(self):
		caisse = Caisse()
		NB_TICKET = 21
		carte = mock()
		when(carte).nb_ticket().thenReturn(NB_TICKET)
		caisse.inserer_carte(carte)
		self.assertEqual(caisse.nb_ticket(), NB_TICKET)

	def test_nb_ticket_pas_de_carte_erreur(self):
		caisse = Caisse()
		self.assertRaises(CarteManquanteError, caisse.nb_ticket)

class TestVisualiserValeurTicketCaisse(unittest.TestCase):

	def test_la_valeur_ticket_est_celle_de_la_carte(self):
		caisse = Caisse()
		VALEUR_TICKET = 7.50
		carte = mock()
		when(carte).valeur_ticket().thenReturn(VALEUR_TICKET)
		caisse.inserer_carte(carte)
		self.assertEqual(caisse.valeur_ticket(), VALEUR_TICKET)

	def test_la_valeur_ticket_pas_de_carte_erreur(self):
		caisse = Caisse()
		self.assertRaises(CarteManquanteError, caisse.valeur_ticket)

class TestPayerRepasSansTicketCaisse(unittest.TestCase):

	def test_caisse_debite_carte(self):
		caisse = Caisse()
		PRIX = 12
		carte = mock()
		caisse.inserer_carte(carte)
		caisse.payer_sans_ticket(PRIX)
		verify(carte).debiter(PRIX)

	def test_payer_sans_ticket_sans_carte_erreur(self):
		caisse = Caisse()
		PRIX = 12
		self.assertRaises(CarteManquanteError, caisse.payer_sans_ticket, PRIX)

	def test_caisse_debite_carte_solde_insuffisant_erreur(self):
		caisse = Caisse()
		PRIX = 12
		carte = mock()
		when(carte).debiter(PRIX).thenRaise(SoldeInsuffisantError)
		caisse.inserer_carte(carte)
		self.assertRaises(SoldeInsuffisantError, caisse.payer_sans_ticket, PRIX)

	def test_caisse_debite_carte_prix_invalide_erreur(self):
		caisse = Caisse()
		PRIX = -12
		carte = mock()
		when(carte).debiter(PRIX).thenRaise(PrixInvalideError)
		caisse.inserer_carte(carte)
		self.assertRaises(PrixInvalideError, caisse.payer_sans_ticket, PRIX)

class TestPayerRepasAvecTicketCaisse(unittest.TestCase):

	def test_payer_avec_uniquement_ticket(self):
		caisse = Caisse()
		PRIX = 10
		VALEUR_TICKET = 11
		carte = mock()
		when(carte).nb_ticket().thenReturn(3)
		when(carte).valeur_ticket().thenReturn(VALEUR_TICKET)
		caisse.inserer_carte(carte)
		caisse.payer_avec_ticket(PRIX)
		verify(carte).retirer_ticket()

	def test_payer_avec_ticket_sans_carte_erreur(self)	:
		caisse = Caisse()
		PRIX = 24
		self.assertRaises(CarteManquanteError, caisse.payer_avec_ticket, PRIX)

	def test_payer_avec_ticket_et_solde(self):
		caisse = Caisse()
		PRIX = 24
		VALEUR_TICKET = 11
		carte = mock()
		when(carte).nb_ticket().thenReturn(3)
		when(carte).valeur_ticket().thenReturn(VALEUR_TICKET)
		caisse.inserer_carte(carte)
		caisse.payer_avec_ticket(PRIX)
		verify(carte).retirer_ticket()
		verify(carte).debiter(PRIX - VALEUR_TICKET)

	def test_payer_avec_ticket_pas_ticket_erreur(self):
		caisse = Caisse()
		PRIX = 24
		VALEUR_TICKET = 11
		carte = mock()
		when(carte).nb_ticket().thenReturn(0)
		when(carte).valeur_ticket().thenReturn(VALEUR_TICKET)
		caisse.inserer_carte(carte)
		self.assertRaises(TicketInsuffisantError, caisse.payer_avec_ticket, PRIX )

	def test_payer_avec_ticket_et_solde_insuffisant_erreur(self):
		caisse = Caisse()
		PRIX = 24
		VALEUR_TICKET = 11
		carte = mock()
		when(carte).nb_ticket().thenReturn(3)
		when(carte).valeur_ticket().thenReturn(VALEUR_TICKET)
		when(carte).debiter(PRIX-VALEUR_TICKET).thenRaise(SoldeInsuffisantError)
		caisse.inserer_carte(carte)
		self.assertRaises(SoldeInsuffisantError, caisse.payer_avec_ticket, PRIX )

	def test_payer_prix_invalide_erreur(self):
		caisse = Caisse()
		PRIX = -24
		VALEUR_TICKET = 11
		carte = mock()
		when(carte).nb_ticket().thenReturn(3)
		when(carte).valeur_ticket().thenReturn(VALEUR_TICKET)
		when(carte).debiter(PRIX-VALEUR_TICKET).thenRaise(PrixInvalideError)
		caisse.inserer_carte(carte)
		self.assertRaises(PrixInvalideError, caisse.payer_avec_ticket, PRIX )

class TestCarte(unittest.TestCase):

	def test_solde_nul_par_defaut(self):
		carte = Carte()
		self.assertEqual(carte.solde,0)

	def test_solde_non_nul(self):
		MONTANT=485726
		carte=Carte(MONTANT)
		self.assertEqual(carte.solde, MONTANT)

	def test_nb_ticket_nul_par_defaut(self):
		carte = Carte()
		self.assertEqual(carte.nb_ticket,0)

	def test_crediter_nb_ticket(self):
		carte = Carte()
		NB_TICKET=4
		carte.ajouter_ticket(NB_TICKET)
		self.assertEqual(carte.nb_ticket, NB_TICKET)

	def test_crediter_plusieur_ticket(self):
		carte = Carte()
		NB_TICKET=4
		NB_TICKET2=6
		NB_TICKET_TOTAL=10
		carte.ajouter_ticket(NB_TICKET)
		carte.ajouter_ticket(NB_TICKET2)
		self.assertEqual(carte.nb_ticket, NB_TICKET_TOTAL)

	def test_valeur_ticket_nulle_par_defaut(self):
		carte = Carte()
		self.assertEqual(carte.valeur_ticket,0)

	def test_changer_valeur_ticket(self):
		carte = Carte()
		VALEUR_TICKET=5
		carte.changer_valeur_ticket(VALEUR_TICKET)
		self.assertEqual(carte.valeur_ticket,VALEUR_TICKET)

	def test_debiter_solde(self):
		carte=Carte(50)
		MONTANT= 10
		carte.debiter(MONTANT)
		self.assertEqual(carte.solde, 40)

	def test_debiter_solde_insuffisant_erreur(self):
		carte=Carte()
		MONTANT= 10
		self.assertRaises(SoldeInsuffisantError, carte.debiter,MONTANT)


