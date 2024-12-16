from enum import Enum

class Color(Enum):
    ROJO = 1
    AZUL = 2

    def __str__(self):
        return self.name.lower()