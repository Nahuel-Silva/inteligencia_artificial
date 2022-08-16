from matriz import *

def main():

    cant_col = int(input("Cantidad de columnas? "))
    cant_fil = int(input("Cantidad de filas? "))
    num_mezcladas = int(input("Cuantas veces quiere mezclar las fichas? "))


    matriz = Matriz().matriz_random(cant_col, cant_fil, num_mezcladas)
    # matriz = Matriz().random_np(cant_col, cant_fil, num_mezcladas)
    print(matriz)


if __name__ == '__main__':
    main()