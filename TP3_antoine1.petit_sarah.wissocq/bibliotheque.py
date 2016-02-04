"""
PETIT Antoine & WISSOCQ Sarah

Test Bibliotheque
"""

class ServiceEmprunt:

    def __init__(self, les_emprunts, les_litiges):
        self.fabrique_emprunts = les_emprunts
        self.fabrique_litiges = les_litiges

    def rendre(self,livre,membre):
    	if not membre.limiteDepasse(livre):
       		membre.rendre(livre)
    	else:
    		membre.rendre(livre)
    		return self.fabrique_litiges.creer_litige(livre,membre)	

    def emprunter(self, livre, membre):
        if not livre.est_empruntable():
            raise LivreNonEmpruntableError()
        if not membre.peut_emprunter():
            raise QuotaAtteintError()
        # emprunt = Emprunt(livre, membre)
        # JAMAIS ! SURTOUT PAS !
        return self.fabrique_emprunts.creer_emprunt(livre, membre)

class LivreNonEmpruntableError(Exception):
    pass

class QuotaAtteintError(Exception):
    pass

class Livre:
    """
    >>> livre = Livre()
    >>> livre.est_empruntable()
    True
    """
    pass

class Membre:
    """
    >>> membre = Membre()
    >>> membre.peut_emprunter()
    True
    """
    pass

class FabriqueEmprunts:
    """
    Permet de créer des emprunts.
    >>> fabrique = FabriqueEmprunts()
    >>> livre = Livre()
    >>> membre = membre()
    >>> emprunt = fabrique.creer_emprunt(livre, membre)
    """
    pass

class FabriqueLitiges:
    """
    Permet de créer des litiges.
    """
    pass
