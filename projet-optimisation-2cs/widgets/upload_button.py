from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def upload_button(name, self):
    button = QPushButton(name, self)
    button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    button.setFixedWidth(335)
    button.setFixedHeight(74)
    button.setStyleSheet("QPushButton"
                         "{"
                         "border-radius: 12px;"
                         "font-size: 12px;"
                         "background-color : #39c28e;"
                         "font-weight: bold;"
                         "color: 'white';"
                         "}"
                         "QPushButton:hover"
                         "{"
                         "background-color : #2d9b71;"
                         "}"
                         )
    return button
