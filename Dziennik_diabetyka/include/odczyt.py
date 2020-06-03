#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

baza = {}
sPlik = "baza.txt"


def otworz(plik):
    if os.path.isfile(sPlik):
        with open(sPlik, "r") as pliktxt:
            for line in pliktxt:
                t = line.split(":")
                data = t[0]
                pomiary = t[1].replace("\n", "")
                pomiary = pomiary.split(",")
                baza[data] = pomiary

def zapisz(baza):
    # otwieramy plik do zapisu, istniejący plik zostanie nadpisany(!)
    pliktxt = open(sPlik, "w")
    for data in baza:
        # "sklejamy" znaczenia przecinkami w jeden napis
        pomiary = ",".join(baza[data])
        # wyraz_obcy:znaczenie1,znaczenie2,...
        linia = ":".join([data, pomiary])
        pliktxt.write(linia)  # zapisujemy w pliku kolejne linie
        # można też tak:
        # print(linia, file=pliktxt)
    pliktxt.close()  # zamykamy plik

def wyszukaj_po_dacie(szukana_data):
    if szukana_data in baza:
        return baza[szukana_data]
    else: return "W tym dniu nie został zrealizowany żaden pomiar"

def wyszukaj_po_pomiarze(pomiar):
    daty = []
    for key in baza.keys():
        if pomiar in baza[key]:
            daty.append(key)
    if daty == []:
        return "Taki pomiar nigdy nie został zarejestrowany"
    return daty


otworz(sPlik)
szukana_data = "2020-05-30"
print(baza[szukana_data])
pomiar = "76"
print(wyszukaj_po_pomiarze(pomiar))
