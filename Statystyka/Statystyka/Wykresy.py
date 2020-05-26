#!/usr/bin/python
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from matplotlib import style

def graph_of_last_30_measurments():

    style.use("bmh")

    x = [i for i in range(1, 9)]
    f = open('pomocniczy.txt', 'r', encoding=" utf -8")
    y = []
    z = f.readlines()
    c1 = [70 for i in range(len(z))]
    c2 = [99 for i in range(len(z))]
    for line in range(len(z)-1, -1, -1):
        a = z[line]
        y.append(int(a[49]+a[50]))

    y.reverse()
    plt.plot(x, y, 'g',  x, c1, '--', x, c2, '--',  linewidth=5)
    plt.title("Wykres 30 pomiarów")
    plt.ylabel("Poziom cukru [mm/dl]")
    plt.xlabel("Pomiar")
    plt.legend(["Wykres pomiarów cukru","Wartość minimalna","Wartość maksymalna"], loc='upper right')
    plt.grid(True, color='k')
    plt.show()
    f.close()

graph_of_last_30_measurments()