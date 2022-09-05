import copy


class B_bidireccional():

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

    def definitiva(self, matriz_r, matriz_o):

        lista_comunes = []
        lista_comunes2 = []

        arbol = [[]]
        arbol_bi = [[]]
        arbol[0].append(matriz_r)
        arbol_bi[0].append(matriz_o)

        arbol2 = copy.deepcopy(arbol)
        arbol_bi2 = copy.deepcopy(arbol_bi)

        lista_comunes.append(matriz_r)
        lista_comunes2.append(matriz_o)
        
        a = True
        while a == True:

            arbol_cp = copy.deepcopy(arbol)
            arbol_cp2 = copy.deepcopy(arbol_bi)

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

            for matriz_nodo2 in arbol_cp2:
                arbol_bi.remove(matriz_nodo2)
                m_nodo_cp2 = copy.deepcopy(matriz_nodo2[-1])
                niveles2 = self.movimientos_posibles(m_nodo_cp2)
                for j in niveles2:
                    if j not in lista_comunes2:
                        lista_comunes2.append(j)
                        nodo_s2 = copy.deepcopy(matriz_nodo2)
                        nodo_s2.append(j)
                        arbol_bi.append(nodo_s2)
                        arbol_bi2.append(nodo_s2)

            for h in lista_comunes:
                if h in lista_comunes2:
                    a = False
                    matriz_coinc = copy.deepcopy(h)
        
        for i in arbol2:
            if matriz_coinc in i:
                camino2 = copy.deepcopy(i)

        for j in arbol_bi2:
            if matriz_coinc in j:
                camino1 = copy.deepcopy(j)
        
        print("\nMatriz coincidente: ")
        for fila in matriz_coinc:
            print(fila)

        camino2 = camino2[:-1]
        camino1.reverse()

        c = 0
        for l in camino2:
            print(f"\nNivel {c}")
            for fila in l:
                print(fila)
            c+=1

        for m in camino1:
            print(f"\nNivel {c}")
            for fila2 in m:
                print(fila2)
            c+=1