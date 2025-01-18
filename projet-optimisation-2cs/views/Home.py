from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def homeTab(self):
    main_layout = QVBoxLayout()
    welcome = QLabel('Welcome To The Knapsack-Problem Solver')
    welcome.setStyleSheet(
        "QLabel"
        "{"
        "font-size: 32px;"
        "font-weight: bold;"
        "color: #000;"
        "}"
    )

    by = QLabel('Resolving the Knapsack Problem, by:')
    by.setStyleSheet(
        "QLabel"
        "{"
        "font-size: 18px;"
        "margin-top: 20px;"
        "color: #000;"
        "}"
    )

    memebers = QLabel('''
            <ul>
                <li>Ould mohamed Celina</li>
                <li style="margin-top:8px;">Deghboudj Abderrahmen</li>              
                <li style="margin-top:8px;">Belabied Redouane </li>              
                <li style="margin-top:8px;">Kadouma Abdelhak</li>              
                <li style="margin-top:8px;">Haddad Zineddine</li>              

            </ul>
        ''')
    memebers.setStyleSheet(
        "QLabel"
        "{"
        "font-size: 16px;"
        "margin-top: 12px;"
        "color: #000;"
        "}"
    )

    label = QLabel(self)
    pixmap = QPixmap('./images/home.png')
    pixmap = pixmap.scaled(300, 300)

    label.setPixmap(pixmap)
    label.setAlignment(Qt.AlignCenter)
    label.setStyleSheet(
        "QLabel"
        "{"
        "margin-top: 50px;"
        "}"
    )

    main_layout.addWidget(welcome)
    main_layout.addWidget(by)
    main_layout.addWidget(memebers)
    main_layout.addWidget(label)

    main_layout.addStretch(5)
    main = QWidget()

    main.setLayout(main_layout)
    return main
