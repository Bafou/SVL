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
		self.messageFactory = mock()
		self.lecteur = LecteurDeLog(self.messageFactory)
		
	def test_lecteur_message_vide_erreur(self):
		MESSAGE_VIDE=""
		self.assertRaises(MessageMalFormateError,self.lecteur.lire_une_ligne,MESSAGE_VIDE)

	def test_lecteur_message_mal_formate_trop_court_erreur(self):
		MESSAGE_MAL_FORMATE = "test"
		self.assertRaises(MessageMalFormateError,self.lecteur.lire_une_ligne,MESSAGE_MAL_FORMATE)
		
	def test_lecteur_message_date_mal_formate_erreur(self):
		MESSAGE_DATE_MAL_FORMATE = "25-12-2015, 5, erreur_date"
		self.assertRaises(MessageDateMalFormateError,self.lecteur.lire_une_ligne,MESSAGE_DATE_MAL_FORMATE)
		
	def test_lecteur_priorite_est_pas_un_entie(self):
		MESSAGE_PRIORITE_NON_ENTIE = "2015-12-25, a, erreur_priorité"
		self.assertRaises(MessagePrioriteError, self.lecteur.lire_une_ligne,MESSAGE_PRIORITE_NON_ENTIE)

	def test_lecteur_priorite_inferieur_a_1_erreur(self):
		MESSAGE_PRIORITE_INFERIEUR_UN = "2015-12-25, 0, erreur_priorité"
		self.assertRaises(MessagePrioriteError, self.lecteur.lire_une_ligne,MESSAGE_PRIORITE_INFERIEUR_UN)
		
	def test_lecteur_priorite_superieur_a_9_erreur(self):
		MESSAGE_PRIORITE_SUPERIEUR_NEUF = "2015-12-25, 10, erreur_priorité"
		self.assertRaises(MessagePrioriteError, self.lecteur.lire_une_ligne,MESSAGE_PRIORITE_SUPERIEUR_NEUF)	
	
	def test_lecteur_priorite_egal_a_9_retourne_objet(self):
		MESSAGE_CORRECT = "2015-12-25, 9, correct"
		message = mock()
		date = datetime.strptime("2015-12-25","%Y-%M-%d")
		priorite = 9
		texte = "correct"
		when(self.messageFactory).creer_message(date, priorite, texte).thenReturn(message)
		self.assertEqual(message, self.lecteur.lire_une_ligne(MESSAGE_CORRECT))
		
	def test_lecteur_priorite_egal_a_1_retourne_objet(self):
		MESSAGE_CORRECT = "2015-12-25, 1, correct"
		message = mock()
		date = datetime.strptime("2015-12-25","%Y-%M-%d")
		priorite = 1
		texte = "correct"
		when(self.messageFactory).creer_message(date, priorite, texte).thenReturn(message)
		self.assertEqual(message, self.lecteur.lire_une_ligne(MESSAGE_CORRECT))
	
	def test_message_correct_retourne_un_message(self):
		MESSAGE_CORRECT = "2015-12-25, 5, correct"
		message = mock()
		date = datetime.strptime("2015-12-25","%Y-%M-%d")
		priorite = 5
		texte = "correct"
		when(self.messageFactory).creer_message(date, priorite, texte).thenReturn(message)
		self.assertEqual(message, self.lecteur.lire_une_ligne(MESSAGE_CORRECT))
	
	def test_messages_conserves_si_correct(self):
		MESSAGES_CORRECT = "2015-12-25, 5, correct1 \n2016-02-05, 8, correct2"
		message1 = mock;
		message2 = mock;
		list_message = [message1,message2]
		date1 = datetime.strptime("2015-12-25","%Y-%M-%d")
		priorite1 = 5
		texte1 = "correct1"
		when(self.messageFactory).creer_message(date1, priorite1, texte1).thenReturn(message1)
		date2 = datetime.strptime("2016-02-05","%Y-%M-%d")
		priorite2 = 8
		texte2 = "correct2"
		when(self.messageFactory).creer_message(date2, priorite2, texte2).thenReturn(message2)
		self.assertEqual(list_message, self.lecteur.lire_log(MESSAGES_CORRECT))

	def test_messages_contenant_un_message_refuse_pour_priorite(self):
		MESSAGES_CORRECT = "2015-12-25, 5, correct1 \n2016-02-05, a, correct2"
		message1 = mock;
		message2 = mock;
		list_message = [message1]
		date1 = datetime.strptime("2015-12-25","%Y-%M-%d")
		priorite1 = 5
		texte1 = "correct1"
		when(self.messageFactory).creer_message(date1, priorite1, texte1).thenReturn(message1)
		date2 = datetime.strptime("2016-02-05","%Y-%M-%d")
		priorite2 = 8
		texte2 = "correct2"
		when(self.messageFactory).creer_message(date2, priorite2, texte2).thenReturn(message2)
		self.assertEqual(list_message, self.lecteur.lire_log(MESSAGES_CORRECT))
		
	def test_messages_contenant_un_message_refuse_pour_date(self):
		MESSAGES_CORRECT = "2015-12-25, 5, correct1 \n20-02-2015, 5, correct2"
		message1 = mock;
		message2 = mock;
		list_message = [message1]
		date1 = datetime.strptime("2015-12-25","%Y-%M-%d")
		priorite1 = 5
		texte1 = "correct1"
		when(self.messageFactory).creer_message(date1, priorite1, texte1).thenReturn(message1)
		date2 = datetime.strptime("2016-02-05","%Y-%M-%d")
		priorite2 = 8
		texte2 = "correct2"
		when(self.messageFactory).creer_message(date2, priorite2, texte2).thenReturn(message2)
		self.assertEqual(list_message, self.lecteur.lire_log(MESSAGES_CORRECT))
		
	def test_messages_contenant_un_message_refuse_pour_format(self):
		MESSAGES_CORRECT = "2015-12-25, 5, correct1 \n20-02-2015,  correct2"
		message1 = mock;
		message2 = mock;
		list_message = [message1]
		date1 = datetime.strptime("2015-12-25","%Y-%M-%d")
		priorite1 = 5
		texte1 = "correct1"
		when(self.messageFactory).creer_message(date1, priorite1, texte1).thenReturn(message1)
		date2 = datetime.strptime("2016-02-05","%Y-%M-%d")
		priorite2 = 8
		texte2 = "correct2"
		when(self.messageFactory).creer_message(date2, priorite2, texte2).thenReturn(message2)
		self.assertEqual(list_message, self.lecteur.lire_log(MESSAGES_CORRECT))
