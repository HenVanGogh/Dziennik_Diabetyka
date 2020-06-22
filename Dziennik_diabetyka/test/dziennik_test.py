#!/usr/bin/python
# -*- coding: utf-8 -*-


import datetime
import unittest
import sys
sys.path.append("../include")
from dziennik import Wpis as Wpis_test


class MyTestCase(unittest.TestCase):
    def test_czy_w_normie(self):
        wpis_za_wysoki = Wpis_test(100, 1)
        wpis_w_normie = Wpis_test(80, 2)
        wpis_za_niski = Wpis_test(50, 3)
        self.assertEqual(wpis_za_wysoki.czy_w_normie(), "za wysoki cukier")
        self.assertEqual(wpis_w_normie.czy_w_normie(), "cukier w normie")
        self.assertEqual(wpis_za_niski.czy_w_normie(),"za niski cukier")

    def test_pojedynczy_wpis(self):
        wpis_1 = Wpis_test(80.1, 1)
        self.assertEqual(wpis_1.poziom_cukru, 80.1)
        self.assertEqual(wpis_1.numer_pomiaru, 1)
        self.assertEqual(wpis_1.data, str(datetime.datetime.today()).split()[0])
        self.assertEqual(wpis_1.czy_w_normie(), "cukier w normie")
        self.assertEqual(str(wpis_1), "data: " + wpis_1.data +
                         ", pomiar nr " + str(wpis_1.numer_pomiaru) +
                         ", poziom cukru: " + str(wpis_1.poziom_cukru) +
                         ", " + wpis_1.czy_w_normie() + "\n")


if __name__ == '__main__':
    unittest.main()
