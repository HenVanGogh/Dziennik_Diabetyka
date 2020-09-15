#!/usr/bin/python
# -*- coding: utf-8 -*-
from include.dziennik import Wpis
import datetime


def dodaj_wpis(poziom_cukru: float, year=None, month=None, day=None) -> None:
    plik = open('baza.csv', 'a', encoding=" utf -8")
    if year is None:
        nowy_wpis = Wpis(poziom_cukru, ktory_to_dzis_pomiar(str(datetime.datetime.today()).split()[0]))
    else:
        nowy_wpis = Wpis(poziom_cukru, ktory_to_dzis_pomiar(str(year + "-" + month + "-" + day)),
                         str(year + "-" + month + "-" + day))
    print(nowy_wpis)
    dodac = str(nowy_wpis)
    plik.write(dodac)
    plik.close()


def ktory_to_dzis_pomiar(data: str) -> int:
    measurment_number = 1
    f = open('baza.csv', 'r', encoding=" utf -8")
    wiersze = f.readlines()
    wyp = []
    for line in range(len(wiersze)):
        pom = wiersze[line]
        wyp.append(pom.split(','))
        if data == wyp[0][0][6:16]:  # porównanie czy przekazany parametr zgadza się z datą danego wpisu w bazie
            measurment_number += 1
        del wyp[0]
    return measurment_number