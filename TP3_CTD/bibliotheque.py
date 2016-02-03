"""
PETIT Antoine & WISSOCQ Sarah

Test Bibliotheque
"""

class ServiceEmprunt():

	def __init__(self):
		pass

	def emprunter(self,livre,membre):
		if not livre.est_empruntable():
			raise LivreNonEmpruntable()
		raise QuotaAtteintError()

class LivreNonEmpruntable(Exception):
	pass

class QuotaAtteintError(Exception):
	pass

class Livre :
	"""
	>>> livre = Livre()
	>>> livre.est_empruntable()
	True
	"""
	pass

class Membre :
	pass