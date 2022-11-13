# coding: utf-8
# Programmieraufgaben Übungsblatt 4
# =================================
# # Aufgabe 4 - Signalrekonstruktion

# Die folgenden imports werden empfohlen:
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


r""" Die folgenden Funktionen sind gegeben: """

# Das ist eine moegliche Implementierung der `sinc`-Funktion. Die Funktion wird an
# allen Stellen t berechnet, mit der Abtastperiode T und hat ihr globales
# Maximum an dem x-Wert offset.
def sinc(t, T, offset):
    r"""Berechnet die `sinc` Funktion."""
    x = np.pi * (t-offset) / T
    y = np.ones(x.shape)
    x_mask = x != 0
    y[x_mask] = np.sin(x[x_mask]) / x[x_mask]
    return y


r"""############################################################################
Sie sind dran:
#############################################################################"""

# Definieren Sie die Funktion `sigFunc(x)` zum Berechnen des Signals aus Blatt 3
# Aufgabe 3 an einer oder mehreren gegebenen Stellen `x` (`x` soll auch ein
# Vektor sein dürfen).
def sigFunc(x):
    r"""Berechnet Signalwerte an Stelle(n) x und gibt diese zurück
    :param x: Zeitpunkte zu denen die Signalwerte berechnet werden sollen.
    :return: Die berechneten Signalwerte
    """
    # ... #



def reconstruct(x, xs, ys, abtastperiode, n):
    """
    Rekonstruieren Sie das Signal y (definiert zu den Zeiten x) mithilfe der ersten n Abtastwerte in ys.
    :param x: Zeiten zu denen das Originalsignal definiert ist
    :param xs: Abtastzeitpunkte des abgetastetetn Signals
    :param ys: Funktionswerte des abgetasteten Signals
    :param abtastperiode: Abtastperiode (T)
    :param n: Anzahl an Abtastwerten, die zur Rekonstruktion verwendet werden sollen.
    :return: Das rekonstruierte Signal yr
    """
    yr = np.zeros(x.shape)

    # ... #

    return yr


# Definieren Sie die Funktion `showReconstruction`. Tasten sie zuerst das in der
# Funktion sigFunc erzeugte Signal ab.  Rekonstruieren Sie das Signal dann analog zur Vorlesung
# "Digitale Signale", Folien zur Rekonstruktion (speziell: "Grundidee der Rekonstruktion")
def showReconstruction(abtastperiode, definitionsbereich):
    r"""
    Tastet ein Signal mit der gegebenen Abtastperiode im
    Wertebereich ab und zeigt das rekonstruierte Signal
    für verschieden viele Abtastwerte an.
    :param abtastperiode: Abtastperiode (T)
    :param definitionsbereich: Definitionsbereich in dem das Originalsignal betrachtet und abgetastet wird
    """
    # 1000 äquidistante Punkte
    x = np.linspace(definitionsbereich[0], definitionsbereich[1], num=1000)
    # berechne Funktonswerte
    y = # ... #

    # Taste 1d signal ab
    # Abtastpunkte
    xs = # ... #
    # Funktionswerte der Abtastpunkte
    ys = # ... #
    # Anzahl der Abtastpunkte
    N = # ... #

    # Visualisierung der Rekonstruktion
    # AB HIER MUESSEN SIE NICHTS MEHR AN DIESER FUNKTION AENDERN !!!
    wertebereich = [np.min(y), np.max(y)]
    fig = plt.figure()
    axes = [plt.subplot2grid((3, 1), (i, 0), fig=fig) for i in range(3)]

    axes[0].plot(x, y)
    axes[0].stem(xs, ys, "-")
    axes[0].set_title("Originalsignal")
    reconstruction_plot, = axes[1].plot(x, np.zeros(x.shape), color="g")
    diff_plot, = axes[2].plot(x, y, color="r")

    for ax in axes:
        ax.set_xlim(definitionsbereich)
        ax.set_ylim([wertebereich[0] - 0.3, wertebereich[1] + 0.3])

    plt.tight_layout()

    def animate_reconstruction(n):
        yr = reconstruct(x, xs, ys, abtastperiode=abtastperiode, n=n)
        reconstruction_plot.set_data(x, yr)
        axes[1].set_title("Rekonstruktion mittels der ersten {} Werte".format(n))
        diff_plot.set_data(x, y - yr)
        axes[2].set_title("Rekonstruktionsfehler nach den ersten {} Werten".format(n))

        return [reconstruction_plot, diff_plot]

    ani = FuncAnimation(fig, func=animate_reconstruction, frames=N+1, interval=500, blit=False, repeat=False)
    plt.show()


# Zeigen sie die Visualisierung der Rekonstruction an.
# Testen Sie verschiedene Abtastperioden.
# Achtung: Wenn Sie die Abtastperiode vergroessern, sollten Sie auch den Dargestellten Definitionsbereich vergroessern.
showReconstruction(abtastperiode=0.01, definitionsbereich=[-0.2, 0.2])


