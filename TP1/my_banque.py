"""
Banque
"""

class Compte():

	def __init__ (self):
		self.solde = [0.0]

	def crediter(self, montant):
		if montant <= 0:
			raise MontantIncorrectError()
		self.solde.append(montant)


class MontantIncorrectError(Exception):
	pass