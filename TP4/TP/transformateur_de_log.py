"""
Petit Antoine & Wissocq Sarah

Transformateur de log
"""
from datetime import datetime

class TransformateurDeLog():

	def __init__(self, lecteur, ecrivain):
		self.lecteur = lecteur
		self.ecrivain = ecrivain

	def filtrer_messages(self, list_messages):
		result = []
		for message in list_messages:
			if message.priorite() >= 5 :
				result.append(message)
		return result

	def transforme_log(self, log_entree, log_sortie):
		list_messages = self.lecteur.lire_log(log_entree)
		message_conserver = self.filtrer_messages(list_messages)
		self.ecrivain.ecrire_log(log_sortie, message_conserver)


class LecteurDeLog():
	"""
	On a fait le choix que les logs mauvais ne sont pas conserves, ce traitement pourrait etre remplace par la creation d'un fichier bad si on le souhaite
	"""
	def __init__(self, messageFactory):
		self.messageFactory = messageFactory
		
	def lire_log(self, log):
		result = []
		list_ligne = log.split("\n")
		for ligne in list_ligne:
			try :
				ligne_conservee = self.lire_une_ligne(ligne)
			except MessageMalFormateError:
				pass
			except MessageDateMalFormateError:
				pass
			except MessagePrioriteError:
				pass
			if ligne_conservee != None:
				result.append(ligne_conservee)
			ligne_conservee = None
		return result
	
	def lire_une_ligne(self,ligne):
		parties_message = ligne.split(",")
		if len(parties_message) != 3 :
			print ("MessageMalFormateError dans lire ligne")
			raise MessageMalFormateError
		try :
			date = datetime.strptime(parties_message[0].strip(),"%Y-%M-%d")
		except ValueError:
			print ("MessageDateMalFormateError dans lire ligne")
			raise MessageDateMalFormateError
		try :
			priorite = int(parties_message[1])
		except ValueError:
			print ("MessagePrioriteError dans lire ligne 1")
			raise MessagePrioriteError
		if priorite > 9 or priorite < 1:
			print ("MessagePrioriteError dans lire ligne 2")
			raise MessagePrioriteError
		texte = parties_message[2].strip()
		return self.messageFactory.creer_message(date, priorite, texte)
			

	
class Message():
	pass
	
class MessageFactory():
	pass
	
class MessageMalFormateError(Exception):
	pass
	
class MessageDateMalFormateError(Exception):
	pass
	
class MessagePrioriteError(Exception):
	pass
