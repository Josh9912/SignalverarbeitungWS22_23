import numpy as np
import cv2

""" Aufgabe 1.3 """

# Definieren Sie eine Funktion, die ein Bild übergeben bekommen und eine
# eine um 90° gedrehte Version zurückgibt.
def rot90(image):
    hoehe = image.shape[0]
    breite = image.shape[1]
    result = np.empty((breite, hoehe, 3), dtype="uint8")
    for y in range(hoehe):
        for x in range(breite):
            result[breite - x - 1, y] = image[y, x]
    return result

# lesen Sie ein Testbild ein.
image = cv2.imread("lenna.png")#, cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Das Einlesen hat nicht funktioniert!")

# Rotieren Sie das Testbild mit ihrer Funktion
rotated = rot90(image)

# Zeigen Sie beide Bilder an
cv2.imshow("original", image)
cv2.imshow("rotated", rotated)
cv2.waitKey()

# Mit welcher OpenCV Funktion können Sie das gleiche Ergebnis erreichen?
# Mit OpenCV warpAffine
M = cv2.getRotationMatrix2D((image.shape[1]//2, image.shape[0]//2), 90, 1.)
cv2.imshow("warpAffine", cv2.warpAffine(image, M, (image.shape[1], image.shape[0])))

# Mit OpenCV transpose
cv2.imshow("transpose", cv2.transpose(np.fliplr(image)))

cv2.waitKey()

cv2.destroyAllWindows()
