import math

class Capa_oculta():

    def neurona_generica(self, fila, list_pesos):
        
        fila_cortada = fila[:-1]
        x = 0
        for i in range(len(list_pesos)):
            x += (list_pesos[i] * fila_cortada[i])
        numerador = 1
        denominador = 1 + (math.e**(-x))
        s_real_y = numerador / denominador

        return s_real_y
        