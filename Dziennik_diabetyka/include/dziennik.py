#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime


class Wpis:
    def __init__(self, poziom_cukru: float, numer_pomiaru: int, date=None):
        self.poziom_cukru = poziom_cukru
        self.numer_pomiaru = numer_pomiaru
        if date is None:
            self.data = str(datetime.datetime.today()).split()[0]
        else:
            self.data = date

    def czy_w_normie(self) -> str:
        if 70 <= self.poziom_cukru <= 99:
            return "cukier w normie"
        elif self.poziom_cukru < 70:
            return "za niski cukier"
        else:
            return "za wysoki cukier"

    def __str__(self) -> str:
        reprezentacja_wpisu = "data: " + self.data + ", pomiar nr " + str(self.numer_pomiaru) + \
                              ", poziom cukru: " + str(self.poziom_cukru) + ", " \
                              + self.czy_w_normie() + "\n"
        return reprezentacja_wpisu
