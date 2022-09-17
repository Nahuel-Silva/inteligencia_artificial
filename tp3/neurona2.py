import math

class Neurona2():

    def enseñar_neurona2(self):

        tabla_xor = [[0, 0, 0],[0, 1, 1],[1, 0, 1],[1, 1, 0]]

        w3 = 0.3
        w4 = -0.9
        w5 = -1

        print("\nNeurona 2:\n")
        print(f"W3: {w3}")
        print(f"W4: {w4}")
        print(f"W5: {w5}")

        vias = 1
        e1 = tabla_xor[0][0]
        e2 = tabla_xor[0][1]
        s_deseada = tabla_xor[0][2]
        x = (w3*vias)+(w4*e1)+(w5*e2)
        numerador = 1
        denominador = 1 + (math.e**(-x))
        s_real_y = numerador / denominador
        error = s_deseada - s_real_y
        s = s_real_y*(1-s_real_y)*error
        lr = 0.1
        delta_w3 = lr*vias*s
        w3 = w3 + delta_w3
        delta_w4 = lr*e1*s
        w4 = w4 + delta_w4
        delta_w5 = lr*e2*s
        w5 = w5 + delta_w5

        print(f"\nSalida real: {s_real_y}")
        print(f"W3: {w3}")
        print(f"W4: {w4}")
        print(f"W5: {w5}")

        return s_real_y
        