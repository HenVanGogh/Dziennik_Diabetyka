#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from Wykresy import average_of_30_measurements, average_of_chosen_day_and_month_and_year, \
    average_of_chosen_month_and_year, standard_deviation_of_30_last_measurements


class TestStatystyka(unittest.TestCase):
    def test_average_of_30_measurements(self):
        srednia = average_of_30_measurements()
        self.assertEqual('87.5 mm/Hg', srednia)

    def test_average_of_chosen_day_and_month_and_year(self):
        srednia = average_of_chosen_day_and_month_and_year('26.05.2020')
        self.assertEqual('80.0 mm/Hg', srednia)

    def test_average_of_chosen_month_and_year(self):
        srednia = average_of_chosen_month_and_year('05.2020')
        self.assertEqual('90.0 mm/Hg', srednia)

    def test_standard_deviation_of_30_last_measurements(self):
        odchylenie_stand = standard_deviation_of_30_last_measurements()
        self.assertEqual('15.77 mm/Hg', odchylenie_stand)


if __name__ == '__main__':
    unittest.main()
