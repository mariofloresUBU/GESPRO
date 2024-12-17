
class Tablero:

    def __init__(self, filas, columnas ):
        self.matriz = [[Celda(fila, columna) for columna in range(columnas)] for fila in range(filas)]

    def imprimir(self):
        tablero = ""
        for fila in self.matriz:
            tablero += "\n"
            for celda in fila:
                tablero += celda.devolverFicha().devolver_color().toString()
        print(tablero)

    def estaCompleto(self):
        completo = True
        for fila in self.matriz:
            for celda in fila:
                if not celda.estaVacia():
                    completo = False
                    break
        return completo

    def contarPiezasConsecutivas(self, coordenada, direccion):
        piezasConsecutivas = 0
        if direccion == Direccion.DIAGONAL_NO_SE:
            piezasConsecutivas = contarPiezasConsecutivasDIAGONAL_NO_SE(coordenada, direccion)
        else if direccion == Direccion.DIAGONAL_SO_NE:
            piezasConsecutivas = contarPiezasConsecutivasDIAGONAL_SO_NE(coordenada, direccion)
        else if direccion == Direccion.HORIZONTAL:
            piezasConsecutivas = contarPiezasConsecutivasHORIZONTAL(coordenada, direccion)
        else if direccion == Direccion.VERTICAL:
            piezasConsecutivas = contarPiezasConsecutivasVERTICAL(coordenada, direccion)
        return piezasConsecutivas

    def contarPiezasConsecutivasHORIZONTAL(self, coordenada):
        fila = coordenada.obtenerFila()
        columna = coordenada.obtenerColumna()
        piezasConsecutivas = 0

        if not self.matriz[fila][columna].estaVacia():
            color = self.matriz[fila][columna].devolverFicha().DevolverColor()
        else return: piezasConsecutivas

        for i in range(columna, len(self.matriz[0])):
            if not self.matriz[fila][i].estaVacia() and self.matriz[fila][i].devolverFicha().DevolverColor() == color:
                piezasConsecutivas += 1
            else: break
        if perteneceASusDimensiones(fila, columna - 1):
            for i in range(columna - 1, -1, -1):
                if not self.matriz[fila][i].estaVacia() and self.matriz[fila][i].devolverFicha().DevolverColor() == color:
                    piezasConsecutivas += 1
                else: break
        return piezasConsecutivas

    def contarPiezasConsecutivasVERTICAL(self, coordenada):
        fila = coordenada.obtenerFila()
        columna = coordenada.obtenerColumna()
        piezasConsecutivas = 0

        if not self.matriz[fila][columna].estaVacia():
            color = self.matriz[fila][columna].devolverFicha().DevolverColor()
        else: return piezasConsecutivas

        for i in range(fila, len(self.matriz[0])):
            if not self.matriz[i][columna].estaVacia() and self.matriz[i][columna].devolverFicha().DevolverColor() == color:
                piezasConsecutivas += 1
            else: break
        if perteneceASusDimensiones(fila - 1, columna):
            for i in range(fila - 1, -1, -1):
                if not self.matriz[i][columna].estaVacia() and self.matriz[i][columna].devolverFicha().DevolverColor() == color:
                    piezasConsecutivas += 1
                else: break
        return piezasConsecutivas

    def contarPiezasConsecutivasSoNe(self, coordenada):
        fila = coordenada.obtenerFila()
        columna = coordenada.obtenerColumna()
        piezasConsecutivas = 0

        if not self.matriz[fila][columna].estaVacia():
            color = self.matriz[fila][columna].devolverFicha().DevolverColor()
        else: return piezasConsecutivas

        i = fila
        j = columna
        while i >= 0 and j < len(self.matriz[0]):
            if not self.matriz[i][j].estaVacia() and self.matriz[i][j].devolverFicha().DevolverColor() == color:
                piezasConsecutivas += 1
            else: break
        i -= 1
        j += 1

        if perteneceASusDimensiones(fila + 1, columna - 1):
            i = fila + 1
            j = columna - 1
            while i <= len(self.matriz) and j >= 0:
                if not self.matriz[i][j].estaVacia() and self.matriz[i][j].devolverFicha().DevolverColor() == color:
                    piezasConsecutivas += 1
                else: break
                i += 1
                j -= 1
        return piezasConsecutivas

    def contarPiezasConsecutivasNoSe(self, coordenada):
        fila = coordenada.obtenerFila()
        columna = coordenada.obtenerColumna()
        piezasConsecutivas = 0

        if not self.matriz[fila][columna].estaVacia():
            color = self.matriz[fila][columna].devolverFicha().DevolverColor()
        else: return piezasConsecutivas

        i = fila
        j = columna
        while i < len(self.matriz) and j < len(self.matriz[0]):
            if not self.matriz[i][j].estaVacia() and self.matriz[i][j].devolverFicha().DevolverColor() == color:
                piezasConsecutivas += 1
            else: break
        i += 1
        j += 1

        if perteneceASusDimensiones(fila - 1, columna - 1):
            i = fila - 1
            j = columna - 1
            while i >= 0 and j >= 0:
                if not self.matriz[i][j].estaVacia() and self.matriz[i][j].devolverFicha().DevolverColor() == color:
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
        if pieza and self.perteneceASusDimensiones(coordenada):
            self.matriz[coordenada.fila][coordenada.columna].establecer_pieza(pieza)
        """
               Ubica la pieza en la coordenada seleccionada.
        """
    def consultar_numero_filas(self):
        return len(self.matriz)
        """
               Devuelve la cantidad de filas.
        """
    def consultar_numero_columnas(self):
        return len(self.matriz[0])
        """
               Devuelve la cantidad de columnas.
        """
    def obtener_celda(self, coordenada):
        if self.perteneceASusDimensiones(coordenada):
            return self.matriz[coordenada.fila][coordenada.columna]
        """
               Devuelve la celda correspondiente a la coordenada recibida.
               """
        return None
























