# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CalculatorUI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MyCalculator(object):
    def setupUi(self, MyCalculator):
        if not MyCalculator.objectName():
            MyCalculator.setObjectName(u"MyCalculator")
        MyCalculator.resize(800, 600)
        self.centralwidget = QWidget(MyCalculator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(170, 370, 241, 81))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Button1 = QPushButton(self.horizontalLayoutWidget)
        self.Button1.setObjectName(u"Button1")
        self.Button1.setMaximumSize(QSize(171, 101))
        font = QFont()
        font.setFamilies([u"Book Antiqua"])
        font.setPointSize(12)
        self.Button1.setFont(font)

        self.horizontalLayout.addWidget(self.Button1)

        self.Button2 = QPushButton(self.horizontalLayoutWidget)
        self.Button2.setObjectName(u"Button2")
        self.Button2.setMaximumSize(QSize(171, 101))
        self.Button2.setFont(font)

        self.horizontalLayout.addWidget(self.Button2)

        self.Button3 = QPushButton(self.horizontalLayoutWidget)
        self.Button3.setObjectName(u"Button3")
        self.Button3.setMaximumSize(QSize(171, 101))
        self.Button3.setFont(font)

        self.horizontalLayout.addWidget(self.Button3)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(170, 190, 239, 80))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Button7 = QPushButton(self.horizontalLayoutWidget_2)
        self.Button7.setObjectName(u"Button7")
        self.Button7.setMaximumSize(QSize(171, 101))
        self.Button7.setFont(font)

        self.horizontalLayout_2.addWidget(self.Button7)

        self.Button8 = QPushButton(self.horizontalLayoutWidget_2)
        self.Button8.setObjectName(u"Button8")
        self.Button8.setMaximumSize(QSize(171, 101))
        self.Button8.setFont(font)

        self.horizontalLayout_2.addWidget(self.Button8, 0, Qt.AlignHCenter)

        self.Button9 = QPushButton(self.horizontalLayoutWidget_2)
        self.Button9.setObjectName(u"Button9")
        self.Button9.setMaximumSize(QSize(171, 101))
        self.Button9.setFont(font)

        self.horizontalLayout_2.addWidget(self.Button9)

        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(170, 280, 239, 80))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Button4 = QPushButton(self.horizontalLayoutWidget_3)
        self.Button4.setObjectName(u"Button4")
        self.Button4.setMaximumSize(QSize(171, 101))
        self.Button4.setFont(font)

        self.horizontalLayout_3.addWidget(self.Button4)

        self.Button5 = QPushButton(self.horizontalLayoutWidget_3)
        self.Button5.setObjectName(u"Button5")
        self.Button5.setMaximumSize(QSize(171, 101))
        self.Button5.setFont(font)

        self.horizontalLayout_3.addWidget(self.Button5, 0, Qt.AlignHCenter)

        self.Button6 = QPushButton(self.horizontalLayoutWidget_3)
        self.Button6.setObjectName(u"Button6")
        self.Button6.setMaximumSize(QSize(171, 101))
        self.Button6.setFont(font)

        self.horizontalLayout_3.addWidget(self.Button6)

        self.Button10 = QPushButton(self.centralwidget)
        self.Button10.setObjectName(u"Button10")
        self.Button10.setGeometry(QRect(250, 460, 75, 79))
        self.Button10.setMaximumSize(QSize(171, 101))
        self.Button10.setFont(font)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(460, 190, 211, 161))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.PlusButton = QPushButton(self.gridLayoutWidget)
        self.PlusButton.setObjectName(u"PlusButton")
        self.PlusButton.setMaximumSize(QSize(171, 101))
        self.PlusButton.setFont(font)

        self.gridLayout_2.addWidget(self.PlusButton, 0, 0, 1, 1)

        self.MinusButton = QPushButton(self.gridLayoutWidget)
        self.MinusButton.setObjectName(u"MinusButton")
        self.MinusButton.setMaximumSize(QSize(171, 101))
        self.MinusButton.setFont(font)

        self.gridLayout_2.addWidget(self.MinusButton, 0, 1, 1, 1)

        self.TimesButton = QPushButton(self.gridLayoutWidget)
        self.TimesButton.setObjectName(u"TimesButton")
        self.TimesButton.setMaximumSize(QSize(171, 101))
        self.TimesButton.setFont(font)

        self.gridLayout_2.addWidget(self.TimesButton, 1, 0, 1, 1)

        self.DivisionButton = QPushButton(self.gridLayoutWidget)
        self.DivisionButton.setObjectName(u"DivisionButton")
        self.DivisionButton.setMaximumSize(QSize(171, 101))
        self.DivisionButton.setFont(font)

        self.gridLayout_2.addWidget(self.DivisionButton, 1, 1, 1, 1)

        self.EqualButton = QPushButton(self.centralwidget)
        self.EqualButton.setObjectName(u"EqualButton")
        self.EqualButton.setGeometry(QRect(510, 410, 102, 76))
        self.EqualButton.setMaximumSize(QSize(171, 101))
        self.EqualButton.setFont(font)
        self.ClearButton = QPushButton(self.centralwidget)
        self.ClearButton.setObjectName(u"ClearButton")
        self.ClearButton.setGeometry(QRect(24, 80, 101, 51))
        MyCalculator.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MyCalculator)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 800, 22))
        MyCalculator.setMenuBar(self.menuBar)
        self.statusbar = QStatusBar(MyCalculator)
        self.statusbar.setObjectName(u"statusbar")
        MyCalculator.setStatusBar(self.statusbar)

        self.retranslateUi(MyCalculator)

        QMetaObject.connectSlotsByName(MyCalculator)
    # setupUi

    def retranslateUi(self, MyCalculator):
        MyCalculator.setWindowTitle(QCoreApplication.translate("MyCalculator", u"MainWindow", None))
        self.Button1.setText(QCoreApplication.translate("MyCalculator", u"1", None))
        self.Button2.setText(QCoreApplication.translate("MyCalculator", u"2", None))
        self.Button3.setText(QCoreApplication.translate("MyCalculator", u"3", None))
        self.Button7.setText(QCoreApplication.translate("MyCalculator", u"7", None))
        self.Button8.setText(QCoreApplication.translate("MyCalculator", u"8", None))
        self.Button9.setText(QCoreApplication.translate("MyCalculator", u"9", None))
        self.Button4.setText(QCoreApplication.translate("MyCalculator", u"4", None))
        self.Button5.setText(QCoreApplication.translate("MyCalculator", u"5", None))
        self.Button6.setText(QCoreApplication.translate("MyCalculator", u"6", None))
        self.Button10.setText(QCoreApplication.translate("MyCalculator", u"0", None))
        self.PlusButton.setText(QCoreApplication.translate("MyCalculator", u"+", None))
        self.MinusButton.setText(QCoreApplication.translate("MyCalculator", u"-", None))
        self.TimesButton.setText(QCoreApplication.translate("MyCalculator", u"*", None))
        self.DivisionButton.setText(QCoreApplication.translate("MyCalculator", u"\u00f7", None))
        self.EqualButton.setText(QCoreApplication.translate("MyCalculator", u"=", None))
        self.ClearButton.setText(QCoreApplication.translate("MyCalculator", u"CLEAR", None))
    # retranslateUi

