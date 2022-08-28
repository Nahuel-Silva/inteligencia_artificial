import copy

class B_anchura():

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
        
        pos_fila0, pos_cero = B_anchura().posicion_cero(matriz)

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

        niveles = []
        matriz_cp = copy.deepcopy(matriz)

        for pos in posiciones_dis:
            matriz_cp[pos_fila0][pos_cero], matriz_cp[pos[0]][pos[1]] = matriz_cp[pos[0]][pos[1]], matriz_cp[pos_fila0][pos_cero]
            niveles.append(matriz_cp)
            matriz_cp = copy.deepcopy(matriz)
        
        return niveles
    
    def definitiva(self, matriz_r, matriz_o):

        niveles = B_anchura().movimientos_posibles(matriz_r)

        contador = 0
        lista_comun = []

        for j in niveles:
            lista_comun.append(j)

        for i in range(2):
            for matriz in niveles:
                niveles = B_anchura().movimientos_posibles(matriz)
                for i in niveles:
                    niveles = B_anchura().movimientos_posibles(i)
                    if i not in lista_comun:
                        lista_comun.append(i)
                
        #         if matriz == matriz_o:
        #             print(f"\nMatriz resultante: ")
        #             for fila in matriz:
        #                 print(fila)
        #             print(f"Numero de niveles que se hicieron{contador}")
        #             break
            