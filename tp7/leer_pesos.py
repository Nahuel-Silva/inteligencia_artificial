def leer_pesos():
    list_pesos = []
    list_pesos2 = []
    with open('pesos.txt', 'r') as pesos:
        for line in pesos:
            list_pesos.append(float(line))
    with open('pesos2.txt', 'r') as pesos:
        for line in pesos:
            list_pesos2.append(float(line))
    return (list_pesos),(list_pesos2)