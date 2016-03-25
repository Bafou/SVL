# CTD9 SVL - M. Nebut - 03/2016
# property-based testing

class Compte:

    def __init__(self):
        self.montant = 0
        
    def crediter(self, somme):
        if somme <= 0:
            raise ValueError()
        self.montant += somme

    def debiter(self, somme):
    	if somme <= 0:
    		raise ValueError()
    	self.montant -= somme