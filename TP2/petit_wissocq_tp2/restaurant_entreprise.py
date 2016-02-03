"""
PETIT Antoine & WISSOCQ Sarah

Restaurant Entreprise
"""

class Caisse():
	
	def __init__(self):
		"""
		Creer une Caisse
		>>> caisse=Caisse()
		"""
		self.carte = None

	
	def inserer_carte(self, carte):
		"""
		Insere une Carte
		>>> caisse=Caisse()
		>>> carte=Carte()
		>>> caisse.inserer_carte(carte)
		"""
		self.carte=carte

	
	def solde(self):
		"""
		Visualise le solde
		>>> caisse=Caisse()
		>>> carte=Carte()
		>>> caisse.inserer_carte(carte)
		>>> caisse.solde()
		"""
		if self.carte == None :
			raise CarteManquanteError()
		return self.carte.solde()

	def nb_ticket(self):
		if self.carte == None :
			raise CarteManquanteError()
		return self.carte.nb_ticket()

	def valeur_ticket(self):
		if self.carte == None :
			raise CarteManquanteError()
		return self.carte.valeur_ticket()

	def payer_sans_ticket(self, prix):
		if self.carte == None :
			raise CarteManquanteError()
		self.carte.debiter(prix)

	def payer_avec_ticket(self, prix):
		if prix <= 0 :
			raise PrixInvalideError
		if self.carte == None :
			raise CarteManquanteError()
		if self.carte.nb_ticket() <= 0 :
			raise TicketInsuffisantError()
		if self.carte.valeur_ticket() < prix :
			self.carte.debiter(prix - self.carte.valeur_ticket())
		self.carte.retirer_ticket()


class CarteManquanteError(Exception):
	pass

class SoldeInsuffisantError(Exception):
	pass

class TicketInsuffisantError(Exception):
	pass

class PrixInvalideError(Exception):
	pass

class Carte():

	def __init__(self, montant=0):
		self.solde=montant
		self.nb_ticket=0
		self.valeur_ticket=0

	def ajouter_ticket(self, nbticket):
		self.nb_ticket+=nbticket

	def changer_valeur_ticket(self, new_val):
		self.valeur_ticket=new_val

	def debiter(self, montant):
		if self.solde-montant<0:
			raise SoldeInsuffisantError		
		self.solde-=montant

	def solde(self):
		return self.solde
