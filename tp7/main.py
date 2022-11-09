from capa_oculta import Capa_oculta
from ult_neurona import *
import matplotlib.pyplot as plt
import random
from leer_img import *
from leer_pesos import *

def main():

    c = 0
    contador = []

    tabla_img = leer_imagenes()

    n = int(input("Cuantas neuronas quiere en la capa oculta (1 a n)? "))
    cant_entradas = len(tabla_img[0])-1 #7681 entradas

    pesos_cpo, pesos_ult_neu = leer_pesos()


    lista_div = []
    for i in range(0, len(pesos_cpo), cant_entradas):
        lista_div.append(pesos_cpo[i:i+cant_entradas]) #50 listas de 7681 pesos

    lista_y = []
    lista_errores = [[] for x in range(len(tabla_img))]
    
    while c != 20:
        c += 1
        cont_error = 0
        contador.append(c)
        print(f"--------------------------->Iteracion {c}<------------------------------------")
        for i in tabla_img:
            lista_y.append(1)
            for j in lista_div:
                s_real_y = Capa_oculta().neurona_generica(i, j)
                lista_y.append(s_real_y) #51 salidas reales (y)

            s, nuevas_w, error = Ultima_neurona().enseñar_ultNeurona(lista_y, i, pesos_ult_neu)
            lista_errores[cont_error].append(error)
            cont_error += 1
            pesos_ult_neu.clear()
            pesos_ult_neu = nuevas_w #51 pesos de la ultima neurona

            lr = 0.5

            lista_comun = []
            
            i_cortada = i[:-1] #7681 entradas (excluimos la ultima)
            y_cortada = lista_y[1:] #50 salidas reales (excluimos el vias que agregamos en el principio para la ult neurona)

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

    # with open('pesos.txt', 'w') as f:
    #     for peso in lista_comun:
    #         f.write(str(peso) + "\n")

    # with open('pesos2.txt', 'w') as f:
    #     for peso in pesos_ult_neu:
    #         f.write(str(peso) + "\n")
    
    for i in range(len(lista_errores)):
        plt.plot(contador, lista_errores[i], label=f"errores{i}")
    plt.title("errores")
    plt.legend()
    plt.show()



if __name__ == '__main__':
    main()