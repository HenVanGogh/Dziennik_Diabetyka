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

def average_of_30_measurements():
    f = open('pomocniczy.txt', 'r', encoding=" utf -8")
    z = f.readlines()
    y = []
    for line in range(len(z)-1, -1, -1):
        a = z[line]
        y.append(int(a[49]+a[50]))
    for i in range(len(z)-30):
        del y[i+30]
    suma = sum(y)
    liczba = len(y)
    f.close()
    return suma/liczba

def average_of_50_measurements():
    f = open('pomocniczy.txt', 'r', encoding=" utf -8")
    z = f.readlines()
    y = []
    for line in range(len(z)-1, -1, -1):
        a = z[line]
        y.append(int(a[49]+a[50]))
    for i in range(len(z)-50):
        del y[i+50]
    suma = sum(y)
    liczba = len(y)
    f.close()
    return suma/liczba

def average_of_100_measurements():
    f = open('pomocniczy.txt', 'r', encoding=" utf -8")
    z = f.readlines()
    y = []
    for line in range(len(z)-1, -1, -1):
        a = z[line]
        y.append(int(a[49]+a[50]))
    for i in range(len(z)-100):
        del y[i+100]
    suma = sum(y)
    liczba = len(y)
    f.close()
    return suma/liczba

def average_of_chosen_month_and_year(data : str):
    f = open('pomocniczy.txt', 'r', encoding=" utf -8")
    z = f.readlines()
    y = []
    for line in range(len(z)):
        a = z[line]
        if data == a[11:18]:
            y.append(int(a[49] + a[50]))
    suma = sum(y)
    liczba = len(y)
    f.close()
    return suma / liczba

graph_of_last_30_measurments()