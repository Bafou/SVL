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
		return self.fabrique_utilisateur.creation_utilisateur(nom, prenom, login)

class ServiceCreationLogin():
	
	def __init__(self,bdd):
		self.base_de_donnees =bdd
		
	def creer_login(self, nom, prenom):
		if len(nom) <=8 :
			result = nom.lower()
		else :
			result = nom[:8].lower()
		if self.base_de_donnees.existe_deja(result):
			result = nom[:7].lower() + prenom[0].lower()
			if self.base_de_donnees.existe_deja(result):
				raise MethodeAEtBOnEchoueError()
		return result
		

class FabriqueUtilisateur():
	pass
	
class BaseDeDonne():
	pass

# Classes d'exception avec une exception specifique par probleme

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
	
class LoginDejaExistantError(Exception):
	pass

class MethodeAEtBOnEchoueError(Exception):
	pass

