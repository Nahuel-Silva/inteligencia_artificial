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

        contador = 0
        contador += 1
        niveles = []

        for pos in posiciones_dis:
            matriz[pos_fila0][pos_cero], matriz[pos[0]][pos[1]] = matriz[pos[0]][pos[1]], matriz[pos_fila0][pos_cero]
        #     niveles.append(matriz)
        # print(niveles)

        # arbol = {contador:niveles}
        # print(arbol)
        
        # return arbol
    
    # def definitiva(self, matriz_r, matriz_o):

    #     arbol = B_anchura().movimientos_posibles(matriz_r)

    #     print(arbol)

        # for matriz in arbol.values:
        #     arbol = B_anchura().movimientos_posibles(matriz)
        
        # print(arbol)

        # contador = 0

        # while True:
        #     matriz_armada = B_anchura().movimientos_posibles(matriz_r)
        #     contador += 1

            # if matriz_armada == matriz_o:
            #     print(f"\nMatriz resultante: ")
            #     for fila in matriz_armada:
            #         print(fila)
            #     print(f"Numero de movimientos necesarios {contador}")
            #     break
            