#!/usr/bin/python
# -*- coding: utf-8 -*-

from dziennik import Wpis

plik = open('baza.txt','a')
poziom_cukru = int(input("Podaj poziom cukru: "))
numer_pomiaru = int(input("Podaj numer pomiaru: "))
nowy_wpis = Wpis(poziom_cukru,numer_pomiaru)
str = nowy_wpis.__str__()
plik.write(str)
plik.close()