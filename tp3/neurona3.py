import math

class Neurona3():

    def enseñar_neurona3(self, y_n1, y_n2):

        tabla_xor = [[0, 0, 0],[0, 1, 1],[1, 0, 1],[1, 1, 0]]

        w6 = 0.8
        w7 = 0.35
        w8 = 0.1

        print("\nNeurona 3:\n")
        print(f"W6: {w6}")
        print(f"W7: {w7}")
        print(f"W8: {w8}")

        vias = 1
        e1 = y_n1
        e2 = y_n2
        s_deseada = tabla_xor[0][2]
        x = (w6*vias)+(w7*e1)+(w8*e2)
        numerador = 1
        denominador = 1 + (math.e**(-x))
        s_real_y = numerador / denominador
        error = s_deseada - s_real_y
        s = s_real_y*(1-s_real_y)*error
        lr = 0.1
        delta_w6 = lr*vias*s
        w6 = w6 + delta_w6
        delta_w7 = lr*e1*s
        w7 = w7 + delta_w7
        delta_w8 = lr*e2*s
        w8 = w8 + delta_w8

        print(f"\nSalida real: {s_real_y}")
        print(f"W6: {w6}")
        print(f"W7: {w7}")
        print(f"W8: {w8}")

        return s_real_y
        