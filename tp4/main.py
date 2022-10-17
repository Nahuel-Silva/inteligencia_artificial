from capa_oculta import Capa_oculta
from ult_neurona import *

def main():
    c = 0

    tabla_xor = [[0, 0, 0],[0, 1, 1],[1, 0, 1],[1, 1, 0]]

    n = int(input("Cuantas neuronas quiere en la capa oculta (1 a n)? "))

    pesos_cpo = []

    a = 0

    for i in range(n*3):
        a += 1
        p = float(input(f"Ingrese el peso {i}: "))
        pesos_cpo.append(p)

    pesos_ult_neu = []

    for i in range(n+1):
        p = float(input(f"Ingrese el peso {a}: "))
        pesos_ult_neu.append(p)
        a += 1

    lista_div = []
    for i in range(0, len(pesos_cpo), 3):
        lista_div.append(pesos_cpo[i:i+3])

    lista_y = []
    
    while c != 1:
        c += 1

        print(f"--------------------------->Iteracion {c}<------------------------------------")
        for i in tabla_xor:
            for j in lista_div:
                s_real_y = Capa_oculta().neurona_generica(i, j)
                lista_y.append(s_real_y)

            s, nuevas_w, error = Ultima_neurona().enseñar_ultNeurona(lista_y, i, pesos_ult_neu)
            pesos_ult_neu = nuevas_w

            vias = 1
            lr = 0.1

            lista_comun = []
            
            for l in range(len(lista_div)):
                Soc_gen = lista_y[l]*(1-lista_y[l])*s
                delta_gen = lr*vias*Soc_gen
                for r in range(len(lista_div)):
                    w_gen = lista_div[l][r] + delta_gen
                    lista_comun.append(w_gen)

            lista_y.clear()
            lista_div.clear()

            for f in range(0, len(lista_comun), 3):
                lista_div.append(lista_comun[f:f+3])

                




        

    

if __name__ == '__main__':
    main()