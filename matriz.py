import numpy as np
import random


class Matriz():

    def armar_matriz(self, cant_col, cant_fil):

        matriz = []
        a = 0

        for i in range(cant_fil):
            matriz.append([])
            for j in range(cant_col):
                a += 1
                matriz[i].append(a)
        
        matriz[cant_fil-1][cant_col-1] = 0

        # print(matriz)
        return matriz

    def matriz_np(self, cant_col, cant_fil):

        matriz = np.zeros((cant_col, cant_fil), int)
        a = 0

        for i in range(cant_fil):
            for j in range(cant_col):
                a += 1
                matriz[i][j] = a
        matriz[-1][-1] = 0

        # print(matriz)
        return matriz

    def matriz_random(self, cant_col, cant_fil, num_mezcladas):

        matriz = []
        cant_pos = [i for i in range(cant_col*cant_fil)]

        for i in range(num_mezcladas):
            random.shuffle(cant_pos)

        a = 0

        for i in range(cant_fil):
            matriz.append([])
            for j in range(cant_col):
                matriz[i].append(cant_pos[a])
                a += 1
            
        # print(matriz)
        
        return matriz

    def random_np(self, cant_col, cant_fil, num_mezcladas):

        matriz = np.zeros((cant_col, cant_fil), int)
        a = 0

        cant_pos = [i for i in range(cant_col*cant_fil)]

        for i in range(num_mezcladas):
            random.shuffle(cant_pos)

        for i in range(cant_fil):
            for j in range(cant_col):
                matriz[i][j] = cant_pos[a]
                a += 1

        # print(matriz)
        return matriz
        