import random


class B_random():

    def posicion_cero(self, matriz_o):

        pos_fila0 = 0

        for fila in matriz_o:
            pos_fila0 += 1
            for pos in fila:
                if pos == 0:
                    pos_fila0 = pos_fila0 - 1
                    pos_cero = matriz_o[pos_fila0].index(0)     
                    return pos_fila0, pos_cero
    
    def movimientos_posibles(self, matriz):
        
        pos_fila0, pos_cero = B_random().posicion_cero(matriz)

        posiciones_dis = []

        cant_filas = len(matriz)

        if (pos_fila0 + 1) < 3:
            posicion = [matriz[pos_fila0 + 1], pos_cero]
            posiciones_dis.append(posicion)
        if (pos_fila0 - 1) >= 3:
            posicion = [matriz[pos_fila0 - 1], pos_cero]
            posiciones_dis.append(posicion)
        if (pos_cero + 1) < 3:
            posicion = [pos_fila0, matriz[pos_fila0][pos_cero + 1]]
            posiciones_dis.append(posicion)
        if (pos_cero - 1) >= 3:
            posicion = [pos_fila0, matriz[pos_fila0][pos_cero - 1]]
            posiciones_dis.append(posicion)

        print(posiciones_dis)
