"""
Petit Antoine & Wissocq Sarah

Test transformateur de log
"""

import unittest
from mockito import *
from transformateur_de_log import *

class TestTransformateurDeLog(unittest.TestCase):
	"""
	Scenarios a tester : 
		- le transformateur conserve un message de priorité strictement supérieur à 5
		- le transformateur conserve un message de priorité égal à 5
		- le transformateur ne conserve pas un message de priorité strictement inférieur à 5
		- le transformateur est capable de conserver les bons messages dans une liste de message
	"""

	def setUp(self):
		self.lecteur = mock()
		self.ecrivain = mock()
		self.transformateur = TransformateurDeLog(self.lecteur, self.ecrivain)

	def test_transformateur_conserve_message_priorite_superieur_a_5(self):
		PRIORITE_SUPERIEUR_A_5 = 7
		message_sup_a_5 = mock()
		list_messages = [message_sup_a_5]
		when(message_sup_a_5).priorite().thenReturn(PRIORITE_SUPERIEUR_A_5)
		self.assertEqual(list_messages,self.transformateur.filtrer_messages(list_messages))

	def test_transformateur_conserve_message_priorite_egal_a_5(self):
		PRIORITE_EGAL_A_5 = 5
		message_egal_a_5 = mock()
		list_messages = [message_egal_a_5]
		when(message_egal_a_5).priorite().thenReturn(PRIORITE_EGAL_A_5)
		self.assertEqual(list_messages,self.transformateur.filtrer_messages(list_messages))

	def test_transformateur_rejete_message_priorite_inferieur_a_5(self):
		PRIORITE_INFERIEUR_A_5 = 3
		message_inferieur_a_5 = mock()
		list_messages = [message_inferieur_a_5]
		when(message_inferieur_a_5).priorite().thenReturn(PRIORITE_INFERIEUR_A_5)
		self.assertEqual([],self.transformateur.filtrer_messages(list_messages))

	def test_transformateur_conserve_plusieurs_messages_avec_priorite_sup_a_5(self):
		PRIORITE_SUPERIEUR_A_5 = 8
		PRIORITE_INFERIEUR_A_5 = 2
		message1 = mock()
		message2 = mock()
		message3 = mock()
		when(message1).priorite().thenReturn(PRIORITE_SUPERIEUR_A_5)
		when(message2).priorite().thenReturn(PRIORITE_INFERIEUR_A_5)
		when(message3).priorite().thenReturn(PRIORITE_SUPERIEUR_A_5)
		list_messages = [message1, message2, message3]
		list_messages_attendu = [message1, message3]
		self.assertEqual(list_messages_attendu, self.transformateur.filtrer_messages(list_messages))

	def test_transformateur_transforme_lit_les_bons_logs_et_retourne_les_bons_logs(self):
		PRIORITE_SUPERIEUR_A_5 = 8
		PRIORITE_INFERIEUR_A_5 = 2
		log_entree = mock()
		log_sortie = mock()
		message1 = mock()
		message2 = mock()
		message3 = mock()
		when(message1).priorite().thenReturn(PRIORITE_SUPERIEUR_A_5)
		when(message2).priorite().thenReturn(PRIORITE_INFERIEUR_A_5)
		when(message3).priorite().thenReturn(PRIORITE_SUPERIEUR_A_5)
		list_messages = [message1, message2, message3]
		list_messages_attendu = [message1, message3]
		when(self.lecteur).lire_log(log_entree).thenReturn(list_messages)
		self.transformateur.transforme_log(log_entree,log_sortie)
		inorder.verify(self.lecteur).lire_log(log_entree)
		inorder.verify(self.ecrivain).ecrire_log(log_sortie, list_messages_attendu)


class TestLecteurDeLog(unittest.TestCase):
	"""
	Scenarios a tester :
		- le log a une date mal formatee et retourne une erreur
		- le log n'a pas un entie en deuxieme parametre et retourne une erreur
		- la priorite a une valeur incorrect et retourne une erreur
		- le log est mal forme de maniere general et retourne une erreur (nombre de virgule)
		- 
	"""

	def setUp(self):
		pass
