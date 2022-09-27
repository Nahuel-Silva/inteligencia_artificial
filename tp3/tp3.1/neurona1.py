import math

class Neurona1():

    def enseñar_neurona1(self, fila):

        w0 = 0.9
        w1 = 0.7
        w2 = 0.5

        # print("Neurona 1:\n")
        # print(f"W0: {w0}")
        # print(f"W1: {w1}")
        # print(f"W2: {w2}")

        vias = 1
        e1 = fila[0]
        e2 = fila[1]
        x = (w0*vias)+(w1*e1)+(w2*e2)
        numerador = 1
        denominador = 1 + (math.e**(-x))
        s_real_y = numerador / denominador

        # print(f"\nSalida real: {s_real_y}")

        return s_real_y, w0, w1, w2
        