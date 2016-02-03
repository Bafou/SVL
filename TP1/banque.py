"""
Banque
"""

class Compte():

	def __init__ (self, montant=0.0):
		self.solde = montant

	def crediter(self, montant):
		if montant <= 0:
			raise MontantIncorrectError()
		self.solde += montant

	def debiter(self, montant):
		if montant <= 0:
			raise MontantIncorrectError()
		if (self.solde - montant) < 0 :
			raise SoldeNegatifError()
		self.solde -= montant


class MontantIncorrectError(Exception):
	pass

class SoldeNegatifError(Exception):
	pass