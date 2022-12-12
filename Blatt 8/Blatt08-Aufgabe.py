""" Multimedia Grundlagen 1 - Programmieraufgaben Blatt 08 """
import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib.cm as cm

"""
Implementieren Sie die folgenden Funktionen.
"""

#############
# Aufgabe 2 #
#############

def calculateHistogram(image, B) :
    r"""
    Berechnet das Histogramm eines Einkanalbildes mit
    `B` bins.
    """
	pass

def calculateColorHistogram(image, B) :
    r"""
    Berechnet das Histogramm eines Farbbildes mit
    drei Kanälen.
    """
	pass 
	
def drawHistogram(hist, color):
    r"""
    Zeichnet ein Einkanalhistogramm.
    """
    pass

def drawHistogramsOfImage(image, bins) :
    r"""
    Visualisiert das Histogramm für das gegebene Bild.
    """
    pass

image_gray = cv2.imread("lenna.png", cv2.IMREAD_GRAYSCALE)
drawHistogramsOfImage(image_gray, 64)

image = cv2.imread("lenna.png", cv2.IMREAD_COLOR)
drawHistogramsOfImage(image, 256)
plt.show()

#############
# Aufgabe 3 #
#############

def convertToLuminance(image_src):
    r"""
    Konvertiert ein Bild so, dass jedes Pixel der
    Leuchtdichte entspricht.
    """
    pass


image_luminance = convertToLuminance(image)

plt.figure(1)
plt.imshow(image[:,:,(2,1,0)])

plt.figure(2)
plt.imshow(image_luminance, cmap=cm.gray, vmin=0, vmax=255)


#############
# Aufgabe 4 #
#############

def normalizeHistogram(image):
    r"""
    Normalisiert ein Graustufenbild auf den Wertebereich [0;255].
    """
	# Sie sind dran!
    pass

def normalizeHistogramWithCutOff(image, cut_off_percentage):
    r"""
    Normalisiert ein Graustufenbild auf den Wertebereich [0;255].
    Zusätzlich werden 'cut_off_percentage' Prozent der Randpixel im Histogramm ignoriert.
    """
	# Sie sind dran!
    pass


image = cv2.imread('overflow.bmp', flags=cv2.IMREAD_GRAYSCALE)
if image is None:
    print('Das Einlesen hat nicht funktioniert!')
else:
    image_normalized1 = normalizeHistogram(image)
    cut_off = 0.05
    image_normalized2 = normalizeHistogramWithCutOff(image, cut_off)

    # Anzeige
    cv2.imshow("Original", image)
    cv2.imshow("Normalisiert", image_normalized1)
    cv2.imshow("Normalisiert mit " + str(cut_off) + " Prozent cut-off", image_normalized2)

    cv2.waitKey()
    cv2.destroyAllWindows()


