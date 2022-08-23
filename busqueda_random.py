import random


class B_random():

    def posicion_cero(self, matriz_r):

        pos_fila0 = 0

        for fila in matriz_r:
            pos_fila0 += 1
            for pos in fila:
                if pos == 0:
                    pos_fila0 = pos_fila0 - 1
                    pos_cero = matriz_r[pos_fila0].index(0)     
                    return pos_fila0, pos_cero
    
    def movimientos_posibles(self, matriz):
        
        pos_fila0, pos_cero = B_random().posicion_cero(matriz)

        posiciones_dis = []

        cant_filas = len(matriz)

        if (pos_fila0 + 1) < cant_filas:
            posicion = ((pos_fila0+1) , pos_cero)
            posiciones_dis.append(posicion)
        if (pos_fila0 - 1) >= (cant_filas-cant_filas):
            posicion = ((pos_fila0-1) , pos_cero)
            posiciones_dis.append(posicion)
        if (pos_cero + 1) < cant_filas:
            posicion = (pos_fila0, (pos_cero+1))
            posiciones_dis.append(posicion)
        if (pos_cero - 1) >= (cant_filas-cant_filas):
            posicion = (pos_fila0, (pos_cero-1))
            posiciones_dis.append(posicion)

        pos_random = random.choice(posiciones_dis)

        for pos in posiciones_dis:
            if pos_random == pos:
                matriz[pos_fila0][pos_cero], matriz[pos_random[0]][pos_random[1]] = matriz[pos_random[0]][pos_random[1]], matriz[pos_fila0][pos_cero]

        return matriz

    def definitiva(self, matriz_r, matriz_o):

        contador = 0

        while True:
            matriz_armada = B_random().movimientos_posibles(matriz_r)
            contador += 1
            if matriz_armada == matriz_o:
                print(f"\nMatriz resultante: ")
                for fila in matriz_armada:
                    print(fila)
                print(f"Numero de movimientos necesarios {contador}")
                break
            
        

        
