import matplotlib.pyplot as plt
from neurona1 import *
from neurona2 import *
from neurona3 import *
from neurona4 import *

def main():
    
    tabla_xor = [[0, 0, 0],[0, 1, 1],[1, 0, 1],[1, 1, 0]]
    c = 0
    a = 0

    w0 = 0.9
    w1 = 0.7
    w2 = 0.5
    w3 = 0.3
    w4 = -0.9
    w5 = -1
    w6 = 0.8
    w7 = 0.35
    w8 = 0.1
    w9 = -0.23
    w10 = -0.79
    w11 = 0.56
    w12 = 0.6
    lista_w0 = []
    lista_w1 = []
    lista_w2 = []
    lista_w3 = []
    lista_w4 = []
    lista_w5 = []
    lista_w6 = []
    lista_w7 = []
    lista_w8 = []
    lista_w9 = []
    lista_w10 = []
    lista_w11 = []
    lista_w12 = []
    lista_errores0 = []
    lista_errores1 = []
    lista_errores2 = []
    lista_errores3 = []
    lista_contador = []
    lista_contador1 = []

    while c != 1:
        c+=1
        lista_contador1.append(c)
        print(f"--------------------------->Iteracion {c}<------------------------------------")
        for i in tabla_xor:
            a+=1
            lista_contador.append(a)
            y_n1, w0, w1, w2 = Neurona1().enseñar_neurona1(i, w0, w1, w2)
            y_n2, w3, w4, w5 = Neurona2().enseñar_neurona2(i, w3, w4, w5)
            y_n3, w6, w7, w8 = Neurona3().enseñar_neurona3(i, w6, w7, w8)
            s, w9, w10, w11, w12, error = Neurona4().enseñar_neurona4(y_n1, y_n2, y_n3, i, w9, w10, w11, w12)
            
            if i == [0,0,0]:
                lista_errores0.append(error)
            elif i == [0,1,1]:
                lista_errores1.append(error)
            elif i == [1,0,1]:
                lista_errores2.append(error)
            elif i == [1,1,0]:
                lista_errores3.append(error)    

            vias = 1
            lr = 0.5

            Soc1 = y_n1*(1-y_n1)*s

            delta_w0c1 = lr*vias*Soc1
            w0c1 = w0 + delta_w0c1
            delta_w1c1 = lr*i[0]*Soc1
            w1c1 = w1 + delta_w1c1
            delta_w2c1 = lr*i[1]*Soc1
            w2c1 = w2 + delta_w2c1

            w0 = w0c1
            w1 = w1c1
            w2 = w2c1

            # print(f"###{w0}###{w1}###{w2}")

            lista_w0.append(w0)
            lista_w1.append(w1)
            lista_w2.append(w2)

            Soc2 = y_n2*(1-y_n2)*s

            delta_w3c2 = lr*vias*Soc2
            w3c2 = w3 + delta_w3c2
            delta_w4c2 = lr*i[0]*Soc2
            w4c2 = w4 + delta_w4c2
            delta_w5c2 = lr*i[1]*Soc2
            w5c2 = w5 + delta_w5c2

            w3 = w3c2
            w4 = w4c2
            w5 = w5c2

            # print(f"###{w3}###{w4}###{w5}")

            lista_w3.append(w3)
            lista_w4.append(w4)
            lista_w5.append(w5)

            Soc3 = y_n3*(1-y_n3)*s

            delta_w6c3 = lr*vias*Soc3
            w6c3 = w6 + delta_w6c3
            delta_w7c3 = lr*i[0]*Soc3
            w7c3 = w7 + delta_w7c3
            delta_w8c3 = lr*i[1]*Soc3
            w8c3 = w8 + delta_w8c3

            w6 = w6c3
            w7 = w7c3
            w8 = w8c3

            # print(f"###{w6}###{w7}###{w8}")

            lista_w6.append(w6)
            lista_w7.append(w7)
            lista_w8.append(w8)

            w9 = w9
            w10 = w10
            w11 = w11
            w12 = w12

            lista_w9.append(w9)
            lista_w10.append(w10)
            lista_w11.append(w11)
            lista_w12.append(w12)

    plt.plot(lista_contador, lista_w0, label="w0")
    plt.plot(lista_contador, lista_w1, label="w1")
    plt.plot(lista_contador, lista_w2, label="w2")
    plt.plot(lista_contador, lista_w3, label="w3")
    plt.plot(lista_contador, lista_w4, label="w4")
    plt.plot(lista_contador, lista_w5, label="w5")
    plt.plot(lista_contador, lista_w6, label="w6")
    plt.plot(lista_contador, lista_w7, label="w7")
    plt.plot(lista_contador, lista_w8, label="w8")
    plt.plot(lista_contador, lista_w9, label="w9")
    plt.plot(lista_contador, lista_w10, label="w10")
    plt.plot(lista_contador, lista_w11, label="w11")
    plt.plot(lista_contador, lista_w12, label="w12")
    plt.title("pesos")
    plt.legend()
    # plt.show()
    # plt.savefig('grafica_pesos.png')

    plt.plot(lista_contador1, lista_errores0, label="errores0")
    plt.plot(lista_contador1, lista_errores1, label="errores1")
    plt.plot(lista_contador1, lista_errores2, label="errores2")
    plt.plot(lista_contador1, lista_errores3, label="errores3")
    plt.title("errores")
    plt.legend()
    # plt.show()
    # plt.savefig('grafica_errores.png')


if __name__ == '__main__':
    main()