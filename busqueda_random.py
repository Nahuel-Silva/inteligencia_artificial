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

    def movimientos_posibles(self, matriz_r):

        pos_fila0, pos_cero = B_random().posicion_cero(matriz_r)

        # Primera fila
        if pos_fila0 == 0:
            # Indice a11
            if pos_cero == 0:
                pos_mov = [0,1]
                n_random = random.choice(pos_mov)
                if n_random == 1:
                    matriz_r[pos_fila0][pos_cero], matriz_r[pos_fila0][n_random] = matriz_r[pos_fila0][n_random], matriz_r[pos_fila0][pos_cero]
                elif n_random == 0:
                    matriz_r[pos_fila0][pos_cero], matriz_r[1][pos_cero] =  matriz_r[1][pos_cero], matriz_r[pos_fila0][pos_cero]

            # Indice a12
            elif pos_cero == 1:
                pos_mov = [0,1,2]
                n_random = random.choice(pos_mov)
                if n_random == 0:
                    matriz_r[pos_fila0][pos_cero], matriz_r[pos_fila0][n_random] = matriz_r[pos_fila0][n_random], matriz_r[pos_fila0][pos_cero]
                elif n_random == 2:
                    matriz_r[pos_fila0][pos_cero], matriz_r[pos_fila0][n_random] = matriz_r[pos_fila0][n_random], matriz_r[pos_fila0][pos_cero]
                elif n_random == 1:
                    matriz_r[pos_fila0][pos_cero], matriz_r[1][n_random] = matriz_r[1][n_random], matriz_r[pos_fila0][pos_cero]
            
            # Indice a13
            elif pos_cero == 2:
                pos_mov = [1,2]
                n_random = random.choice(pos_mov)
                if n_random == 1:
                    matriz_r[pos_fila0][pos_cero], matriz_r[pos_fila0][n_random] = matriz_r[pos_fila0][n_random], matriz_r[pos_fila0][pos_cero]
                elif n_random == 2:
                    matriz_r[pos_fila0][pos_cero], matriz_r[1][pos_cero] = matriz_r[1][pos_cero], matriz_r[pos_fila0][pos_cero]

        # Segunda fila
        elif pos_fila0 == 1:
            # Indice a21
            if pos_cero == 0:
                pos_mov = [0,1,2]
                n_random = random.choice(pos_mov)
                if n_random == 0:
                    matriz_r[pos_fila0][pos_cero], matriz_r[0][n_random] = matriz_r[0][n_random], matriz_r[pos_fila0][pos_cero]
                elif n_random == 1:
                    matriz_r[pos_fila0][pos_cero], matriz_r[pos_fila0][n_random] = matriz_r[pos_fila0][n_random], matriz_r[pos_fila0][pos_cero]
                elif n_random == 2:
                    matriz_r[pos_fila0][pos_cero], matriz_r[n_random][0] = matriz_r[n_random][0], matriz_r[pos_fila0][pos_cero]

            # Indice a22
            elif pos_cero == 1:
                pos_mov = [0,1,2,3]
                n_random = random.choice(pos_mov)
                if n_random == 0:
                    matriz_r[pos_fila0][pos_cero], matriz_r[pos_fila0][n_random] = matriz_r[pos_fila0][n_random], matriz_r[pos_fila0][pos_cero]
                elif n_random == 1:
                    matriz_r[pos_fila0][pos_cero], matriz_r[0][n_random] = matriz_r[0][n_random], matriz_r[pos_fila0][pos_cero]
                elif n_random == 2:
                    matriz_r[pos_fila0][pos_cero],  matriz_r[pos_fila0][n_random] = matriz_r[pos_fila0][n_random], matriz_r[pos_fila0][pos_cero]
                elif n_random == 3:
                    matriz_r[pos_fila0][pos_cero], matriz_r[2][pos_cero] = matriz_r[2][pos_cero], matriz_r[pos_fila0][pos_cero]
            
            # Indice a23
            elif pos_cero == 2:
                pos_mov = [0,1,2]
                n_random = random.choice(pos_mov)
                if n_random == 0:
                    matriz_r[pos_fila0][pos_cero], matriz_r[n_random][pos_cero] = matriz_r[n_random][pos_cero], matriz_r[pos_fila0][pos_cero]
                elif n_random == 1:
                    matriz_r[pos_fila0][pos_cero], matriz_r[n_random][n_random] = matriz_r[n_random][n_random], matriz_r[pos_fila0][pos_cero]
                elif n_random == 2:
                    matriz_r[pos_fila0][pos_cero], matriz_r[n_random][pos_cero] = matriz_r[n_random][pos_cero], matriz_r[pos_fila0][pos_cero]

        # Tercera fila
        elif pos_fila0 == 2:
            # Indice a31
            if pos_cero == 0:
                pos_mov = [1,2]
                n_random = random.choice(pos_mov)
                if n_random == 1:
                    matriz_r[pos_fila0][pos_cero], matriz_r[n_random][pos_cero] = matriz_r[n_random][pos_cero], matriz_r[pos_fila0][pos_cero]
                elif n_random == 2:
                    matriz_r[pos_fila0][pos_cero], matriz_r[pos_fila0][1] = matriz_r[pos_fila0][1], matriz_r[pos_fila0][pos_cero]

            # Indice a32
            elif pos_cero == 1:
                pos_mov = [0,1,2]
                n_random = random.choice(pos_mov)
                if n_random == 0:
                    matriz_r[pos_fila0][pos_cero], matriz_r[pos_fila0][n_random] = matriz_r[pos_fila0][n_random], matriz_r[pos_fila0][pos_cero]
                elif n_random == 1:
                    matriz_r[pos_fila0][pos_cero], matriz_r[n_random][pos_cero] = matriz_r[n_random][pos_cero], matriz_r[pos_fila0][pos_cero]
                elif n_random == 2:
                    matriz_r[pos_fila0][pos_cero], matriz_r[pos_fila0][n_random] = matriz_r[pos_fila0][n_random], matriz_r[pos_fila0][pos_cero]

            # Indice a33
            elif pos_cero == 2:
                pos_mov = [1,2]
                n_random = random.choice(pos_mov)
                if n_random == 1:
                    matriz_r[pos_fila0][pos_cero], matriz_r[pos_fila0][n_random] = matriz_r[pos_fila0][n_random], matriz_r[pos_fila0][pos_cero]
                elif n_random == 2:
                    matriz_r[pos_fila0][pos_cero], matriz_r[1][n_random] = matriz_r[1][n_random], matriz_r[pos_fila0][pos_cero]

        return matriz_r

    def definitiva(self, matriz_r, matriz_o):

        contador = 0

        while True:
            matriz_armada = B_random().movimientos_posibles(matriz_r)
            contador += 1
            if matriz_armada == matriz_o:
                print(f"\nNumero de movimientos necesarios {contador}")
                print(f"\nMatriz resultante: ")
                for fila in matriz_armada:
                    print(fila)
                break