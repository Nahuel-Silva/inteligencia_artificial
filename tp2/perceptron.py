import math
import matplotlib.pyplot as plt

class Perceptron():

    def enseñar_perceptron(self):

        tabla_or = [[0,0,0],[0,1,1],[1,0,1],[1,1,1]]

        tabla_and = [[0,0,0],[0,1,0],[1,0,0],[1,1,1]]

        tabla_xor = [[0, 0, 0],[0, 1, 1],[1, 0, 1],[1, 1, 0]]

        lista_w0 = []
        lista_w1 = []
        lista_w2 = []
        lista_con = []
        lista_con2 = []
        errores_r1 = []
        errores_r2 = []
        errores_r3 = []
        errores_r4 = []

        w0 = 0.9
        w1 = 0.66
        w2 = -0.2

        error = 1

        res = input("Quiere usar la tabla or, and o xor? ")

        if res == "or":
            tabla = tabla_or
        elif res == "and":
            tabla = tabla_and
        elif res == "xor":
            tabla = tabla_xor

        contador = 0
        c = 0

        print(f"W0: {w0}")
        print(f"W1: {w1}")
        print(f"W2: {w2}")

        a = True
        # while math.fabs(error) > 0.1:
        while a == True:
            contador += 1
            lista_con.append(contador)
            r = 0
            for fila in tabla:
                c += 1
                lista_con2.append(c)
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
                # print(f"Iteracion {contador} R{r}")
                # print(f"W0: {w0}")
                # print(f"W1: {w1}")
                # print(f"W2: {w2}")
                # print(f"Error: {error}\n")
                
                lista_w0.append(w0)
                lista_w1.append(w1)
                lista_w2.append(w2)

                if fila == tabla[0]:
                    errores_r1.append(error)
                elif fila == tabla[1]:
                    errores_r2.append(error)
                elif fila == tabla[2]:
                    errores_r3.append(error)
                elif fila == tabla[3]:
                    errores_r4.append(error)    

                if contador == 10000:
                    a = False
        
        plt.plot(lista_con, errores_r1, label="error de r1")
        plt.plot(lista_con, errores_r2, label="error de r2")
        plt.plot(lista_con, errores_r3, label="error de r3")
        plt.plot(lista_con, errores_r4, label="error de r4")
        plt.title("Errores")
        plt.legend()
        plt.show()
        plt.savefig('grafica_error.png')

        plt.plot(lista_con2, lista_w0, label="w0")
        plt.plot(lista_con2, lista_w1, label="w1")
        plt.plot(lista_con2, lista_w2, label="w2")
        plt.title("pesos")
        plt.legend()
        plt.show()
        plt.savefig('grafica_pesos.png')
        
        
        

