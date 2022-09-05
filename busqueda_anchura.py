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

        lista_comunes = []
        arbol = [[]]
        arbol2 = copy.deepcopy(arbol)
        arbol[0].append(matriz_r)
        lista_comunes.append(matriz_r)
        a = True
        while a == True:

            arbol_cp = copy.deepcopy(arbol)

            for matriz_nodo in arbol_cp:
                arbol.remove(matriz_nodo)
                m_nodo_cp = copy.deepcopy(matriz_nodo[-1])
                niveles = self.movimientos_posibles(m_nodo_cp)

                for i in niveles:
                    if i not in lista_comunes:
                        lista_comunes.append(i)
                        nodo_s = copy.deepcopy(matriz_nodo)
                        nodo_s.append(i)
                        arbol.append(nodo_s)
                        arbol2.append(nodo_s)
                        
                    if matriz_o in lista_comunes:
                            a = False
                if matriz_o in lista_comunes:
                    a = False
            if matriz_o in lista_comunes:
                a = False

        for i in arbol:
            if matriz_o in i:
                camino = copy.deepcopy(i)

        nivel = 0
        for i in camino:
            print(f"\nNivel {nivel}")
            for fila in i:
                print(fila)
            nivel += 1
        
        print(f"\nNumero de movimientos necesarios {len(arbol2)}")

        
        