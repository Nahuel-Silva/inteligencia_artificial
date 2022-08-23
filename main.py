from matriz import *
from busqueda_random import *
from mezclar import *

def main():

    # cant_fil = int(input("Cuantas filas quiere? "))
    # cant_col = int(input("Cuantas columnas quiere? "))
    # while cant_col != cant_fil:
    #     print("Se necesita que la matriz sea cuadrada ")
    #     cant_col = int(input("Cuantas columnas quiere? "))
    #     cant_fil = int(input("Cuantas filas quiere? "))
    #     if cant_col == cant_fil:
    #         cant_col = cant_col
    #         cant_fil = cant_fil
    #         break

    cant_fil = 3
    cant_col = 3
    num_mezcladas = int(input("Cuantas veces quiere mover las fichas para mezclar? "))

    matriz_o = Matriz().armar_matriz(cant_col, cant_fil)
    matriz_o2 = Matriz().armar_matriz(cant_col, cant_fil)

    matriz_r = Mezclar().mezclar_random(matriz_o, num_mezcladas)

    B_random().definitiva(matriz_r, matriz_o2)

if __name__ == '__main__':
    main()