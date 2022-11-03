import cv2
import copy
import os

def read_images():
    lista_1 = []
    lista_2 = []
    persona = True
    input_images_path = "C:/Users/nahue/OneDrive/Desktop/inteligencia_artificial/tp6/fotosIA/"

    for i in range(10):
        img = cv2.imread(input_images_path + str(i) + ".jpg", cv2.COLOR_RGB2GRAY)
        for image in img:
            for i in image:
                for j in i:
                    lista_1.append(j)
                    # print(lista_1)
        print(len(lista_1))
        lista_1.clear()
                    # lista_2.append(lista_1)
        
    # return lista_2

if __name__ == '__main__':
    read_images()
    # print(len(a))