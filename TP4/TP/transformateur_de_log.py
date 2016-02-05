"""
Petit Antoine & Wissocq Sarah

Transformateur de log
"""

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

#nosetests3 -v --with-coverage --cover-erase --cover-branches --cover-package=transformateur_de_log

class LecteurDeLog():
	"""
	next_msg(): Message
	"""
	pass

class Message():
	pass