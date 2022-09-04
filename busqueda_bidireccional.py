import copy


class B_bidireccional():

    def __init__(self, tabla):
        self.tabla = tabla
        self.padre = None
        self.hijo = []

    def agrega_hijo(self, hijo):
        hijo.padre = self
        self.hijo.append(hijo)

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
        
        pos_fila0, pos_cero = self.posicion_cero(matriz)

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