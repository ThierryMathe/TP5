from src.exercice1 import Article

art1 = Article(reference= 12, intitule="un truc à vendre", prix_ht= 10.5, quantite_en_stock= 10)

print(art1)
print(art1.get_quantite_en_stock())
art1.approvisionner(5)
art1.vendre(8)
print(art1)
print(art1.get_quantite_en_stock())
art1.vendre(15)
print(art1.get_quantite_en_stock())
