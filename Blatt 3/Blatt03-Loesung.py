""" Blatt 3 - Aufgabe 4 """

# empfohlene Imports
import numpy as np
import cv2

zeilen = 480 # Bildhöhe
spalten = 640 # Bildbreite

# Sie sind dran!

# erzeugen Sie 3 Bilder mit den Dimensionen (zeilen, spalten) vom Typ uint8, je
# eines für die ursprüngliche Funktion und je eines für die Ableitungen. Es ist
# sinnvoll, dass alle Werte im Bild ursprünglich auch 0 initiallisiert sind.
bild_f = np.empty((zeilen, spalten), dtype=np.uint8)
bild_dfdx = np.empty((zeilen, spalten), dtype=np.uint8)
bild_dfdy = np.empty((zeilen, spalten), dtype=np.uint8)

# tragen Sie die entsprechenden Funktionswerte in die Bilder ein.
for zeile in range(zeilen):
    for spalte in range(spalten):
        # Pixelwert für das Originalbild
        pixelwert = (127.5 * np.sin(0.5 * (np.pi / 640) * (((spalte - 320)**2) + ((zeile - 240)**2))) + 127.5)
        bild_f[zeile, spalte] = pixelwert

        # Pixelwert für das dx-Bild
        pixelwert = ((127.5 * np.cos(0.5 * np.pi / 640 * (((spalte - 320)**2) + ((zeile - 240)**2))) *
                     np.pi / 640.0 * (spalte - 320) + 201) / 402.0 * 255)
        bild_dfdx[zeile, spalte] = pixelwert

        # Pixelwert für das dy-Bild
        pixelwert = ((127.5 * np.cos(0.5 * np.pi / 640 * (((spalte - 320)**2) + ((zeile - 240)**2))) *
                     np.pi / 640.0 * (zeile - 240) + 151) / 302 * 255)
        bild_dfdy[zeile, spalte] = pixelwert
        
# Erstellen Sie ein Bild, das das Originalbild um den Faktor 4 verkleinert. ( Es
# soll einfach jeder 4te Pixelwert jeder Dimension in das kleine Bild 
# übernommen werden)
bild_klein = np.empty((zeilen // 4, spalten // 4), dtype=np.uint8)
for zeile in range(0, zeilen, 4):
    for spalte in range(0, spalten, 4):
        pixelwert = bild_f[zeile, spalte]
        bild_klein[zeile // 4, spalte // 4] = pixelwert
        
# zeigen Sie die Bilder an und warten sie auf einen Tastendruck bevor Sie die
# Fenster wieder schließen
cv2.imshow("bild_f", bild_f)
cv2.imshow("bild_dfdx", bild_dfdx)
cv2.imshow("bild_dfdy", bild_dfdy)
cv2.imshow("bild_klein", bild_klein)
cv2.waitKey()
cv2.destroyAllWindows()
