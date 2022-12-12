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

    # ... #

    plt.show()  # Zum Anzeigen des Plots am Ende


showFourierTransform(abtastperiode=0.01, definitionsbereich=[-0.2, 0.2])
