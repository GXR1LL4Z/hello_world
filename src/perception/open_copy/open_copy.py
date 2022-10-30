import numpy
import cv2

image_name = "knr"

print("Odczyt obrazu z pliku")
img = cv2.imread("/home/krzysztof/catkin_ws/src/hello_world/src/perception/open_copy/"+image_name+".jpg")

print("Stworz miejsce dla obrazu")
cv2.namedWindow("Image", cv2.WINDOW_AUTOSIZE)

print("Wyswietl obraz")
cv2.imshow("Image", img)

print("Nacisnij klawisz 0 aby zrobic kopie")
cv2.waitKey(0)

#print("Obraz skopiowano do folderu copy")
#cv2.imwrite("/home/krzysztof/catkin_ws/src/hello_world/src/perception/copy/" + image_name + ".jpg", img)