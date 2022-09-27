import math

class Neurona4():

    def enseñar_neurona4(self, y_n1, y_n2, y_n3, fila, w9, w10, w11, w12):

        w9 = w9
        w10 = w10
        w11 = w11
        w12 = w12

        vias = 1
        e1 = y_n1
        e2 = y_n2
        e3 = y_n3
        s_deseada = fila[2]
        x = (w9*vias)+(w10*e1)+(w11*e2)+(w12*e3)
        numerador = 1
        denominador = 1 + (math.e**(-x))
        s_real_y = numerador / denominador
        error = s_deseada - s_real_y
        s = s_real_y*(1-s_real_y)*error
        lr = 0.5
        delta_w9 = lr*vias*s
        w9 = w9 + delta_w9
        delta_w10 = lr*e1*s
        w10 = w10 + delta_w10
        delta_w11 = lr*e2*s
        w11 = w11 + delta_w11
        delta_w12 = lr*e3*s
        w12 = w12 + delta_w12

        print("\nNeurona 4:\n")
        print(f"\nSalida real: {s_real_y}\n")

        return s, w9, w10, w11, w12
        