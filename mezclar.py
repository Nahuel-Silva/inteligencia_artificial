from busqueda_random import *

class Mezclar():

    def mezclar_random(self, matriz, n_mezcladas):

        for i in range(n_mezcladas):
            matriz_desordenada = B_random().movimientos_posibles(matriz)

        print("\nMatriz random: ")
        for fila in matriz_desordenada:
            print(fila)

        return matriz_desordenada
