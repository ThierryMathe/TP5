from __future__ import annotations

class Article:
    """Modélisatin d'un article avec stock

        Parameters
        ----------
        reference : int
            Référence de l'article
        intitule : str
            Nom de l'article
        prix_ht : float
            Prix hors taxes
        quantite_en_stock : int
            Quantité en stock
    """
    def __init__(self, reference: int, intitule: str, prix_ht:float, quantite_en_stock : int):
        self.__reference: int = reference
        self.__intitule: str = intitule
        self.__prix_ht: float = prix_ht
        self.__quantite_en_stock: int = quantite_en_stock

    def get_reference(self) -> int:
        """Donne la référence de l'article
        """
        return self.__reference
    
    def get_intitule(self) -> str:
        """Donne le nom de l'article
        """
        return self.__intitule
    
    def get_prix_ht(self) -> float:
        """Donne le prix hors taxe de l'article
        """
        return self.__prix_ht
    
    def get_quantite_en_stock(self) -> int:
        """Donne la quantité en stock de l'article
        """
        return self.__quantite_en_stock
    
    def approvisionner(self, quantite:int) -> None:
        """Ajoute la quantité donnée au stock de l'article

        Parameters
        ----------
        quantite : int
            Quantité  à ajouter au stock
        """
        self.__quantite_en_stock += int(quantite)

    def vendre(self, quantite: int) -> bool:
        """Retire la quantité données au stock de l'aricle est indique si 
        l'opération s'est bien déroulée.

        Parameters
        ----------
        quantite : int
            Quantité à retirer du stock

        Returns
        -------
        bool
            Renvoie `True` si l'opération s'est bien déroulée et `False` sinon.
            Le stock de l'article est alors inchangé.
        """
        if self.get_quantite_en_stock() > quantite:
            self.__quantite_en_stock -= quantite
            return True
        else:
            return False
        
    def prix_ttc(self):
        """Renvoie le prix de l'artique avec un taux de taxes de 20%"""
        return self.get_prix_ht() * 1.
    
    def __str__(self):
        return f"{self.get_intitule()} ({self.get_reference()}) : {self.get_prix_ht}€ HT."
    
    def __eq__(self, o: Article):
        return self.get_reference() == o.get_reference()
    
    def __lt__(self, o: Article):
        return self.get_quantite_en_stock() < o.get_quantite_en_stock()