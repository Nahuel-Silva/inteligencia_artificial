from capa_oculta import Capa_oculta
from ult_neurona import *
import matplotlib.pyplot as plt
import random
from leer_img import *

def main():

    c = 0

    tabla_img = leer_imagenes()

    n = int(input("Cuantas neuronas quiere en la capa oculta (1 a n)? "))
    cant_entradas = len(tabla_img[0])

    pesos_cpo = []

    for i in range(n*cant_entradas):
        p = random.uniform(-1,1)
        pesos_cpo.append(p)

    pesos_ult_neu = []

    for i in range(n+1):
        p = random.uniform(-1,1)
        pesos_ult_neu.append(p)

    lista_div = []
    for i in range(0, len(pesos_cpo), cant_entradas):
        lista_div.append(pesos_cpo[i:i+cant_entradas])

    lista_y = []
    
    while c != 100:
        c += 1

        print(f"--------------------------->Iteracion {c}<------------------------------------")
        for i in tabla_img:
            for j in lista_div:
                s_real_y = Capa_oculta().neurona_generica(i, j)
                lista_y.append(s_real_y)

            s, nuevas_w, error = Ultima_neurona().enseñar_ultNeurona(lista_y, i, pesos_ult_neu)
            pesos_ult_neu.clear()
            pesos_ult_neu = nuevas_w

            vias = 1
            lr = 0.5

            lista_comun = []
            
            for l in range(len(lista_div)):
                Soc_gen = lista_y[l]*(1-lista_y[l])*s
                delta_prim = lr*vias*Soc_gen
                delta_seg = lr*i[0]*Soc_gen
                delta_ter = lr*i[1]*Soc_gen
                w_prim = lista_div[l][0] + delta_prim
                w_seg = lista_div[l][1] + delta_seg
                w_ter = lista_div[l][2] + delta_ter
                lista_comun.append(w_prim)
                lista_comun.append(w_seg)
                lista_comun.append(w_ter)

            lista_y.clear()
            lista_div.clear()


            for f in range(0, len(lista_comun), cant_entradas):
                lista_div.append(lista_comun[f:f+cant_entradas])

                




        

    

if __name__ == '__main__':
    main()