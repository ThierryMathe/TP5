from __future__ import annotations


class Flacon:
    """Modélisation d'un flacon de sirop avec gestion de la concentration
    d'eau et de sirop.

        Parameters
        ----------
        etiquette : str
            Description du flacon
        capacite : int
            capacité maximale du flacon
    """
    def __init__(self, etiquette: str, capacite: int):
        self.__etiquette = etiquette
        self.__capacite = capacite
        self.__volume: int | float = 0
        self.__concentration: float = 0

    @property
    def capacite(self):
        """Capacité maximale du flacon
        """
        return self.__capacite

    @property
    def volume(self):
        """Volume courrant contenu dans le flacon
        """
        return self.__volume

    @volume.setter
    def volume(self, volume):
        if not (isinstance(volume, (int, float))):
            raise ValueError("Le volume doit être un nombre.")
        if volume > self.__capacite:
            raise ValueError(
                f"Le volume donné:{volume} dépasse la capacité du flacon :{self.capacite}"
            )
        elif volume < 0:
            raise ValueError("Le volume doit être positif")
        self.__volume = volume

    @property
    def concentration(self):
        """Concentration de sirop dans le flacon
        """
        return self.__concentration

    @concentration.setter
    def concentration(self, valeur: float):
        if not (valeur >= 0 and valeur <= 1):
            raise ValueError("La concentration doit être comprise entre 0 et 1")
        self.__concentration = valeur

    def volume_sirop(self):
        """Donne le volume de sirop dilué dans le flacon
        """
        return self.volume * self.concentration

    def volume_eau(self):
        """Donne le volume d'eau diluant le sirop
        """
        return self.volume * (1 - self.concentration)

    def remplir(self, volume_sirop: float, volume_eau: float):
        try:
            self.volume += volume_sirop + volume_eau
            self.concentration((volume_sirop + self.volume_sirop()) / self.volume)
        except ValueError:
            return False
        return True

    def vider(self, volume: float) -> bool:
        try:
            self.volume -= volume
        except ValueError:
            return False
        return True

    def transvaser(self, autre: Flacon, volume: float):
        try:
            self.vider(volume)
        except ValueError:
            return False
        return autre.remplir(
            volume_sirop=volume * self.concentration,
            volume_eau=volume * (1 - self.concentration),
        )
