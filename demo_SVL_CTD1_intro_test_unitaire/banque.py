"""
Application bancaire : comptes
"""

class Compte():
    """
    Représentation d'un compte bancaire.

    On peut creer un compte avec solde nul.
    >>> compte = Compte()
    >>> compte.solde
    0.0

    On peut créditer un compte.
    >>> compte.crediter(10.0)
    >>> compte.crediter(50.0)
    >>> compte.solde
    60.0

    On ne peut pas créditer un montant négatif.
    >>> compte.crediter(-10.0)
    Traceback (most recent call last):
    ...
    banque.MontantIncorrectError
    """

    def __init__(self):
        """Cree un compte avec solde nul."""
        self.solde = 0.0

    def crediter(self, montant):
        if montant <= 0:
            raise MontantIncorrectError()
        self.solde += montant

class MontantIncorrectError(Exception):
    pass
