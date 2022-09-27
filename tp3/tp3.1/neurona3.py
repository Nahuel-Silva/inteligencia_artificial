import math

class Neurona3():

    def enseñar_neurona3(self, fila):

        w6 = 0.8
        w7 = 0.35
        w8 = 0.1

        # print("\nNeurona 3:\n")
        # print(f"W6: {w6}")
        # print(f"W7: {w7}")
        # print(f"W8: {w8}")

        vias = 1
        e1 = fila[0]
        e2 = fila[1]

        x = (w6*vias)+(w7*e1)+(w8*e2)
        numerador = 1
        denominador = 1 + (math.e**(-x))
        s_real_y = numerador / denominador

        # print(f"\nSalida real: {s_real_y}")

        return s_real_y, w6, w7, w8
        