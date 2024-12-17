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

def esta_vacia(self):
    """
    método que verifica si la celda está vacía.
    
    @return: true si la celda está vacía, false en caso contrario.
    """
    # compruebo si el atributo 'pieza' es none
    # devuelvo true si lo es, de lo contrario devuelvo false
    return self.pieza is None

