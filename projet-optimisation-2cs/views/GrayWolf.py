from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from algorithms.GrayWolf import GWO, import_csv

from widgets.calculte_button import calculte_button
from widgets.upload_button import upload_button
from widgets.table_view import table_view


def run(self, weight, taill, iterations):
    pass
    array = import_csv(self.fname[:len(self.fname)-4])
    tps, Benefice, capacite_prise, resultat = GWO(
        weight, array, taill, iterations)

    data = {
        'Best Value': [str(Benefice)],
        'Current weight': [str(capacite_prise)],
        'Objects': [],
        'Duration': [str(tps)]
    }

    while(len(resultat) != 0):
        s = resultat.pop(len(resultat)-1)
        data['Objects'].append(
            "Objet: " + str(s.item) + " => Exemplaires: " + str(s.nbr_item))

    showResult(self, data)


def grayWolfTab(self):

    self.gray_wolf_layout = QVBoxLayout()
    welcome = QLabel('Gray Wolf Optimizer')
    welcome.setStyleSheet(
        "QLabel"
        "{"
        "font-size: 32px;"
        "font-weight: bold;"
        "color: #000;"
        "}"
    )

    container = QHBoxLayout()
    container.setContentsMargins(0, 0, 0, 0)

    maxWeight = QLineEdit(self)
    maxWeight.setPlaceholderText('Max Weight')
    maxWeight.setFixedHeight(80)

    maxWeight.setStyleSheet(
        "QLineEdit"
        "{"
        "border: 1px solid #000;"
        "border-radius: 12px;"
        "font-weight: bold;"
        "padding: 5px;"
        "}"
    )

    upload_csv = upload_button('Upload csv file', self)
    upload_csv.setFixedWidth(200)
    upload_csv.setFixedHeight(80)

    upload_csv.clicked.connect(lambda: uploadFile(self))

    size = QLineEdit(self)
    size.setPlaceholderText('Population size')
    size.setFixedHeight(50)
    size.setFixedWidth(400)

    size.setStyleSheet(
        "QLineEdit"
        "{"
        "border: 1px solid #000;"
        "border-radius: 12px;"
        "font-weight: bold;"
        "padding: 5px;"
        "margin-top: 10px;"
        "}"
    )

    iterations = QLineEdit(self)
    iterations.setPlaceholderText('Number of iterations')
    iterations.setFixedHeight(50)
    iterations.setFixedWidth(400)

    iterations.setStyleSheet(
        "QLineEdit"
        "{"
        "border: 1px solid #000;"
        "border-radius: 12px;"
        "font-weight: bold;"
        "padding: 5px;"
        "margin-top: 10px;"
        "}"
    )

    container.addWidget(maxWeight)
    container.addWidget(upload_csv)

    upload = QWidget()
    upload.setLayout(container)

    upload.setStyleSheet(
        "QWidget"
        "{"
        "margin-top: 40px;"
        "}"
    )

    self.gray_wolf_layout.addWidget(welcome)
    self.gray_wolf_layout.addWidget(upload)

    calcualte = calculte_button('Calculate', self)

    calcualte.clicked.connect(lambda: run(
        self, int(maxWeight.text()), int(size.text()), int(iterations.text())))

    calcualte.setFixedWidth(400)
    calcualte.setFixedHeight(80)

    self.gray_wolf_layout.addWidget(size)
    self.gray_wolf_layout.addWidget(iterations)
    self.gray_wolf_layout.addWidget(calcualte)

    self.gray_wolf_layout.addStretch(0)
    main = QWidget()
    main.setLayout(self.gray_wolf_layout)
    return main


def uploadFile(self):
    fname, _ = QFileDialog.getOpenFileName(
        self, "Import CSV", "", "CSV data files (*.csv)")
    self.fname = fname

def showResult(self, data):
    table = table_view(data, len(data['Objects']), 4)
    table.verticalHeader().setVisible(False)
    table.setStyleSheet(
        "QTableView"
        "{"
        "margin-right: 10px;"
        "margin-top: 40px;"
        "}"
    )
    header = table.horizontalHeader()
    header.setMaximumWidth(760)
    header.setSectionResizeMode(0, QHeaderView.Stretch)
    header.setSectionResizeMode(1, QHeaderView.Stretch)
    header.setSectionResizeMode(2, QHeaderView.Stretch)
    header.setSectionResizeMode(3, QHeaderView.Stretch)

    table.setFixedWidth(1200)

    self.gray_wolf_layout.addWidget(table)
    self.gray_wolf_layout.addStretch(5)

