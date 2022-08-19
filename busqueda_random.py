
class B_random():

    def busqueda_random(self, matriz_r, matriz_o):

        pos_fila0 = 0
        pos_ficha = 0

        for fila in matriz_r:
            pos_fila0 += 1
            for pos in fila:
                pos_ficha += 1
                if pos == 0:
                    pos_ficha = pos_ficha - 1
                    pos_fila0 = pos_fila0 - 1
                    
                     


        print(matriz_r)