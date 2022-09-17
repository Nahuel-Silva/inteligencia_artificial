import math

class Neurona5():

    def enseñar_neurona5(self, y_n1, y_n2):

        tabla_xor = [[0, 0, 0],[0, 1, 1],[1, 0, 1],[1, 1, 0]]

        w12 = 0.6
        w13 = -0.6
        w14 = 0.22

        print("\nNeurona 5:\n")
        print(f"W12: {w12}")
        print(f"W13: {w13}")
        print(f"W14: {w14}")

        vias = 1
        e1 = y_n1
        e2 = y_n2
        s_deseada = tabla_xor[0][2]
        x = (w12*vias)+(w13*e1)+(w14*e2)
        numerador = 1
        denominador = 1 + (math.e**(-x))
        s_real_y = numerador / denominador
        error = s_deseada - s_real_y
        s = s_real_y*(1-s_real_y)*error
        lr = 0.1
        delta_w12 = lr*vias*s
        w12 = w12 + delta_w12
        delta_w13 = lr*e1*s
        w13 = w13 + delta_w13
        delta_w14 = lr*e2*s
        w14 = w14 + delta_w14

        print(f"\nSalida real: {s_real_y}")
        print(f"W12: {w12}")
        print(f"W13: {w13}")
        print(f"W14: {w14}")

        return s_real_y