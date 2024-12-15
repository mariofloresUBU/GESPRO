class Celda:
    def __init__(self, pieza=None):
        # Inicializa el atributo 'pieza' con el valor proporcionado o None por defecto
        self.pieza = pieza

    def obtener_pieza(self):
        """
        Método que devuelve una pieza.

        @return: devuelve una pieza.
        """
        # Devuelve el valor del atributo 'pieza' de la instancia actual de 'Celda'
        return self.pieza