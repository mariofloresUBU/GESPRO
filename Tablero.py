from direccion import Direccion
from celda import Celda

class Tablero:

    def __init__(self, filas, columnas ):
        """
        Constructor del tipo Tablero.
        :param filas: filas con las que se creará el tablero.
        :param columnas: columnas con las que se creará el tablero.
        """
        self.matriz = [[Celda(fila, columna) for columna in range(columnas)] for fila in range(filas)]

    def imprimir(self):
        """
        Imprime por pantalla el tablero
        :return: texto que imprime el tablero.
        """
        tablero = ""
        for fila in self.matriz:
            tablero += "\n"
            for celda in fila:
                tablero += celda.devolverFicha().devolver_color().toString()
        print(tablero)

    def estaCompleto(self):
        """
        Devuelve True si está completo de fichas o False si no.
        :return: valor booleano.
        """
        completo = True
        for fila in self.matriz:
            for celda in fila:
                if not celda.esta_vacia():
                    completo = False
                    break
        return completo

    def contarPiezasConsecutivas(self, coordenada, direccion):
        """
        Cuenta las piezas consecutivas de un mismo color que hay en una dirección a partir de una coordenada.
        Para cada dirección llama a una función auxiliar.
        :param coordenada: desde la que queremos empezar a comprobar.
        :param direccion: que queremos comprobar.
        :return: valor entero
        """
        piezasConsecutivas = 0
        if direccion == Direccion.DIAGONAL_NO_SE:
            piezasConsecutivas = self.contarPiezasConsecutivasNoSe(coordenada)
        elif direccion == Direccion.DIAGONAL_SO_NE:
            piezasConsecutivas = self.contarPiezasConsecutivasSoNe(coordenada)
        elif direccion == Direccion.HORIZONTAL:
            piezasConsecutivas = self.contarPiezasConsecutivasHORIZONTAL(coordenada)
        elif direccion == Direccion.VERTICAL:
            piezasConsecutivas = self.contarPiezasConsecutivasVERTICAL(coordenada)
        return piezasConsecutivas

    def contarPiezasConsecutivasHORIZONTAL(self, coordenada):
        """
        Cuenta las piezas consecutivas de un mismo color que hay en la dirección Horizontal
        :param coordenada: desde la que queremos empezar a comprobar.
        :return: valor entero
        """
        fila = coordenada.obtenerFila()
        columna = coordenada.obtenerColumna()
        piezasConsecutivas = 0

        if not self.matriz[fila][columna].esta_vacia():
            color = self.matriz[fila][columna].devolverFicha().DevolverColor()
        else: return piezasConsecutivas

        for i in range(columna, len(self.matriz[0])):
            if not self.matriz[fila][i].esta_vacia() and self.matriz[fila][i].devolverFicha().DevolverColor() == color:
                piezasConsecutivas += 1
            else: break
        if self.perteneceASusDimensiones(fila, columna - 1):
            for i in range(columna - 1, -1, -1):
                if not self.matriz[fila][i].esta_vacia() and self.matriz[fila][i].devolverFicha().DevolverColor() == color:
                    piezasConsecutivas += 1
                else: break
        return piezasConsecutivas

    def contarPiezasConsecutivasVERTICAL(self, coordenada):
        fila = coordenada.obtenerFila()
        columna = coordenada.obtenerColumna()
        piezasConsecutivas = 0

        if not self.matriz[fila][columna].esta_vacia():
            color = self.matriz[fila][columna].devolverFicha().DevolverColor()
        else: return piezasConsecutivas

        for i in range(fila, len(self.matriz[0])):
            if not self.matriz[i][columna].esta_vacia() and self.matriz[i][columna].devolverFicha().DevolverColor() == color:
                piezasConsecutivas += 1
            else: break
        if self.perteneceASusDimensiones(fila - 1, columna):
            for i in range(fila - 1, -1, -1):
                if not self.matriz[i][columna].esta_vacia() and self.matriz[i][columna].devolverFicha().DevolverColor() == color:
                    piezasConsecutivas += 1
                else: break
        return piezasConsecutivas

    def contarPiezasConsecutivasSoNe(self, coordenada):
        fila = coordenada.obtenerFila()
        columna = coordenada.obtenerColumna()
        piezasConsecutivas = 0

        if not self.matriz[fila][columna].esta_vacia():
            color = self.matriz[fila][columna].devolverFicha().DevolverColor()
        else: return piezasConsecutivas

        i = fila
        j = columna
        while i >= 0 and j < len(self.matriz[0]):
            if not self.matriz[i][j].esta_vacia() and self.matriz[i][j].devolverFicha().DevolverColor() == color:
                piezasConsecutivas += 1
            else: break
        i -= 1
        j += 1

        if self.perteneceASusDimensiones(fila + 1, columna - 1):
            i = fila + 1
            j = columna - 1
            while i <= len(self.matriz) and j >= 0:
                if not self.matriz[i][j].esta_vacia() and self.matriz[i][j].devolverFicha().DevolverColor() == color:
                    piezasConsecutivas += 1
                else: break
                i += 1
                j -= 1
        return piezasConsecutivas

    def contarPiezasConsecutivasNoSe(self, coordenada):
        fila = coordenada.obtenerFila()
        columna = coordenada.obtenerColumna()
        piezasConsecutivas = 0

        if not self.matriz[fila][columna].esta_vacia():
            color = self.matriz[fila][columna].devolverFicha().DevolverColor()
        else: return piezasConsecutivas

        i = fila
        j = columna
        while i < len(self.matriz) and j < len(self.matriz[0]):
            if not self.matriz[i][j].esta_vacia() and self.matriz[i][j].devolverFicha().DevolverColor() == color:
                piezasConsecutivas += 1
            else: break
        i += 1
        j += 1

        if self.perteneceASusDimensiones(fila - 1, columna - 1):
            i = fila - 1
            j = columna - 1
            while i >= 0 and j >= 0:
                if not self.matriz[i][j].esta_vacia() and self.matriz[i][j].devolverFicha().DevolverColor() == color:
                    piezasConsecutivas += 1
                else: break
                i -= 1
                j -= 1
        return piezasConsecutivas

    def perteneceASusDimensiones(self, fila, columna):
        """
        Verifica si las coordenadas (fila, columna) están dentro de las dimensiones del tablero.
        """
        return 0 <= fila < len(self.matriz) and 0 <= columna < len(self.matriz[0])

    def colocar(self, pieza, coordenada):
        """
        Ubica la pieza en la coordenada seleccionada.
        """
        if pieza and self.perteneceASusDimensiones(coordenada):
            self.matriz[coordenada.fila][coordenada.columna].establecer_pieza(pieza)

    def consultar_numero_filas(self):
        """
        Devuelve la cantidad de filas.
        """
        return len(self.matriz)

    def consultar_numero_columnas(self):
        """
        Devuelve la cantidad de columnas.
        """
        return len(self.matriz[0])

    def obtener_celda(self, coordenada):
        """
        Devuelve la celda correspondiente a la coordenada recibida.
        """
        if self.perteneceASusDimensiones(coordenada):
            return self.matriz[coordenada.fila][coordenada.columna]
        return None
























