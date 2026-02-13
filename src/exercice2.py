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
    def etiquette(self):
        """Etiquette du flacon"""
        return self.__etiquette

    @property
    def capacite(self):
        """Capacité maximale du flacon"""
        return self.__capacite

    @property
    def volume(self):
        """Volume courrant contenu dans le flacon"""
        return self.__volume

    def __set_volume(self, volume):
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
        """Concentration de sirop dans le flacon"""
        return self.__concentration


    def __set_concentration(self, valeur: float):
        if not (valeur >= 0 and valeur <= 1):
            raise ValueError("La concentration doit être comprise entre 0 et 1")
        self.__concentration = valeur

    def volume_sirop(self):
        """Donne le volume de sirop dilué dans le flacon"""
        return self.volume * self.concentration

    def volume_eau(self):
        """Donne le volume d'eau diluant le sirop"""
        return self.volume * (1 - self.concentration)

    def remplir(self, volume_sirop: float, volume_eau: float) -> bool:
        """Rempli le flacon

        Parameters
        ----------
        volume_sirop : float
            volume de sirop ajouté
        volume_eau : float
            volume d'au ajouté

        Returns
        -------
        bool
            Indique si l'opération a eu lieu: `True` si le flacon est rempli,
            `False` si non.
        """
        try:
            self.__set_volume(self.volume +  volume_sirop + volume_eau)
            self.__set_concentration((volume_sirop + self.volume_sirop()) / self.volume)
        except ValueError:
            return False
        return True

    def vider(self, volume: float) -> bool:
        """Retire du flacon le volume de liquide indiqué

        Parameters
        ----------
        volume : float
            Volume à retirer

        Returns
        -------
        bool
            indique si l'opération s'est bien déroulée: `True` si le
            le volume a été retiré, `False` sinon.
        """
        try:
            self.__set_volume(self.volume - volume)
        except ValueError:
            return False
        return True

    def transvaser(self, autre: Flacon, volume: float) -> bool:
        """Transvase un le volume donné de liquite dans un autre
        flacon.

        Parameters
        ----------
        autre : Flacon
            flacon dans lequel le volume va être transvasé
        volume : float
            volume de liquite à transvaser.

        Returns
        -------
        bool
            Indique si l'opération s'est bien déroullée: `True` si
            le volume a été transvasé, `False` sinon.
        """
        try:
            self.vider(volume)
        except ValueError:
            return False
        return autre.remplir(
            volume_sirop = volume * self.concentration,
            volume_eau = volume * (1 - self.concentration),
        )

    def __str__(self):
        return f"Falcon {self.__etiquette}"
