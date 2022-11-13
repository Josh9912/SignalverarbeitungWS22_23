#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Thu Oct 01 19:22:40 2015

@author: Anton Winschel, Dan Zecha

Mit dem folgenden Skript können Sie testen, ob Sie Anaconda und OpenCV richtig
installiert haben. Führen Sie dazu das Skript von der Kommandozeile mit "python test_script.py" aus.
Wenn sie alles richtig gemacht haben,
erscheint nach ein paar Sekunden das Bild eines Farbrads in einem neuen Fenster.
Drücken sie eine beliebige Taste um das Fenster zu schließen.

"""

import numpy as np
import cv2 as cv
import colorsys

w,h = 500,500
img = np.zeros((h,w,3), np.uint8)

for y in range(h):
    for x in range(w):
        c = np.complex(x, y) - np.complex(w/2, h/2)
        if np.abs(c) > w/2:
            img[y][x] = (0,0,0)
        else:
            hue = (np.arctan2(c.real,c.imag) + np.pi) / (2*np.pi)
            img[y][x] = np.dot(255, colorsys.hsv_to_rgb(h=hue, s=1, v=1))

cv.imshow("HSV", img)
cv.waitKey()
cv.destroyAllWindows()
