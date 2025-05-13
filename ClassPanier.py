from datetime import datetime

class Panier(object):

    def __init__(self,statut="",liste_produit=[]):
        self.datecrea = datetime.now()
        self.statut=statut
        self.liste_produit=liste_produit

 
    def setstatut(self,m:str):
        self.statut=m

    def setliste_produit(self,m:[]):
        self.statut=m