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