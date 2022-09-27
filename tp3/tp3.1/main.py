from re import S
from neurona1 import *
from neurona2 import *
from neurona3 import *
from neurona4 import *

def main():
    
    tabla_xor = [[0, 0, 0],[0, 1, 1],[1, 0, 1],[1, 1, 0]]
    c = 0

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

    while c != 1000:
        c+=1
        print(f"--------------------------->Iteracion {c}<------------------------------------")
        for i in tabla_xor:
            y_n1, w0, w1, w2 = Neurona1().enseñar_neurona1(i, w0, w1, w2)
            y_n2, w3, w4, w5 = Neurona2().enseñar_neurona2(i, w3, w4, w5)
            y_n3, w6, w7, w8 = Neurona3().enseñar_neurona3(i, w6, w7, w8)
            s, w9, w10, w11, w12 = Neurona4().enseñar_neurona4(y_n1, y_n2, y_n3, i, w9, w10, w11, w12)

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

            w9 = w9
            w10 = w10
            w11 = w11
            w12 = w12

        if c == 1000:
            break


if __name__ == '__main__':
    main()