import numpy as np
import cv2


def coord_zu_zahl(CoordX, CoordY, bildgroesse, grenzen_reell, grenzen_im):

    re_diff =  grenzen_reell[1] - grenzen_reell[0]
    im_diff =  grenzen_im[1] - grenzen_im[0]

    Re = (CoordX / bildgroesse[0]) + re_diff + grenzen_reell[0]
    Im = (CoordY / bildgroesse[1]) + im_diff + grenzen_im[0]

    return np.complex(Re, Im)


def mandelbrot(groesse=[200, 150],
               grenzen_reell=(-2., 1.),
               grenzen_im=(-1.1, 1.1),
               pruef_iterationen=50):
    erg = np.zeros(groesse[::-1] + [3], dtype='uint8')

    return erg


cv2.imshow("Mandelbrot Menge", mandelbrot([200, 150]))
cv2.waitKey()
cv2.destroyAllWindows()