import numpy 
import cv2

image_name = "balckwhite.png"

#odczyt obrazu z pliku
print("Odczyt obrazu z pliku")
img = cv2.imread("/home/krzysztof/catkin_ws/src/hello_world/src/perception/img_structure/blackwhite.png")

#wyswietlenie pliku obrazu, jest on przechowywany w postaci numpy tablicy
print(img)

#typ obrazy 
print("Typ obrazu {}".format(type(img)))

#wielkosc obrazu
print("Wielkosc obrazu {}".format(img.size))

#długosc obrazu, ilosc pikseli w pionowej osi
print("Dlugosc obrazu, ilosc pikseli w pionowej osi {}".format(len(img)))

#kształt obrazu  DLUGOSC     SZEROKOSC   KANALY KOLOWROW mozna te inf wywolywac nastepujaco img.shape[i] gdzie i = 0,1,2
print("Ksztalt obrazu {}  {}  {}".format(img.shape[0], img.shape[1],img.shape[2]))

#aby odczytac pojedynczy kanal koloru
print(img[:,:,0])


