from src.exercice3.ligne_polygonale import Point, LignePolygonale
from math import pi

ligne = LignePolygonale([Point(0, 0), Point(1, 0), Point(1, 1), Point(0,1)])
print(ligne)
ligne.rotation(pi/2)
print(ligne)
ligne.homothetie(2)
print(ligne)
ligne.translation(1,-1)
print(ligne)
ligne.rotation(pi/2)
print(ligne)
