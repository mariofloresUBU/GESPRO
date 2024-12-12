from enumeraciones import COLOR 

class Pieza:
    def __init__(self, color):
        """
        Constructor que establece el color de la pieza.
        :param color: El color de la pieza, debe ser un valor de la enumeración COLOR.
        """
        if color not in COLOR:
            raise ValueError(f"El color debe ser un valor de la enumeración COLOR, recibido: {color}")
        self.color = color

    def devolver_color(self):
        """
        Devuelve el color de la pieza. 
        :return: El color de la pieza.
        """
        return self.color

    def __str__(self):
        """
        Representación en forma de cadena de la pieza.
        :return: El nombre del color de la pieza.
        """
        return f"Pieza({self.color.name})"
