from matriz import *
from busqueda_random2 import *

def main():

    cant_col = 3
    cant_fil = 3
    num_mezcladas = int(input("Cuantas veces quiere mezclar las fichas? "))

    matriz_o = Matriz().armar_matriz(cant_col, cant_fil)

    B_random().movimientos_posibles(matriz_o)

if __name__ == '__main__':
    main()