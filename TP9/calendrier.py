"""
Antoine PETIT & Sarah Wissocq
Calendrier
"""

class Calendrier():

	def __init__(self):
		pass

	def est_bissextile(self,annee):
		if (annee <= 0):
			raise ValueError()
		elif (annee % 400 == 0 ):
			return True
		elif (annee % 4 == 0) and (annee % 100 != 0) :
			return True
		else :
			return False

	def nb_jour(self, mois, annee):
		if (annee <= 0):
			raise ValueError()
		elif (mois <= 0):
			raise ValueError()
		elif (mois > 12):
			raise ValueError()
		if(mois == 2):
			if(self.est_bissextile(annee)):
				return 29
			else:
				return 28
		elif(mois==1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois ==12):
			return 31
		else:
			return 30

	def date_valide(self, jour, mois,annee):
		try:
			max_jour = self.nb_jour(mois,annee)
			return (jour >= 1 and jour <= max_jour)
		except ValueError : 
			return False
			
	def numero_jour_semaine(self, jour, mois, annee):
		if (not self date_valide(jour, mois, annee)):
			raise ValueError()
		ab = annee // 100
		cd = annee % 100
		k = ab // 4
		q = cd // 4
		if (mois == 1):
			if (self.est_bissextile(annee)):
				M = 3
			else :
				M = 4
		elif (mois == 2):
			if (self.est_bissextile(annee)):
				M = 6
			else :
				M = 0
		elif (mois == 3): 
			M = 0
		elif (mois == 4):
			M = 3
		elif (mois == 5):
			M = 5
		elif (mois == 6):
			M = 1
		elif (mois == 7):
			M = 3
		elif (mois == 8):
			M = 6
		elif (mois == 9):
			M = 2
		elif (mois == 10):
			M = 4
		elif (mois == 11) :
			M = 0
		elif (mois == 12) :
			M = 2
		 
		j = jour
		return (k+q+cd+M+j+2+5×ab) % 7
