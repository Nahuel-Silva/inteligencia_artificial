import math

class Neurona1():

    def enseñar_neurona1(self, fila, w0, w1, w2):

        w0 = w0
        w1 = w1
        w2 = w2

        vias = 1
        e1 = fila[0]
        e2 = fila[1]
        x = (w0*vias)+(w1*e1)+(w2*e2)
        numerador = 1
        denominador = 1 + (math.e**(-x))
        s_real_y = numerador / denominador

        return s_real_y, w0, w1, w2
        