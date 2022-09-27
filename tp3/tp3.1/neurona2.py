import math

class Neurona2():

    def enseñar_neurona2(self, fila, w3, w4, w5):

        w3 = w3
        w4 = w4
        w5 = w5

        vias = 1
        e1 = fila[0]
        e2 = fila[1]

        x = (w3*vias)+(w4*e1)+(w5*e2)
        numerador = 1
        denominador = 1 + (math.e**(-x))
        s_real_y = numerador / denominador

        return s_real_y, w3, w4, w5
        