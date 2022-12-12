# -*- coding: utf-8 -*-
""" Blatt 5 - Aufgabe 4 """

import numpy as np
import matplotlib.pyplot as plt

r""" Die folgenden Funktionen sind gegeben: """


def plotSignal(x, y, pos, plotTitle, color, definitionsbereich, wertebereich):
    """
    Plottet das gegebene Signal an der gegebenen Stelle im Subplot
    :param x: x-Werte des Signals
    :param y: y-Werte des Signals
    :param pos: An welcher Position das Signal geplottet wird (1,2 oder 3)
    :param plotTitle: Beschriftung des Plots
    :param color: Farbe des Plots
    :param definitionsbereich: Definitionsbereich des Signals (x-Achse)
    :param wertebereich: Wertebreich des Signals (y-Achse)
    """
    plt.subplot(3, 1, pos)
    plt.plot(x, y, color=color)
    plt.ylim([wertebereich[0] - 0.3, wertebereich[1] + 0.3])
    plt.xlim(definitionsbereich)
    plt.grid(True, which='both')
    plt.title(plotTitle)
    plt.tight_layout()


def sigFunc(x):
    r"""Berechnet Signalwerte an Stelle(n) x und gibt diese zurück
    :param x: Zeitpunkte zu denen die Signalwerte berechnet werden sollen.
    :return: Die berechneten Signalwerte
    """
    return np.sin(2 * np.pi * 10 * x) + np.cos(2 * np.pi * 20 * x)


r"""############################################################################
Sie sind dran:
#############################################################################"""


def showFourierTransform(abtastperiode, definitionsbereich):
    r"""
    Tasten Sie das Signal aus 'sigFunc' mit der gegebenen Abtastperiode im
    Definitionsbereich ab und zeigeen Sie die DFT an.
    Sie können 'plotSignal' verwenden, um ein Signal zu plotten
    """
    # 1000 äquidistante Punkte
    x = np.linspace(definitionsbereich[0], definitionsbereich[1], num=1000)
    # berechne Funktonswerte
    y = sigFunc(x)
    # Taste 1d signal ab
    # Abtastpunkte
    xs = np.arange(definitionsbereich[0], definitionsbereich[1], np.abs(abtastperiode))
    # deren Anzahl
    N = xs.shape[0]
    print(N)
    # deren Funktionswerte
    ys = sigFunc(xs)
    wertebereich = [np.min(y), np.max(y)]
    plt.figure(figsize=(8, 10))
    plotSignal(x, y, 1, 'Originalsignal', 'm', definitionsbereich, wertebereich)
    plt.stem(xs, ys)

    # DFT
    betraege = np.empty(N)
    phasen = np.empty(N)
    for k in range(0, N):
        dft_sum = np.complex(0)
        for n in range(0, N):
            dft_sum = dft_sum + ys[n] * np.exp(-1j * 2 * np.pi * n * k / N)
        betraege[k] = np.abs(dft_sum)
        phasen[k] = np.angle(dft_sum)

    # phasen = np.where(betraege > 1e-5, phasen, 0)

    # Normierung der Betraege und Berechnung der Achsenindices.
    betraege = betraege / (N / 2)
    abtastfrequenz = 1.0 / abs(abtastperiode)
    frequenzen = np.arange(0, abtastfrequenz, abtastfrequenz / N)

    # Anzeige
    plotSignal(frequenzen, betraege, 2, "Betraege", 'm', (0, abtastfrequenz - abtastfrequenz / N), (0, 1))
    plt.xlabel("Frequenz in Hz")
    plt.stem(frequenzen, betraege)

    plotSignal(frequenzen, phasen, 3, "Phasen", 'm', (0, abtastfrequenz - abtastfrequenz / N), (-np.pi, np.pi))
    plt.xlabel("Frequenz in Hz")
    plt.stem(frequenzen, phasen)

    plt.show()


showFourierTransform(abtastperiode=0.01, definitionsbereich=[-0.2, 0.2])
