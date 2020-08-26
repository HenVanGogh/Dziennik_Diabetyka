#!/usr/bin/python
# -*- coding: utf-8 -*-

from include.losowanie_zartu_z_pliku import say_a_joke
from include.dane import dodaj_wpis
from include.wykresy import graph_of_last_30_measurments, measurments_from_chosen_day_and_month_and_year,\
    measurments_from_chosen_month_and_year

# jezeli dziala usunac
# import datetime
# from typing import List, Dict
# import random as rm
# import math
# from matplotlib import pyplot as plt
# from matplotlib import style
# from typing import List

from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)


class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.originalPalette = QApplication.palette()

        styleComboBox = QComboBox()
        styleComboBox.addItems(QStyleFactory.keys())

        styleLabel = QLabel("&Style:")
        styleLabel.setBuddy(styleComboBox)

        self.useStylePaletteCheckBox = QCheckBox("&Use style's standard palette")
        self.useStylePaletteCheckBox.setChecked(True)

        disableWidgetsCheckBox = QCheckBox("&Disable widgets")

        #self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        self.createBottomLeftTabWidget()
        #self.createBottomRightGroupBox()


        self.useStylePaletteCheckBox.toggled.connect(self.changePalette)
        disableWidgetsCheckBox.toggled.connect(self.topRightGroupBox.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.bottomLeftTabWidget.setDisabled)

        topLayout = QHBoxLayout()
        topLayout.addWidget(styleLabel)
        topLayout.addWidget(styleComboBox)
        topLayout.addStretch(3)
        topLayout.addWidget(self.useStylePaletteCheckBox)
        topLayout.addWidget(disableWidgetsCheckBox)

        mainLayout = QGridLayout()
        #mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        #mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 0, 1 , 0.2, 700)
        mainLayout.addWidget(self.bottomLeftTabWidget, 0, 0)
        #mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        #mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        # mainLayout.setRowStretch(4, 4)
        # mainLayout.setRowStretch(8, 8)
        # mainLayout.setColumnStretch(0, 8)
        # mainLayout.setColumnStretch(8, 8)
        self.setLayout(mainLayout)

        self.setWindowTitle("Dziennik")
        self.changeStyle('Fusion')

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        self.changePalette()

    def changePalette(self):
        if (self.useStylePaletteCheckBox.isChecked()):
            QApplication.setPalette(QApplication.style().standardPalette())
        else:
            QApplication.setPalette(self.originalPalette)



    def tell_joke(self):
        self.textbox4.setText(str(say_a_joke()))

    def add_suggar(self):
        dodaj_wpis(int(self.textbox.text()))
        self.textbox.clear()

    def search(self):
        print( self.textbox3.text() + "-" + self.textbox2.text() + "-" + self.textbox1.text())
        print((measurments_from_chosen_day_and_month_and_year(
            self.textbox1.text() + "-" + self.textbox2.text() + "-" + self.textbox3.text())))
        self.textbox_cukier.setText(measurments_from_chosen_day_and_month_and_year(
            self.textbox1.text() + "-" + self.textbox2.text() + "-" + self.textbox3.text()))

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("Dodaj nowy pomiar")
        defaultPushButton = QPushButton("Zatwierdz")
        joke_button = QPushButton("Powiedz kawał")
        joke_button.clicked.connect(self.tell_joke)
        defaultPushButton.clicked.connect(self.add_suggar)
        defaultPushButton.setDefault(True)
        label = QLabel("Podaj Cukier")
        label_cukier = QLabel("twoj cukier ")
        self.textbox = QLineEdit(self)

        layout = QVBoxLayout()
        layout.addWidget(defaultPushButton)
        button_1 = QPushButton("Wyszukiwanie")
        button_1.clicked.connect(self.search)

        self.textbox_cukier = QLineEdit(self)

        #textbox = QLineEdit(self)
        layout.addWidget(label_cukier)
        layout.addWidget(self.textbox_cukier)
        layout.addWidget(label)


        layout.addWidget(self.textbox)
        layout.addWidget(button_1)
        label = QLabel("Rok")
        layout.addWidget(label)
        self.textbox1 = QLineEdit(self)
        layout.addWidget(self.textbox1)
        label = QLabel("Miesiąc")
        layout.addWidget(label)
        self.textbox2 = QLineEdit(self)
        layout.addWidget(self.textbox2)
        label = QLabel("Dzien")
        layout.addWidget(label)
        self.textbox3 = QLineEdit(self)
        self.textbox3.setBaseSize(10 , 10)
        layout.addWidget(self.textbox3)

        self.textbox4 = QLineEdit(self)
        layout.addWidget(joke_button)
        layout.addWidget(self.textbox4)



        layout.addStretch(1)
        self.topRightGroupBox.setLayout(layout)

    def createBottomLeftTabWidget(self):
        self.bottomLeftTabWidget = QTabWidget()
        self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Ignored)

        tab1 = QWidget()
        tableWidget = QTableWidget(20, 10)   #rowmiar wyswietlane tabeli

        tab1hbox = QHBoxLayout()
        tab1hbox.setContentsMargins(5, 5, 5, 5)
        tab1hbox.addWidget(tableWidget)
        tab1.setLayout(tab1hbox)

        tab2 = QWidget()


        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)

        tab2.setLayout(tab2hbox)
        tab2.setMinimumWidth(800)
        self.bottomLeftTabWidget.addTab(tab1, "&Table")
        self.bottomLeftTabWidget.addTab(tab2, "Text &Edit")

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.resize(1000, 500)
    gallery.show()
    sys.exit(app.exec_())

