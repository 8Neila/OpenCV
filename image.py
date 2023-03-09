import cv2
from random import randint

img = cv2.imread('img/alpha.png', 1)

print(type(img))
print(img.shape)
print(img[0,0]) # pierwszy piksel z kolorem zapisanym w modelu BGR
# print(img[0][0]) # pierwszy piksel z kolorem zapisanym w modelu BGR
print(img[320,250]) 

# Zmiana kolorów wybranych pikseli
# for i in range(100):
#     for j in range(img.shape[1]):
#         # img[i,j] = [0, 255, 0]
#         img[i, j] = [randint(0,255), randint(0,255), randint(0,255)]

# skopiowanie części obrazka i wklejenie gdzieś indziej

fragment = img[141:199, 159:230]
w = fragment.shape
img[225:225+w[0], 159:159+w[1]] = fragment

# cv2.imshow('Image changed', fragment)
cv2.imshow('Image changed', img)
cv2.waitKey(0)
cv2.destroyAllWindows()