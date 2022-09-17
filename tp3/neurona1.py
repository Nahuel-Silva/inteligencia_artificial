import math

class Neurona1():

    def enseñar_neurona1(self):

        tabla_xor = [[0, 0, 0],[0, 1, 1],[1, 0, 1],[1, 1, 0]]

        w0 = 0.9
        w1 = 0.7
        w2 = 0.5

        print("Neurona 1:\n")
        print(f"W0: {w0}")
        print(f"W1: {w1}")
        print(f"W2: {w2}")

        vias = 1
        e1 = tabla_xor[0][0]
        e2 = tabla_xor[0][1]
        s_deseada = tabla_xor[0][2]
        x = (w0*vias)+(w1*e1)+(w2*e2)
        numerador = 1
        denominador = 1 + (math.e**(-x))
        s_real_y = numerador / denominador
        error = s_deseada - s_real_y
        s = s_real_y*(1-s_real_y)*error
        lr = 0.1
        delta_w0 = lr*vias*s
        w0 = w0 + delta_w0
        delta_w1 = lr*e1*s
        w1 = w1 + delta_w1
        delta_w2 = lr*e2*s
        w2 = w2 + delta_w2

        print(f"\nSalida real: {s_real_y}")
        print(f"W0: {w0}")
        print(f"W1: {w1}")
        print(f"W2: {w2}")

        return s_real_y
        