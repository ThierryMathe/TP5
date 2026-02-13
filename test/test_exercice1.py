import pytest
from src.exercice1 import Article

@pytest.fixture
def bouteille_de_lait() -> Article:
    return Article(
        1,
        "Bouteille de lait 1l",
        prix_ht= 2.1,
        quantite_en_stock= 25
    )

@pytest.mark.parametrize(
    "valeur, valeur_attendu",
    [(2, 27),
    (10, 35),
    (-5,25)]

)
def test_approvisionne(bouteille_de_lait,valeur, valeur_attendu):
    bouteille_de_lait.approvisionner(valeur)
    assert bouteille_de_lait.get_quantite_en_stock() == valeur_attendu
