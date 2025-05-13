class Produits(object):
    liste_Produits=[]
    def __init__(self,nom: str,prix:float , qte_stock:int):
        self.nom = nom
        self.prix:float =prix
        self.qte_stock:int=0
        Produits.liste_Produits.append(self)
        

    def getnom(self)->str:
        return self.nom
    
    def getprix(self)->float:
        return self.prix

    def getstock(self)->int:
        return self.qte_stock
    
    def getliste(self)->[]:
        return self.liste_Produits
    
    def getallstock(self):
        liste_stock=[]
        for produits in self.liste_Produits :
            liste_stock.append(produits.qte_stock)
        return liste_stock

    def retire_stock(self):
        if self.qte_stock>0:
            self.qte_stock=self.qte_stock-1
        else:
            raise ValueError("qte_stock ")

    def ajout_stock(self,nb:int):
        if nb>0:
            self.qte_stock=self.qte_stock+int
        else:
            raise ValueError("nb<1")