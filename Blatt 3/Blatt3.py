""" Blatt 3 - Aufgabe 4 """
import numpy as np
import cv2
import math

zeilen = 480  # Bildhöhe
spalten = 640  # Bildbreite


def picture(row, col) -> np.array:
    res = np.zeros((row, col), dtype=np.uint8)
    for x in range(row):
        for y in range(col):
            res[x, y] = f(x, y)
    return res


def der_x(row, col) -> np.array:
    res = np.zeros((row, col), dtype=np.uint8)
    for x in range(row):
        for y in range(col):
            res[x, y] = der_f_x(x, y)
    return res


def der_y(row, col) -> np.array:
    res = np.zeros((row, col), dtype=np.uint8)
    for x in range(row):
        for y in range(col):
            res[x, y] = der_f_y(x, y)
    return res


def down_smpl(inp):
    return cv2.resize(inp, (inp.shape[1] // 4, inp.shape[0] // 4))


def f(x, y):
    return 127.5 * math.sin(
        (1 / 2) * math.pi * ((math.pow((x - 320), 2) + math.pow((y - 240), 2)) / 640)) + 127.5


def der_f_x(x, y):
    return (51 * math.pi * (x - 320) * math.cos(
        (math.pi * (math.pow((x - 320), 2) + math.pow((y - 240), 2))) / 1280)) / 256


def der_f_y(x, y):
    return (51 * math.pi * (y - 240) * math.cos(
        (math.pi * (math.pow((x - 320), 2) + math.pow((y - 240), 2))) / 1280)) / 256


if __name__ == "__main__":
    cv2.imshow("pic", picture(zeilen, spalten))
    cv2.imshow("pic_ds", down_smpl(picture(zeilen, spalten)))
    cv2.imshow("der_x", der_x(zeilen, spalten))
    cv2.imshow("der_y", der_y(zeilen, spalten))
    cv2.waitKey(0)