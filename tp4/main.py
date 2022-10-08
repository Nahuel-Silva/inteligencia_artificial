from capa_oculta import Capa_oculta

def main():
    c = 0

    tabla_xor = [[0, 0, 0],[0, 1, 1],[1, 0, 1],[1, 1, 0]]

    n = int(input("Cuantas neuronas quiere en la capa oculta (1 a n)? "))

    pesos_ini = []

    for i in range(n*3):
        p = float(input(f"Ingrese el peso {i}: "))
        pesos_ini.append(p)

    lista_div = []
    for i in range(0, len(pesos_ini), 3):
        lista_div.append(pesos_ini[i:i+3])

    lista_y = []
    lista_wa = []
    lista_wb = []
    lista_wc = []
    
    while c != 1:
        c += 1

        print(f"--------------------------->Iteracion {c}<------------------------------------")
        for i in tabla_xor:
            for j in lista_div:
                s_real_y = Capa_oculta().neurona_generica(i, j)
                lista_y.append(s_real_y)

    print(lista_y)

        

    

if __name__ == '__main__':
    main()