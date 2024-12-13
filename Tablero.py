
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