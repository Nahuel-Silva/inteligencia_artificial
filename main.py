from matriz import *
from busqueda_random import *

def main():

    cant_col = 3
    cant_fil = 3
    num_mezcladas = int(input("Cuantas veces quiere mezclar las fichas? "))

    matriz_o = Matriz().armar_matriz(cant_col, cant_fil)
    # matriz_o = Matriz().matriz_np(cant_col, cant_fil)

    matriz_r = Matriz().matriz_random(cant_col, cant_fil, num_mezcladas)
    # Matriz().random_np(cant_col, cant_fil, num_mezcladas)

    print(f"Matriz deseada:" )
    for fila in matriz_o:
        print(fila)

    print(f"\nMatriz random:" )
    for fila in matriz_r:
        print(fila)

    B_random().definitiva(matriz_r, matriz_o)


if __name__ == '__main__':
    main()