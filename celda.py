# coding=utf-8
class Celda:
    def __init__(self, pieza=None):
        # Inicializa el atributo 'pieza' con el valor proporcionado o None por defecto
        """
                Constructor que inicializa la celda.
                :param pieza: Objeto de tipo Pieza o None si está vacía.
                :param fila: Coordenada de la fila (opcional).
                :param columna: Coordenada de la columna (opcional).
                """
        self.pieza = pieza
        self.fila = fila
        self.columna = columna

    def obtener_pieza(self):
        """
        Método que devuelve una pieza.

        @return: devuelve una pieza.
        """
        # Devuelve el valor del atributo 'pieza' de la instancia actual de 'Celda'
        return self.pieza

    def colocar_pieza(self, pieza):
        """
        Coloca una pieza en la celda.
        :param pieza: Objeto de tipo Pieza.
        """
        if self.esta_vacia():
            self.pieza = pieza
        else:
            raise ValueError("La celda ya contiene una pieza.")

    def esta_vacia(self):
        """
        Comprueba si la celda está vacía.
        :return: True si está vacía, False si contiene una pieza.
        """
        return self.pieza is None

    def devolver_coordenada(self):
        """
        Devuelve las coordenadas de la celda.
        :return: Una tupla (fila, columna), o None si no están definidas.
        """
        return (self.fila, self.columna)

    def devolver_ficha(self):
        """
        Devuelve la ficha colocada en la celda.
        :return: La ficha si existe, None si la celda está vacía.
        """
        return self.pieza

def esta_vacia(self):
    """
    método que verifica si la celda está vacía.
    
    @return: true si la celda está vacía, false en caso contrario.
    """
    # compruebo si el atributo 'pieza' es none
    # devuelvo true si lo es, de lo contrario devuelvo false
    return self.pieza is None

