from matriz import *
from busqueda_random import *

def main():

    cant_col = int(input("Cantidad de columnas? "))
    cant_fil = int(input("Cantidad de filas? "))
    num_mezcladas = int(input("Cuantas veces quiere mezclar las fichas? "))

    matriz_o = Matriz().armar_matriz(cant_col, cant_fil)
    # matriz_o = Matriz().matriz_np(cant_col, cant_fil)

    matriz_r = Matriz().matriz_random(cant_col, cant_fil, num_mezcladas)
    # Matriz().random_np(cant_col, cant_fil, num_mezcladas)

    B_random().busqueda_random(matriz_r, matriz_o)



if __name__ == '__main__':
    main()