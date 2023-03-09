import cv2

cap = cv2.VideoCapture(0) # indeks przechwytywanej kamery, jezeli komputer ma jedną kamerę to będzie to ta jedna (pierwsza)
# można także podać nazwę pliku w którym znajduje się film

while True:
    ret, frame = cap.read()
    # ret - informuje czy kamera jest czy nie jest zajęta (np. przez inny proces), jezeli nie jest wazny można zastąpić `_`
    # frame to faktycznie przechwytywane klatki

    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) == ord('q'): # nigdy 0, im wyżej tym większe lagi
        break

cap.release() # zwolnij kamerę
cv2.destroyAllWindows()