from math import sqrt, atan2, sin, cos

type nb = int | float


class Point:
    """_suMmmary_

    Parameters
    ----------
    x : nb
        _description_
    y : nb
        _description_
    """

    def __init__(self, x: nb, y: nb):

        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def r(self):
        return sqrt(self.x**2 + self.y**2)

    @property
    def t(self):
        return atan2(self.y, self.x)

    def homothetie(self, k: nb):
        self.__x = k * self.x
        self.__y = k * self.y

    def translation(self, dx: nb, dy: nb):
        self.__x = self.x + dx
        self.__y = self.y + dy

    def rotation(self, a: nb):
        r = self.r
        t = self.t
        self.__x = r * cos(t + a)
        self.__y = r * sin(t + a)

    def __str__(self):
        return f"({round(self.x,3)};{round(self.y,3)})"

    def __eq__(self, other: object):
        if not (isinstance(other, Point)):
            return NotImplemented
        return self.x == other.x and self.y == other.y
