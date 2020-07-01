#!/usr/bin/python
# -*- coding: utf-8 -*-

from include.losowanie_zartu_z_pliku import say_a_joke
from include.dane import dodaj_wpis
from include.wykresy import graph_of_last_30_measurments, measurments_from_chosen_day_and_month_and_year,\
    measurments_from_chosen_month_and_year


print(measurments_from_chosen_day_and_month_and_year("2020-06-22"))
print(measurments_from_chosen_month_and_year("2020-06"))
