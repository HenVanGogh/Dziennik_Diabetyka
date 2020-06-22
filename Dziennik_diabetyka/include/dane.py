#!/usr/bin/python
# -*- coding: utf-8 -*-

from dziennik import Wpis

def dodaj_wpis( poziom_cukru, numer_pomiaru):
    plik = open('baza.txt','a')
    nowy_wpis = Wpis(poziom_cukru,numer_pomiaru)
    str = nowy_wpis.__str__()
    plik.write(str)
    plik.close()
