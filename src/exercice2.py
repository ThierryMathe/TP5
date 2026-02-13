
class Flacon:
    def __init__(self, etiquette: str, capacite: int):
        self.__etiquette = etiquette,
        self.__capacite = capacite
        self.__volume : int | float = 0
        self.__concentration : float = 0
    @property
    def capacite(self):
        return self.__capacite

    @property
    def volume(self):
        return self.__volume

    @property
    def concentration(self):
        return self.__concentration

    def volume_sirop(self):
        return self.volume * self.concentration

    def volume_eau(self):
        return self.volume * (1 - self.concentration)

    @volume.setter
    def volume(self, volume):
        if not(isinstance(volume, (int, float))):
            raise ValueError("Le volume doit être un nombre.")
        if volume > self.__capacite:
            raise ValueError(f"Le volume donné:{volume} dépasse la capacité du flacon :{self.capacite}")
        elif volume < 0:
            raise ValueError("Le volume doit être positif")
        self.__volume = volume

    def __set_concentration(self, valeur : float):
        if not(valeur >= 0 and valeur <= 1):
            raise ValueError("La concentration doit être comprise entre 0 et 1")
        self.concentration = valeur

    def remplir(self, volume_sirop: float, volume_eau: float):
        try:
            self.volume += (volume_sirop + volume_eau)
            self.__set_concentration((volume_sirop + self.volume_sirop()) / self.volume)

    def vider(self, volume: float) -> bool:
        try:
            self.volume -= volume
            return True
        except ValueError:
            return False
