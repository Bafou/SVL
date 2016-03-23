""" 
PETIT Antoine & WISSOCQ Sarah

Tours de Hanoi
"""



class Tour:
	"""
	Represente une tour des tours de Hanoi

	inv :
		forall([self.contenu[i] <= self.contenu[i-1] for i in range(1, len(self.contenu))])
	"""

	def __init__(self,nb_disques =0 ):
		"""
		pre:
			nb_disques >=0
		post:
			len(self.contenu) == nb_disques
		"""
		self.contenu =[]
		if nb_disques == 0 :
			return
		else :
			for i in xrange(nb_disques,0,-1):
				self.contenu.append(i)

	def retirer_disque(self):
		"""
		Retire le disque au sommet de la tour

		pre: 
			len(self.contenu) > 0
		post[self.contenu]:
			len(self.contenu) == len(__old__.self.contenu) -1
		"""
		return self.contenu.pop()

	def ajouter_disque(self,taille_disque):
		"""
		Ajoute le disque au sommet de la tour de Hanoi

		pre:
			self.contenu == [] or taille_disque < self.contenu[len(self.contenu)-1 ]
		post[self.contenu]:
			len(self.contenu) == len(__old__.self.contenu) + 1
		"""
		self.contenu.append(taille_disque)

	def est_vide(self):
		return self.contenu == []

	def sommet(self):
		"""
		pre:
			self.contenu != []
		"""
		return self.contenu[len(self.contenu) -1]

class Hanoi:
	"""
	Represente le jeu des tours de Hanoi

	"""

	def __init__(self,nb_disques):
		"""
		pre:
			nb_disques > 0
		post:
			len(self.tours) == 3
			self.tours[1].est_vide()
			self.tours[2].est_vide()
		"""
		self.tours = [0,0,0]
		self.tours[0] = Tour(nb_disques)
		self.tours[1] = Tour()
		self.tours[2] = Tour()
		

	def deplace_disque_A_vers_B(self,depart,arrive):
		"""
		pre: 
			depart >= 0
			arrive >= 0
			depart < 3
			arrive < 3
			depart != arrive
		"""
		self.tours[arrive].ajouter_disque(self.tours[depart].retirer_disque())

import contract
contract.checkmod(__name__)

if __name__ == '__main__':
    tourVide = Tour()
    tour = Tour(3)
    print tour.retirer_disque()
    tour.ajouter_disque(1)
    hanoi = Hanoi(3)
    hanoi.deplace_disque_A_vers_B(0,1)