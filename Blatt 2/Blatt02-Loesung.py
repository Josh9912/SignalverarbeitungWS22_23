# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 14:12:17 2016

@author: zechadan

Der folgende Code implementiert eine erweitere Version der Mandelbrot-Übungsaufgabe, 
mit dem Sie sich mit dem Abfangen von Maus-Events vertraut machen können.
Es ist möglich, mit der Maus ein Rechteck in das Mandelbrot-Bild zu malen und 
nach der Bestätigung mit der S-Taste einen vergrößerten Bildausschnitt
neu zu berechnen.
"""

# empfohlene imports
import numpy as np
import cv2


# Implementieren Sie die Funktion CoordZuZahl, die einer Pixel-Koordinate eine
# komplexe Zahl zuweist
def CoordZuZahl(CoordX, CoordY, bildgroesse, grenzen_reell, grenzen_im):
    Re = float(grenzen_reell[0]) + \
         float(CoordX) / float(bildgroesse[0] - 1) * \
         float(grenzen_reell[1] - grenzen_reell[0])
    """ Anmerkung: Da das Koordinatensystems eines Bildes relativ zur herkömmlichen
    Betrachtung an der x-Achse gespiegelt ist, muss diese Spiegelung in die Berechung
    der komplexen Zahl berücksichtigt werden
    (siehe: CoordY wird von Bildgröße subtrahiert)."""
    Im = float(grenzen_im[0]) + \
         (float(bildgroesse[1] - 1) - float(CoordY)) / float(bildgroesse[1]-1) * \
         float(grenzen_im[1] - grenzen_im[0])

    return np.complex(Re, Im)

# Weisen Sie jeder Pixel-Koordinate im Mandelbrot-Bild eine komplexe Zahl zu und
# überprüfen Sie, ob diese Zahl divergiert.
def mandelbrot(groesse=[200, 150],
               grenzen_reell=(-2.2, 1.),
               grenzen_im=(-1.5, 1.5),
               pruef_iterationen=50):
    ergebnis = np.zeros(groesse[::-1]+[3], dtype='uint8')
    for y, zeile in enumerate(ergebnis):
        for x, pix in enumerate(zeile):
            komplexe_zahl = CoordZuZahl(x, y, groesse, grenzen_reell, grenzen_im)
            iterations_zahl = np.complex(0)
            abbruch_iteration = pruef_iterationen
            for iteration in range(pruef_iterationen):
                iterations_zahl = iterations_zahl ** 2 + komplexe_zahl
                if (np.abs(iterations_zahl) > 2.):
                    abbruch_iteration = iteration
                    break
            pix[2] = 255. * abbruch_iteration / pruef_iterationen
    return ergebnis


class Rechteck:
    """ Eine Klasse zum abspeichern eines Rechtecks. Das Rechteck ist definiert durch
        die Koordinaten der linken oberen Ecke sowie durch Höhe und Breite. Zwei
        zusätzliche Funktionen geben die linke obere Ecke und die rechte untere Ecke
        zurück und berücksichtigen dabei auch negative Werte für Höhe und Breite.
        Diese entstehen z.B. wenn das Rechteck von rechts unten nach links oben
        konstruiert wird."""
        
    def __init__(self, x_=0, y_=0, w_=0, h_=0):
        """ Konstruktor. """
        self.x = x_ # linke-obere x-Koordinate des Rechtecks
        self.y = y_ # linke-obere y-Koordinate des Rechtecks
        self.w = w_ # Breite des Rechtecks
        self.h = h_ # Höhe des Rechtecks

    def get_leftUpper(self):
        """ Gibt Koordinate der linken oberen Ecke zurück. """
        x, y = self.x, self.y # Standard-Fall
        if self.w < 0:
            x = self.x + self.w
        if self.h < 0:
            y = self.y + self.h
        return (x,y)
        
    def get_rightLower(self):
        """ Gibt Koordinate der rechten unteren Ecke zurück. """
        x, y = self.x + self.w, self.y + self.h # Standard-Fall
        if self.w < 0:
            x = self.x
        if self.h < 0:
            y = self.y
        return (x,y)         
            
    
# Hilfsfunktion: Mouse Handler zum Vergrößern von Ausschnitten    
roi = Rechteck()        # leeres, globales Rechteck definiert die "Region of interest".
isPressed = False

def markiereAusschnitt(event, x, y, flags, param):
    """ Die Parameter der Funktion sind von OpenCV vordefiniert.
        event:  Das beim Aufruf der Funktion ausgelöste Event.
        x:      Die x-Koordinate der Maus zum Zeitpunkt des Funktionsaufrufs. 
        y:      Die y-Koordinate der Maus zum Zeitpunkt des Funktionsaufrufs. 
        flags:  Zusätzlich übergebene Flags.
        param:  Zusätzlich übergebene Parameter. """
        
    global roi, isPressed      # ermöglicht Zugriff und Veränderung der Variable 'roi'
    
    # falls die linke Maustaste gedrückt wird, setze linke obere Ecke
    if event == cv2.EVENT_LBUTTONDOWN: 
        roi.x = x
        roi.y = y
        isPressed = True
        
    # falls linke Maustaste losgelassen wird
    if event == cv2.EVENT_LBUTTONUP:
        isPressed = False
        
    # falls die Linke Maustaste gehalten wird
    if isPressed:
        roi.w = x - roi.x
        roi.h = y - roi.y
    

# bindet den Maus-Handler an ein Fenster mit dem Namen "Mandelbrot Menge"
cv2.namedWindow("Mandelbrot Menge")
cv2.setMouseCallback("Mandelbrot Menge", markiereAusschnitt)

# Bildgröße und Wertebereiche
bildgroesse = [200,150]
grenzen_reell=(-2.2, 1.)
grenzen_im=(-1.5, 1.5)

# berechnet Mandelbrot Menge
mbrot = mandelbrot(groesse=bildgroesse, grenzen_reell=grenzen_reell, grenzen_im=grenzen_im, pruef_iterationen=50)

while True:
    # zeiche ein potentielles gemaltes Rechteck in ein Kopie des Mandelbrot-Bildes ein
    mbrot_copy = np.array(mbrot)
    cv2.rectangle(mbrot_copy, roi.get_leftUpper(), roi.get_rightLower(), (0, 255, 0))

    cv2.imshow("Mandelbrot Menge", mbrot_copy) # zeige Bild an

    key = cv2.waitKey(1) & 0xFF # warte 1ms auf Tastendruck
    if key == 115: # S Taste wird gedrückt
        # Wir verwenden die Funktion CoordZuZahl zur Berechnung des neuen Wertebreichs
        x1, y1 = roi.get_leftUpper()
        x2, y2 = roi.get_rightLower()
        
        left_up = CoordZuZahl(x1, y1, bildgroesse, grenzen_reell, grenzen_im)
        right_lo = CoordZuZahl(x2, y2, bildgroesse, grenzen_reell, grenzen_im)
        
        grenzen_reell_neu = (left_up.real, right_lo.real)
        grenzen_im_neu = (-right_lo.imag, -left_up.imag) # Vertauschung und Negierung wegen "umgedrehtem" Bildkoordinatensystem
        
        # berechne Mandelbrot-Menge für neuen Ausschnitt und gib' sie aus
        cv2.imshow("Mandelbrot big", mandelbrot(bildgroesse, grenzen_reell_neu, grenzen_im_neu, 50))
    if key == 27: # ESC Taste wird gedrückt
        break # beenden

cv2.destroyAllWindows()
