import cv2
import copy

def leer_imagenes():
    imagenes = []
    aux = []
    a = True
    input_images_path = "C:/Users/nahue/OneDrive/Desktop/inteligencia_artificial/tp6/fotosIA/"
    for i in range(10):
        img = cv2.imread(input_images_path + str(i) + ".jpg", cv2.COLOR_RGB2GRAY)
        aux.clear()
        for j in range(len(img)):
            for k in range(len(img[0])):
                px = img[j][k][0]
                aux.append(px/255)

        if a:
            aux.append(int(0))
            a = False
        else:
            aux.append(1)
            a = True
            
        imagenes.append(copy.deepcopy(aux))

    return imagenes