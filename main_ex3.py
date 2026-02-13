from src.exercice3.ligne_polygonale import Point, LignePolygonale
from math import pi
ligne = LignePolygonale([Point(0, 0), Point(1, 0), Point(1, 1), Point(1, 0)])

print(ligne)
print([ligne.get_sommet(i).r for i in range(len(ligne))])
ligne.rotation(pi/2)
print(ligne)
