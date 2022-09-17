import math

class Neurona4():

    def enseñar_neurona4(self, y_n1, y_n2):

        tabla_xor = [[0, 0, 0],[0, 1, 1],[1, 0, 1],[1, 1, 0]]

        w9 = -0.23
        w10 = -0.79
        w11 = 0.56

        print("\nNeurona 4:\n")
        print(f"W9: {w9}")
        print(f"W10: {w10}")
        print(f"W11: {w11}")

        vias = 1
        e1 = y_n1
        e2 = y_n2
        s_deseada = tabla_xor[0][2]
        x = (w9*vias)+(w10*e1)+(w11*e2)
        numerador = 1
        denominador = 1 + (math.e**(-x))
        s_real_y = numerador / denominador
        error = s_deseada - s_real_y
        s = s_real_y*(1-s_real_y)*error
        lr = 0.1
        delta_w9 = lr*vias*s
        w9 = w9 + delta_w9
        delta_w10 = lr*e1*s
        w10 = w10 + delta_w10
        delta_w11 = lr*e2*s
        w11 = w11 + delta_w11

        print(f"\nSalida real: {s_real_y}")
        print(f"W9: {w9}")
        print(f"W10: {w10}")
        print(f"W11: {w11}")

        return s_real_y
        