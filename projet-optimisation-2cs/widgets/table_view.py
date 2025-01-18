from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class table_view(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.setData()
        self.setStyleSheet(
            "QTableWidget"
            "{"

            "font-weight: bold;"
            "margin-top: 40px;"
            "background-color: #40D89E;"
            "}"
            "QTableWidget::item"
            "{"
            "border: 0px;"
            "padding: 5px;"
            "}"

        )

    def setData(self):
        horHeaders = []
        for n, key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)
