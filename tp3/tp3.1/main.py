from re import S
from neurona1 import *
from neurona2 import *
from neurona3 import *
from neurona4 import *

def main():
    tabla_xor = [[0, 0, 0],[0, 1, 1],[1, 0, 1],[1, 1, 0]]
    a=True
    c = 0
    while a:
        c+=1
        for i in tabla_xor:
            
            y_n1, w0, w1, w2 = Neurona1().enseñar_neurona1(i)
            y_n2, w3, w4, w5 = Neurona2().enseñar_neurona2(i)
            y_n3, w6, w7, w8 = Neurona3().enseñar_neurona3(i)
            s = Neurona4().enseñar_neurona4(y_n1, y_n2, y_n3, i)

            vias = 1
            lr = 0.1

            Soc1 = y_n1*(1-y_n1)*s

            delta_w0c1 = lr*vias*Soc1
            w0c1 = w0 + delta_w0c1
            delta_w1c1 = lr*i[0]*Soc1
            w1c1 = w1 + delta_w1c1
            delta_w2c1 = lr*i[1]*Soc1
            w2c1 = w2 + delta_w2c1

            Soc2 = y_n2*(1-y_n2)*s

            delta_w3c2 = lr*vias*Soc2
            w3c2 = w3 + delta_w3c2
            delta_w4c2 = lr*i[0]*Soc2
            w4c2 = w4 + delta_w4c2
            delta_w5c2 = lr*i[1]*Soc2
            w5c2 = w5 + delta_w5c2

            Soc3 = y_n3*(1-y_n3)*s

            delta_w6c3 = lr*vias*Soc3
            w6c3 = w6 + delta_w6c3
            delta_w7c3 = lr*i[0]*Soc3
            w7c3 = w7 + delta_w7c3
            delta_w8c3 = lr*i[1]*Soc3
            w8c3 = w8 + delta_w8c3
        if c == 1000:
            break



if __name__ == '__main__':
    main()