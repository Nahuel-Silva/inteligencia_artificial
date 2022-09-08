import math

class Perceptron():

    def enseñar_perceptron(self):

        tabla_or = [[0,0,0],[0,1,1],[1,0,1],[1,1,1]]

        tabla_and = [[0,0,0],[0,1,0],[1,0,0],[1,1,1]]

        w0 = 0.9
        w1 = 0.66
        w2 = -0.2

        error = 1

        res = input("Quiere usar la tabla or o and? ")

        if res == "or":
            tabla = tabla_or
        else:
            tabla = tabla_and

        contador = 0

        print(f"W0: {w0}")
        print(f"W1: {w1}")
        print(f"W2: {w2}")
        a = True
        while math.fabs(error) > 0.1:
        # while a == True:
            contador += 1
            r = 0
            for fila in tabla:
                r += 1
                # input()
                vias = 1
                e1 = fila[0]
                e2 = fila[1]
                s_deseada = fila[2]
                x = (w0*vias)+(w1*e1)+(w2*e2)
                numerador = 1
                denominador = 1 + (math.e**(-x))
                s_real_y = numerador / denominador
                error = s_deseada - s_real_y
                s = s_real_y*(1-s_real_y)*error
                lr = 0.1
                delta_w0 = lr*vias*s
                w0 = w0 + delta_w0
                delta_w1 = lr*e1*s
                w1 = w1 + delta_w1
                delta_w2 = lr*e2*s
                w2 = w2 + delta_w2
                print(f"Iteracion {contador} R{r}")
                print(f"W0: {w0}")
                print(f"W1: {w1}")
                print(f"W2: {w2}")
                print(f"Error: {error}\n")
                # if contador == 1000:
                #     a = False