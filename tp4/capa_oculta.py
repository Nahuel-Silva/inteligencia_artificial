import math

class Capa_oculta():

    def neurona_generica(self, fila, list_pesos):
        
        lista_cortada = list_pesos[1:]
        fila_cortada = fila[:-1]
        vias = 1
        x = list_pesos[0]*vias
        for i in range(len(lista_cortada)):
            x += (lista_cortada[i] + fila_cortada[i])
        numerador = 1
        denominador = 1 + (math.e**(-x))
        s_real_y = numerador / denominador

        return s_real_y
        