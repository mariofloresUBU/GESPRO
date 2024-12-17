from enum import Enum

class Coordenada(Enum):
    """
    enumeracion que representa las coordenadas para un juego de tres en raya.
    """
    FILA_0_COLUMNA_0 = (0, 0)
    FILA_0_COLUMNA_1 = (0, 1)
    FILA_0_COLUMNA_2 = (0, 2)
    FILA_1_COLUMNA_0 = (1, 0)
    FILA_1_COLUMNA_1 = (1, 1)
    FILA_1_COLUMNA_2 = (1, 2)
    FILA_2_COLUMNA_0 = (2, 0)
    FILA_2_COLUMNA_1 = (2, 1)
    FILA_2_COLUMNA_2 = (2, 2)

    def obtener_coordenada(self):
        """
        metodo para obtener el valor de la coordenada.
        
        @return: devuelve la tupla (fila, columna).
        """
        return self.value
