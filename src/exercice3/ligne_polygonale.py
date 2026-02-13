from src.exercice3.point import Point, nb

class LignePolygonale:
    def __init__(self, sommets: list[Point]):
        if not all([isinstance(e, Point) for e in sommets]):
            raise TypeError("sommets ne doit contenir que des Points.")
        if len(sommets)<2:
            raise ValueError("sommets doit comporter au moins deux Point")
        self.__sommets = sommets
        self.__nb_sommets = len(sommets)

    @property
    def nb_sommets(self):
        return self.__nb_sommets

    def get_sommet(self, i: int) -> Point:
        return self.__sommets[i]

    def set_sommet(self, i:int, p: Point):
        self.__sommets[i] = p

    def homothetie(self, k : nb):
        for i in range(len(self)):
            self.get_sommet(i).homothetie(k)

    def translation(self, dx: nb, dy: nb):
        for p in self.__sommets:
            p.translation(dx, dy)

    def rotation(self, a : nb):
        for p in self.__sommets:
            p.rotation(a)

    def __str__(self):
        return f"LignePolygonale:[{",".join([str(p) for p in self.__sommets])}]"

    def __len__(self):
        return len(self.__sommets)
