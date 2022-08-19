
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

    def movimientos_posibles(self, matriz_r):

        pos_fila0, pos_cero = B_random().posicion_cero(matriz_r)

        if pos_fila0 == 0:
            if pos_cero == 0:
                pass

        # print(pos_cero)
        # print(pos_fila0)
        print(matriz_r)