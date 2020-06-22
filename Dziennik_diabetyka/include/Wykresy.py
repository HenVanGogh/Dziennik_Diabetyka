#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
from matplotlib import pyplot as plt
from matplotlib import style

def graph_of_last_30_measurments():

    style.use("bmh")
    f = open('pomocniczy.csv', 'r', encoding=" utf -8")  # otwarcie pliku do odczytu
    wiersze = f.readlines()  # lista zawierająca kolejne wiersze z naszej bazy
    x = [i for i in range(1, len(wiersze) + 1)]  # lista kolejnych liczb całkowitych od 1 do ilości wierszy w bazie
    wartosci_pom = []  # lista do której będą trafiały wartości poziomu cukru
    wyp = []  # lista pomocnicza do wypakowania wpisu
    # listy pomocnicze c1,c2 będą wskazywały min. i max. dopuszczalny poziom cukru w normie na powstałym wykresie
    c1 = [70 for i in range(len(wiersze))]
    c2 = [99 for i in range(len(wiersze))]
    for line in range(len(wiersze) - 1, -1, -1):
        pom = wiersze[line]  # wypakowanie danego wiersza do zmiennej a
        wyp.append(pom.split(','))  # podział ze względu na przecinki w wpisie i wpisanie do listy pomocniczej wyp
        wartosci_pom.append(
            int(wyp[0][3][15] + wyp[0][3][16] + wyp[0][3][17]))  # sklejenie odpowiednich danych wraz z konwersją na int
        del wyp[0]
    for i in range(len(wiersze) - 30):
        del wartosci_pom[i + 30]  # usunięcie niepotrzebnych pomiarów
    wartosci_pom.reverse()
    # narysowanie wykresu z wykorzystaniem matplotliba
    plt.plot(x, wartosci_pom, 'g', x, c1, '--', x, c2, '--', linewidth=5)
    plt.title("Wykres 30 pomiarów")
    plt.ylabel("Poziom cukru [mm/dl]")
    plt.xlabel("Pomiar")
    plt.legend(["Wykres pomiarów cukru", "Min. dopuszczalna wartość cukru", "Max. dopuszczalna wartość cukru"], loc='upper right')
    plt.grid(True, color='k')
    plt.show()
    f.close()

def average_of_30_measurements():
    f = open('pomocniczy.csv', 'r', encoding=" utf -8")  # otwarcie pliku do odczytu
    wiersze = f.readlines()  # lista zawierająca kolejne wiersze z naszej bazy
    wartosci_pom = []  # lista do której będą trafiały wartości poziomu cukru
    wyp = []  # lista pomocnicza do wypakowania wpisu
    for line in range(len(wiersze) - 1, -1, -1):
        pom = wiersze[line]  # wypakowanie danego wiersza do zmiennej pomocniczej a
        wyp.append(pom.split(','))  # podział ze względu na przecinki w wpisie i wpisanie do listy pomocniczej wyp
        wartosci_pom.append(
            int(wyp[0][3][15] + wyp[0][3][16] + wyp[0][3][17]))  # sklejenie odpowiednich danych wraz z konwersją na int
        del wyp[0]
    for i in range(len(wiersze) - 30):
        del wartosci_pom[i + 30]  # usunięcie niepotrzebnych pomiarów
    suma = sum(wartosci_pom)
    ilosc = len(wartosci_pom)
    f.close()
    return str(suma / ilosc) + " mm/Hg"

def average_of_50_measurements():
    f = open('pomocniczy.csv', 'r', encoding=" utf -8")
    wiersze = f.readlines()
    wartosci_pom = []
    wyp = []
    for line in range(len(wiersze) - 1, -1, -1):
        pom = wiersze[line]
        wyp.append(pom.split(','))
        wartosci_pom.append(int(wyp[0][3][15] + wyp[0][3][16] + wyp[0][3][17]))
        del wyp[0]
    for i in range(len(wiersze) - 50):
        del wartosci_pom[i + 50]
    suma = sum(wartosci_pom)
    ilosc = len(wartosci_pom)
    f.close()
    return str(suma / ilosc) + " mm/Hg"

def average_of_100_measurements():
    f = open('pomocniczy.csv', 'r', encoding=" utf -8")
    wiersze = f.readlines()
    wartosci_pom = []
    wyp = []
    for line in range(len(wiersze) - 1, -1, -1):
        pom = wiersze[line]
        wyp.append(pom.split(','))
        wartosci_pom.append(int(wyp[0][3][15] + wyp[0][3][16] + wyp[0][3][17]))
        del wyp[0]
    for i in range(len(wiersze) - 100):
        del wartosci_pom[i + 100]
    suma = sum(wartosci_pom)
    ilosc = len(wartosci_pom)
    f.close()
    return str(suma / ilosc) + " mm/Hg"

def average_of_chosen_day_and_month_and_year(data : str):
    f = open('pomocniczy.csv', 'r', encoding=" utf -8")
    wiersze = f.readlines()
    wartosci_pom = []
    wyp = []
    for line in range(len(wiersze)):
        pom = wiersze[line]
        wyp.append(pom.split(','))
        if data == wyp[0][1][7:17]: # porównanie czy przekazany parametr zgadza się z datą danego wpisu w bazie
            wartosci_pom.append(int(wyp[0][3][15] + wyp[0][3][16] + wyp[0][3][17]))
        del wyp[0]
    suma = sum(wartosci_pom)
    ilosc = len(wartosci_pom)
    f.close()
    return str(suma / ilosc) + " mm/Hg"


def average_of_chosen_month_and_year(data : str):
    f = open('pomocniczy.csv', 'r', encoding=" utf -8")
    wiersze = f.readlines()
    wartosci_pom = []
    wyp = []
    for line in range(len(wiersze)):
        pom = wiersze[line]
        wyp.append(pom.split(','))
        if data == wyp[0][1][10:17]:  # porównanie czy przekazany parametr zgadza się z datą danego wpisu w bazie
            wartosci_pom.append(int(wyp[0][3][15] + wyp[0][3][16] + wyp[0][3][17]))
        del wyp[0]
    suma = sum(wartosci_pom)
    ilosc = len(wartosci_pom)
    f.close()
    return str(suma / ilosc) + " mm/Hg"

def standard_deviation_of_30_last_measurements():
    f = open('pomocniczy.csv', 'r', encoding=" utf -8")
    wiersze = f.readlines()
    wartosci_pom = []
    wyp = []
    for line in range(len(wiersze) - 1, -1, -1):
        pom = wiersze[line]
        wyp.append(pom.split(','))
        wartosci_pom.append(int(wyp[0][3][15] + wyp[0][3][16] + wyp[0][3][17]))
        del wyp[0]
    for i in range(len(wiersze) - 30):
        del wartosci_pom[i + 30]
    srednia = sum(wartosci_pom) / len(wartosci_pom)
    suma_roznic = 0
    for elem in wartosci_pom:
        suma_roznic = suma_roznic + (elem - srednia) ** 2  # wyznaczenie sumy kwadratów różnic danego pomiaru od wartości średniej
    odchylenie_stand = round(math.sqrt(suma_roznic / len(wartosci_pom)),  2)  # obliczenie pierwiastka z obliczonej powyżej sumy i zaokrąglenie jej do 2 miejsc po przecinku
    f.close()
    return str(odchylenie_stand) + " mm/Hg"

def standard_deviation_of_50_last_measurements():
    f = open('pomocniczy.csv', 'r', encoding=" utf -8")
    wiersze = f.readlines()
    wartosci_pom = []
    wyp = []
    for line in range(len(wiersze) - 1, -1, -1):
        pom = wiersze[line]
        wyp.append(pom.split(','))
        wartosci_pom.append(int(wyp[0][3][15] + wyp[0][3][16] + wyp[0][3][17]))
        del wyp[0]
    for i in range(len(wiersze) - 50):
        del wartosci_pom[i + 50]
    srednia = sum(wartosci_pom) / len(wartosci_pom)
    suma_roznic = 0
    for elem in wartosci_pom:
        suma_roznic = suma_roznic + (elem - srednia) ** 2
    odchylenie_stand = round(math.sqrt(suma_roznic / len(wartosci_pom)), 2)
    f.close()
    return str(odchylenie_stand) + " mm/Hg"

def standard_deviation_of_100_last_measurements():
    f = open('pomocniczy.csv', 'r', encoding=" utf -8")
    wiersze = f.readlines()
    wartosci_pom = []
    wyp = []
    for line in range(len(wiersze) - 1, -1, -1):
        pom = wiersze[line]
        wyp.append(pom.split(','))
        wartosci_pom.append(int(wyp[0][3][15] + wyp[0][3][16] + wyp[0][3][17]))
        del wyp[0]
    for i in range(len(wiersze) - 100):
        del wartosci_pom[i + 100]
    srednia = sum(wartosci_pom)/len(wartosci_pom)
    suma_roznic = 0
    for elem in wartosci_pom:
         suma_roznic = suma_roznic + (elem - srednia)**2
    odchylenie_stand = round(math.sqrt(suma_roznic/len(wartosci_pom)), 2)
    f.close()
    return str(odchylenie_stand) + " mm/Hg"

