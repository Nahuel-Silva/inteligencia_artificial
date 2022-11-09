import cv2
import copy

def leer_imagenes():
    imagenes = []
    aux = []
    a = True
    input_images_path = "C:/Users/nahue/OneDrive/Desktop/inteligencia_artificial/tp7/fotosIA2/"
    for i in range(6):
        img = cv2.imread(input_images_path + str(i) + ".jpg", 0)
        ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) 
        aux.clear()
        aux.append(int(1))
        for j in range(len(img)):
            for k in range(len(img[j])):
                px = img[j][k]
                if px == 0:
                    aux.append(int(0))
                else:
                    aux.append(int(1))

        if a:
            aux.append(int(0))
            a = False
        else:
            aux.append(1)
            a = True
            
        imagenes.append(copy.deepcopy(aux))

    return imagenes