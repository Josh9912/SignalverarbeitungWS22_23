# -*- coding: utf-8 -*-

""" Aufgabe 7.2 """

# empfohlene Imports
import cv2
import numpy as np


# Schreiben Sie eine Funktion, die die Position eines Pixel (x,y) zuerst gemäß einer
# Translation (tx, ty) verschiebt und anschließend eine Rotation um den Winkel
# phi durchführt.
# Hinweis: Sie müssen die Koordinaten des Punkts (x,y) in homogene Koordinaten um-
# wandeln.
def transform_sequence(x, y, t_x, t_y, phi):
	pass
	# Sie sind dran!


# Schreiben Sie eine weitere Funktion, die die Position eines Pixel (x,y) gemäß
# einer Transformation M = T*R transformiert.
def transform_joint(x, y, t_x, t_y, phi):
	pass
	# Sie sind dran!

# Wie müssen Sie die Funktion abändern, damit das Ausgabebild korrekt dargestellt
# wird?
def transform_inverse(x, y, t_x, t_y, phi):
	pass
	# Sie sind dran!

# Lesen Sie ein Testbild ein und führen Sie die Transformationen in allen drei Varianten durch.
img = cv2.imread("Lenna.png")

h,w = img.shape[:2]

dst_sequence = np.zeros((h,w,3), np.uint8)
dst_joint = np.zeros((h,w,3), np.uint8)
dst_correct = np.zeros((h,w,3), np.uint8)

	# Sie sind dran!

cv2.imshow("img", img)
cv2.imshow("dst_sequence", dst_sequence)
cv2.imshow("dst_joint", dst_joint)
cv2.imshow("dst_correct", dst_correct)

cv2.waitKey()
cv2.destroyAllWindows()
