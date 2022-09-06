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
        