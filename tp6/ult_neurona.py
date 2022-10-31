import math

class Ultima_neurona():

    def enseñar_ultNeurona(self, lista_y , fila, lista_pesos):

        vias = 1
        salida_deseada = fila[2]

        lista_cortada = lista_pesos[1:]

        x = (lista_pesos[0]*vias)

        for i in range(len(lista_cortada)):
            x += (lista_cortada[i]*lista_y[i])
        
        numerador = 1
        denominador = 1 + (math.e**(-x))
        s_real_y = numerador / denominador
        error = salida_deseada - s_real_y
        s = s_real_y*(1-s_real_y)*error
        lr = 0.5

        delta_w9 = lr*vias*s
        w9 = lista_pesos[0] + delta_w9

        nuevas_w = []

        nuevas_w.append(w9)

        for i in range(len(lista_y)):
            delta_gen = lr*lista_y[i]*s
            w_gen = lista_cortada[i] + delta_gen
            nuevas_w.append(w_gen)

        print("\nNeurona 4:\n")
        print(f"\nSalida real: {s_real_y}\n")

        return s, nuevas_w, error