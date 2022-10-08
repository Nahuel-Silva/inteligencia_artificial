import math

class Capa_oculta():

    def neurona_generica(self, fila, list_pesos):

        w_a = list_pesos[0]
        w_b = list_pesos[1]
        w_c = list_pesos[2]

        vias = 1
        e1 = fila[0]
        e2 = fila[1]
        x = (w_a*vias)+(w_b*e1)+(w_c*e2)
        numerador = 1
        denominador = 1 + (math.e**(-x))
        s_real_y = numerador / denominador

        return s_real_y
        