from neurona1 import *
from neurona2 import *
from neurona3 import *
from neurona4 import *
from neurona5 import *
from neurona6 import *

def main():
    y_n1 = Neurona1().enseñar_neurona1()
    y_n2 = Neurona2().enseñar_neurona2()
    y_n3 = Neurona3().enseñar_neurona3(y_n1, y_n2)
    y_n4 = Neurona4().enseñar_neurona4(y_n1, y_n2)
    y_n5 = Neurona5().enseñar_neurona5(y_n1, y_n2)
    Neurona6().enseñar_neurona6(y_n3, y_n4, y_n5)


if __name__ == '__main__':
    main()