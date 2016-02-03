"""
PETIT Antoine & WISSOCQ Sarah

Login
"""

class ServiceCreationUtilisateur():

	def __init__(self,fabrique):
		self.fabrique_utilisateur = fabrique

	def creer_utilisateur(self, nom, prenom, login):
		if len(login)> 8:
			raise LoginTropLongError()
		if len(login) == 0:
			raise LoginVideError()
		if len(nom) == 0:
			raise NomVideError()
		if len(prenom) == 0:
			raise PrenomVideError()
		if not login.islower():
			raise LoginMauvaisFormatError()
		if not prenom.isalpha():
			raise PrenomMauvaisFormatError()
		if not nom.isalpha():
			raise NomMauvaisFormatError()
		self.fabrique_utilisateur.creation_utilisateur(nom, prenom, login)


class LoginTropLongError(Exception):
	pass

class LoginMauvaisFormatError(Exception):
	pass

class NomMauvaisFormatError(Exception):
	pass

class PrenomMauvaisFormatError(Exception):
	pass

class LoginVideError(Exception):
	pass

class NomVideError(Exception):
	pass

class PrenomVideError(Exception):
	pass

class FabriqueUtilisateur():
	pass
