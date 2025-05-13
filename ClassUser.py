from    ClassPanier import Panier
class User(object):

    def __init__(self,nom="",prenom="",code_postal=""):
        self.nom = nom
        self.prenom=prenom
        self.code_postal=code_postal
        

 




    def ajout_panier(self,Produits):
        Panier("Créer",liste_produit=[])
        liste_produit.append(Produits)

    def supprimer_panier(self,Produits):
        liste_produit.pop(liste_produit.index(Produits))

    def valider_panier(self):
        self.Panier.setstatut("Valider")

    def vider_panier(self):
        vide=[]
        self.Panier.setliste_produit(vide)

    
    def afficher_produit_en_stock(self):

    def rechercher_cp(self,cp):
        ret = []
        for contact in Carnet.liste:
            if contact.code_postal==cp:
                ret.append(contact)
        return ret

    def rechercher_nom(self,nom):
        pass


