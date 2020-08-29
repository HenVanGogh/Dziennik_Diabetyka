#!/usr/bin/python
# -*- coding: utf-8 -*-

from include.losowanie_zartu_z_pliku import say_a_joke
from include.dane import dodaj_wpis
from include.wykresy import measurments_from_chosen_day_and_month_and_year, graph_of_last_30_measurments
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QSizePolicy, QStyleFactory,
                             QTableWidget, QTabWidget, QVBoxLayout, QWidget, QTextBrowser)
import os


class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.textbox_joke = QTextBrowser(self)
        self.textbox_day = QLineEdit(self)
        self.textbox_month = QLineEdit(self)
        self.textbox_year = QLineEdit(self)
        self.textbox_found_measurments = QTextBrowser(self)
        self.textbox_measurment = QLineEdit(self)
        self.AddMeasurmentGroupBox = QGroupBox("Dodaj nowy pomiar")
        self.SearchingGroupBox = QGroupBox("Przeszukiwanie bazy")
        self.JokesGroupBox = QGroupBox("Kącik rozrywkowy")
        self.StatisticsGroupBox = QGroupBox("Statystyka")
        self.originalPalette = QApplication.palette()

        style_combo_box = QComboBox()
        style_combo_box.addItems(QStyleFactory.keys())

        style_label = QLabel("&Style:")
        style_label.setBuddy(style_combo_box)

        self.useStylePaletteCheckBox = QCheckBox("&Use style's standard palette")
        self.useStylePaletteCheckBox.setChecked(True)

        disable_widgets_check_box = QCheckBox("&Disable widgets")

        self.createAddMeasurmentGroupBox()
        self.createSearchingGroupBox()
        self.createJokesGroupBox()
        self.createStatisticsGroupBox()
        self.useStylePaletteCheckBox.toggled.connect(self.changePalette)
        disable_widgets_check_box.toggled.connect(self.AddMeasurmentGroupBox.setDisabled)

        top_layout = QHBoxLayout()
        top_layout.addWidget(style_label)
        top_layout.addWidget(style_combo_box)
        top_layout.addStretch(3)
        top_layout.addWidget(self.useStylePaletteCheckBox)
        top_layout.addWidget(disable_widgets_check_box)

        main_layout = QGridLayout()
        main_layout.addWidget(self.AddMeasurmentGroupBox, 0, 0)
        main_layout.addWidget(self.SearchingGroupBox, 1, 0)
        main_layout.addWidget(self.JokesGroupBox, 2, 0)
        main_layout.addWidget(self.StatisticsGroupBox, 3, 0)
        self.setLayout(main_layout)

        self.setWindowTitle("Dziennik")
        self.changeStyle('Fusion')

    def changeStyle(self, style_name):
        QApplication.setStyle(QStyleFactory.create(style_name))
        self.changePalette()

    def changePalette(self):
        if self.useStylePaletteCheckBox.isChecked():
            QApplication.setPalette(QApplication.style().standardPalette())
        else:
            QApplication.setPalette(self.originalPalette)

    def tell_joke(self):
        self.textbox_joke.setText(str(say_a_joke()))

    def add_sugar(self):
        dodaj_wpis(int(self.textbox_measurment.text()))
        os.system("python google_synch.py w " + str(self.textbox_measurment.text()))
        self.textbox_measurment.clear()

    def synch_up(self):
        os.system("python google_synch.py r")

    def search(self):
        print((measurments_from_chosen_day_and_month_and_year(
            self.textbox_year.text() + "-" + self.textbox_month.text() + "-" + self.textbox_day.text())))
        self.textbox_found_measurments.setText(measurments_from_chosen_day_and_month_and_year(
            self.textbox_year.text() + "-" + self.textbox_month.text() + "-" + self.textbox_day.text()))

    def draw_graph(self):
        graph_of_last_30_measurments()

    def createAddMeasurmentGroupBox(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Podaj Cukier"))
        layout.addWidget(self.textbox_measurment)
        default_push_button = QPushButton("Zatwierdź")
        default_push_button.clicked.connect(self.add_sugar)
        default_push_button.setDefault(True)
        layout.addWidget(default_push_button)

        synch_button = QPushButton("Synchronizuj")
        synch_button.clicked.connect(self.synch_up)
        layout.addWidget(synch_button)
        layout.addStretch(1)
        self.AddMeasurmentGroupBox.setLayout(layout)

    def createSearchingGroupBox(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Rok"))
        layout.addWidget(self.textbox_year)
        layout.addWidget(QLabel("Miesiąc"))
        layout.addWidget(self.textbox_month)
        layout.addWidget(QLabel("Dzień"))
        layout.addWidget(self.textbox_day)
        search_button = QPushButton("Wyszukiwanie")
        search_button.clicked.connect(self.search)
        layout.addWidget(search_button)
        layout.addWidget(QLabel("Wyniki wyszukiwania"))
        layout.addWidget(self.textbox_found_measurments)

        layout.addStretch(1)
        self.SearchingGroupBox.setLayout(layout)

    def createJokesGroupBox(self):
        layout = QVBoxLayout()

        joke_button = QPushButton("Powiedz kawał")
        joke_button.clicked.connect(self.tell_joke)
        layout.addWidget(joke_button)
        layout.addWidget(self.textbox_joke)

        layout.addStretch(1)
        self.JokesGroupBox.setLayout(layout)

    def createStatisticsGroupBox(self):
        layout = QVBoxLayout()

        stats_button = QPushButton("Narysuj wykres ostatnich 30 pomiarow")
        stats_button.clicked.connect(self.draw_graph)
        layout.addWidget(stats_button)

        layout.addStretch(1)
        self.StatisticsGroupBox.setLayout(layout)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.resize(1000, 500)
    gallery.show()
    sys.exit(app.exec_())
