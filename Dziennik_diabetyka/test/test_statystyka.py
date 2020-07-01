#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from include.wykresy import average_of_n_measurements, average_of_chosen_day_and_month_and_year, \
    average_of_chosen_month_and_year, standard_deviation_of_n_last_measurements


class TestStatystyka(unittest.TestCase):
    def test_average_of_30_measurements(self):
        srednia = average_of_n_measurements(30)
        self.assertEqual('90.0 mm/Hg', srednia)

    def test_average_of_chosen_day_and_month_and_year(self):
        srednia = average_of_chosen_day_and_month_and_year('2020-06-22')
        self.assertEqual('90.0 mm/Hg', srednia)

    def test_average_of_chosen_month_and_year(self):
        srednia = average_of_chosen_month_and_year('2020-06')
        self.assertEqual('90.0 mm/Hg', srednia)

    def test_standard_deviation_of_30_last_measurements(self):
        odchylenie_stand = standard_deviation_of_n_last_measurements(30)
        self.assertEqual('10.0 mm/Hg', odchylenie_stand)


if __name__ == '__main__':
    unittest.main()
