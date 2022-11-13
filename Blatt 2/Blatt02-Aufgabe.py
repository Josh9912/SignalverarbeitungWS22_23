r""" Blatt 2 """

# empfohlene imports
import numpy as np
import cv2

# Implementieren Sie die Funktion CoordZuZahl, die einer Pixel-Koordinate eine
# komplexe Zahl zuweist
def CoordZuZahl(CoordX, CoordY, bildgroesse, grenzen_reell, grenzen_im):

	# Sie sind dran!
	
    return np.complex(Re, Im)

# Weisen Sie jeder Pixel-Koordinate im Mandelbrot-Bild eine komplexe Zahl zu und
# überprüfen Sie, ob diese Zahl divergiert.
def mandelbrot(groesse=[200, 150],
               grenzen_reell=(-2., 1.),
               grenzen_im=(-1.1, 1.1),
               pruef_iterationen=50):
    ergebnis = np.zeros(groesse[::-1]+[3], dtype='uint8')
	
	# Sie sind dran!
	
    return ergebnis

cv2.imshow("Mandelbrot Menge", mandelbrot([200, 150]))
cv2.waitKey()
cv2.destroyAllWindows()