import math

class Neurona3():

    def enseñar_neurona3(self, fila, w6, w7, w8):

        w6 = w6
        w7 = w7
        w8 = w8

        vias = 1
        e1 = fila[0]
        e2 = fila[1]

        x = (w6*vias)+(w7*e1)+(w8*e2)
        numerador = 1
        denominador = 1 + (math.e**(-x))
        s_real_y = numerador / denominador

        return s_real_y, w6, w7, w8
        