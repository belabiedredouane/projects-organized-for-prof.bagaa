from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from widgets.menu_button import menu_button

from views.BranchAndBound import branchTab
from views.GreedyWeight import greedyWeightTab
from views.GreedyProfit import greedyProfitTab
from views.GrayWolf import grayWolfTab
from views.Genetic import geneticTab
from views.GreedyTotal import greedyTotalTab
from views.GreedyEfficiency import greedyEfficiencyTab
from views.ExtendedGreedyEfficiency import extendedGreedyEfficiencyTab
from views.RechercheTabou import rechercheTabouTab
from views.Home import homeTab


class HomeScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title of main window
        self.setWindowTitle('Knapsack algorithms')

        # set the size of window
        # self.Width = 1024
        # self.height = int(0.618 * self.Width)
        # self.setFixedSize(self.Width, self.height)

        # add all widgets
        self.home = menu_button('Home', self)
        self.branch = menu_button('Branch and bound', self)
        self.greedy_weight = menu_button('Greedy Weight', self)
        self.greedy_profit = menu_button('Greedy Profit', self)
        self.gray_wolf = menu_button('Gray Wolf Optimizer', self)
        self.genetic = menu_button('Genetic Algorithm', self)
        self.greedy_total = menu_button('Total value heuristic', self)
        self.greedy_efficiency = menu_button('Greedy Efficiency', self)
        self.extended_greedy_efficiency = menu_button(
            'Extended Greedy Efficiency', self)
        self.recherche_tabou = menu_button('Recherche Tabou', self)

        self.home.clicked.connect(self.showHome)
        self.branch.clicked.connect(self.showBranch)
        self.greedy_weight.clicked.connect(self.showGreedyWeight)
        self.greedy_profit.clicked.connect(self.showGreedyProfit)
        self.gray_wolf.clicked.connect(self.showGrayWolf)
        self.genetic.clicked.connect(self.showGenetic)
        self.greedy_total.clicked.connect(self.showGreedyTotal)
        self.greedy_efficiency.clicked.connect(self.showGreedyEfficiency)
        self.extended_greedy_efficiency.clicked.connect(
            self.showExtendedGreedyEfficiency)
        self.recherche_tabou.clicked.connect(self.showRechercheTabou)

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Knapsack algorithms')
        self.setWindowIcon(QIcon('./images/knapsack.png'))

        menu_layout = QVBoxLayout()

        menu_layout.addWidget(self.home)
        menu_layout.addWidget(self.branch)
        menu_layout.addWidget(self.greedy_weight)
        menu_layout.addWidget(self.greedy_profit)
        menu_layout.addWidget(self.gray_wolf)
        menu_layout.addWidget(self.genetic)
        menu_layout.addWidget(self.greedy_total)
        menu_layout.addWidget(self.greedy_efficiency)
        menu_layout.addWidget(self.extended_greedy_efficiency)
        menu_layout.addWidget(self.recherche_tabou)

        menu_layout.addStretch(0)
        menu_layout.setSpacing(0)
        menu_widget = QWidget()
        menu_widget.setStyleSheet(
            "QWidget"
            "{"
            "background-color : #40D89E;"
            "border-radius: 12px;"
            "}"
        )
        menu_widget.setLayout(menu_layout)

        self.tab_widget = QTabWidget()
        self.tab_widget.setObjectName('tab_widget')

        self.tab_widget.addTab(homeTab(self), '')
        self.tab_widget.addTab(branchTab(self), '')
        self.tab_widget.addTab(greedyWeightTab(self), '')
        self.tab_widget.addTab(greedyProfitTab(self), '')
        self.tab_widget.addTab(grayWolfTab(self), '')
        self.tab_widget.addTab(geneticTab(self), '')
        self.tab_widget.addTab(greedyTotalTab(self), '')
        self.tab_widget.addTab(greedyEfficiencyTab(self), '')
        self.tab_widget.addTab(extendedGreedyEfficiencyTab(self), '')
        self.tab_widget.addTab(rechercheTabouTab(self), '')

        self.tab_widget.setCurrentIndex(0)
        self.tab_widget.setStyleSheet(
            "QTabBar::tab"
            "{"
            "width: 0px;"
            "height: 0px;"
            "}"
        )

        main_layout = QHBoxLayout()

        main_layout.addWidget(menu_widget)
        main_layout.addWidget(self.tab_widget)

        main_widget = QWidget()
        main_widget.setStyleSheet("QWidget"
                                  "{"

                                  "background-color : #9ce0c6;"
                                  "border: none;"
                                  "margin: 0px;"
                                  "padding: 0px;"
                                  "color: #000;"

                                  "}"
                                  )

        main_widget.setObjectName('main_widget')
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    # buttons
    def showHome(self):
        self.tab_widget.setCurrentIndex(0)

    def showBranch(self):
        self.tab_widget.setCurrentIndex(1)

    def showGreedyWeight(self):
        self.tab_widget.setCurrentIndex(2)

    def showGreedyProfit(self):
        self.tab_widget.setCurrentIndex(3)

    def showGrayWolf(self):
        self.tab_widget.setCurrentIndex(4)

    def showGenetic(self):
        self.tab_widget.setCurrentIndex(5)

    def showGreedyTotal(self):
        self.tab_widget.setCurrentIndex(6)

    def showGreedyEfficiency(self):
        self.tab_widget.setCurrentIndex(7)

    def showExtendedGreedyEfficiency(self):
        self.tab_widget.setCurrentIndex(8)

    def showRechercheTabou(self):
        self.tab_widget.setCurrentIndex(9)
