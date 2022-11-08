from capa_oculta import Capa_oculta
from ult_neurona import *
import matplotlib.pyplot as plt
import random

def main():

    lista_errores0 = []
    lista_errores1 = []
    lista_errores2 = []
    lista_errores3 = []
    lista_contador = []

    c = 0

    tabla_xor = [[1, 0, 0, 0],[1, 0, 1, 1],[1, 1, 0, 1],[1, 1, 1, 0]]

    n = int(input("Cuantas neuronas quiere en la capa oculta (1 a n)? "))
    cant_entradas = 3

    pesos_cpo = []

    for i in range(n*cant_entradas):
        p = random.uniform(-1, 1)
        pesos_cpo.append(p)

    pesos_ult_neu = []

    for i in range(n+1):
        p = random.uniform(-1, 1)
        pesos_ult_neu.append(p)

    lista_div = []
    for i in range(0, len(pesos_cpo), cant_entradas):
        lista_div.append(pesos_cpo[i:i+cant_entradas])

    lista_y = []
    
    while c != 10000:
        c += 1
        lista_contador.append(c)

        print(f"--------------------------->Iteracion {c}<------------------------------------")
        for i in tabla_xor:
            lista_y.append(1)
            for j in lista_div:
                s_real_y = Capa_oculta().neurona_generica(i, j)
                lista_y.append(s_real_y)

            s, nuevas_w, error = Ultima_neurona().enseñar_ultNeurona(lista_y, i, pesos_ult_neu)
            pesos_ult_neu.clear()
            pesos_ult_neu = nuevas_w

            if i == [1,0,0,0]:
                lista_errores0.append(error)
            elif i == [1,0,1,1]:
                lista_errores1.append(error)
            elif i == [1,1,0,1]:
                lista_errores2.append(error)
            elif i == [1,1,1,0]:
                lista_errores3.append(error)   

            lr = 0.5

            lista_comun = []
            
            i_cortada = i[:-1]
            y_cortada = lista_y[1:] 

            for l in range(len(y_cortada)):
                Soc_gen = y_cortada[l]*(1-y_cortada[l])*s
                for q in range(len(i_cortada)):
                    delta_gen = lr*i_cortada[q]*Soc_gen
                    w_gen = lista_div[l][q] + delta_gen
                    lista_comun.append(w_gen)

            lista_y.clear()
            lista_div.clear()


            for f in range(0, len(lista_comun), cant_entradas):
                lista_div.append(lista_comun[f:f+cant_entradas])

    plt.plot(lista_contador, lista_errores0, label="errores0")
    plt.plot(lista_contador, lista_errores1, label="errores1")
    plt.plot(lista_contador, lista_errores2, label="errores2")
    plt.plot(lista_contador, lista_errores3, label="errores3")
    plt.title("errores")
    plt.legend()
    plt.show()
            

                




        

    

if __name__ == '__main__':
    main()