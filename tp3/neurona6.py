import math

class Neurona6():

    def enseñar_neurona6(self, y_n3, y_n4, y_n5):

        tabla_xor = [[0, 0, 0],[0, 1, 1],[1, 0, 1],[1, 1, 0]]

        w15 = -0.22
        w16 = -0.55
        w17 = 0.31
        w18 = -0.32

        print("\nNeurona 6:\n")
        print(f"W15: {w15}")
        print(f"W16: {w16}")
        print(f"W17: {w17}")
        print(f"W18: {w18}")

        vias = 1
        e1 = y_n3
        e2 = y_n4
        e3 = y_n5
        s_deseada = tabla_xor[0][2]
        x = (w15*vias)+(w16*e1)+(w17*e2)+(w18*e3)
        numerador = 1
        denominador = 1 + (math.e**(-x))
        s_real_y = numerador / denominador
        error = s_deseada - s_real_y
        s = s_real_y*(1-s_real_y)*error
        lr = 0.1
        delta_w15 = lr*vias*s
        w15 = w15 + delta_w15
        delta_w16 = lr*e1*s
        w16 = w16 + delta_w16
        delta_w17 = lr*e2*s
        w17 = w17 + delta_w17

        print(f"\nSalida real: {s_real_y}")
        print(f"W15: {w15}")
        print(f"W16: {w16}")
        print(f"W17: {w17}")
        print(f"W18: {w18}")

        return s_real_y