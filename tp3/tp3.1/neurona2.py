import math

class Neurona2():

    def enseñar_neurona2(self, fila):

        w3 = 0.3
        w4 = -0.9
        w5 = -1

        # print("\nNeurona 2:\n")
        # print(f"W3: {w3}")
        # print(f"W4: {w4}")
        # print(f"W5: {w5}")

        vias = 1
        e1 = fila[0]
        e2 = fila[1]

        x = (w3*vias)+(w4*e1)+(w5*e2)
        numerador = 1
        denominador = 1 + (math.e**(-x))
        s_real_y = numerador / denominador

        # print(f"\nSalida real: {s_real_y}")

        return s_real_y, w3, w4, w5
        