# https://youtube.com/playlist?list=PLzMcBGfZo4-lUA8uGjeXhBUUzPYc6vZRn
# pip install opencv-python v python -m pip install opencv-python

import cv2

# Wczytanie obrazu z opcjami parametru `flag`:
# cv2.IMREAD_COLOR: It specifies to load a color image, loads the image in the BGR 8-bit format. Any transparency of image will be neglected. It is the default flag. Alternatively, we can pass integer value 1 for this flag.
# cv2.IMREAD_GRAYSCALE: It specifies to load an image in grayscale mode. Alternatively, we can pass integer value 0 for this flag.
# cv2.IMREAD_UNCHANGED: It specifies to load an image as such including alpha channel. Alternatively, we can pass integer value -1 for this flag.

img = cv2.imread('img/most.jpg')

img_s = cv2.resize(img, (200, 200)) # (0,0), fx=0.5, fy=0.5 do zmian proporcjonalnych
img_r = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# inne https://medium.com/@deepak.engg.phd/opencv-images-handling-593918a8c126

cv2.imwrite('img/nowy.jpg', img_r)

cv2.imshow('Original image', img)  # pierwszy parametr to nazwa okna
cv2.imshow('Small image', img_s) # pierwszy parametr to nazwa okna
cv2.imshow('Image rotated', img_r)  # pierwszy parametr to nazwa okna
cv2.waitKey(0)  # milliseconds czekania, `0` oznacza nieskończenie długo
cv2.destroyAllWindows()
