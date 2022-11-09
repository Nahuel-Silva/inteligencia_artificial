import math

class Ultima_neurona():

    def enseñar_ultNeurona(self, lista_y , fila, lista_pesos):

        salida_deseada = fila[-1]
        x = 0

        for i in range(len(lista_pesos)):
            x += (lista_pesos[i]*lista_y[i])
        
        numerador = 1
        denominador = 1 + (math.e**(-x))
        s_real_y = numerador / denominador
        error = salida_deseada - s_real_y
        s = s_real_y*(1-s_real_y)*error
        lr = 0.5

        nuevas_w = []

        for i in range(len(lista_y)):
            delta_gen = lr*lista_y[i]*s
            w_gen = lista_pesos[i] + delta_gen
            nuevas_w.append(w_gen)

        print("\nNeurona 4:\n")
        print(f"\nSalida real: {s_real_y}\n")

        return s, nuevas_w, error