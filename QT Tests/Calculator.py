
import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLCDNumber, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_CalculatorMainWindow(object):
    def setupUi(self, CalculatorMainWindow):
        if not CalculatorMainWindow.objectName():
            CalculatorMainWindow.setObjectName(u"CalculatorMainWindow")
        CalculatorMainWindow.resize(808, 614)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CalculatorMainWindow.sizePolicy().hasHeightForWidth())
        CalculatorMainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(CalculatorMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(240, 390, 371, 121))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.SumButton = QPushButton(self.horizontalLayoutWidget)
        self.SumButton.setObjectName(u"SumButton")
        sizePolicy.setHeightForWidth(self.SumButton.sizePolicy().hasHeightForWidth())
        self.SumButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.SumButton)

        self.MinusButton = QPushButton(self.horizontalLayoutWidget)
        self.MinusButton.setObjectName(u"MinusButton")
        sizePolicy.setHeightForWidth(self.MinusButton.sizePolicy().hasHeightForWidth())
        self.MinusButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.MinusButton)

        self.TimesButton = QPushButton(self.horizontalLayoutWidget)
        self.TimesButton.setObjectName(u"TimesButton")
        sizePolicy.setHeightForWidth(self.TimesButton.sizePolicy().hasHeightForWidth())
        self.TimesButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.TimesButton)

        self.DivisionButton = QPushButton(self.horizontalLayoutWidget)
        self.DivisionButton.setObjectName(u"DivisionButton")
        sizePolicy.setHeightForWidth(self.DivisionButton.sizePolicy().hasHeightForWidth())
        self.DivisionButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.DivisionButton)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 50, 433, 78))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(350, 170, 160, 80))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.LCDShow = QLCDNumber(self.verticalLayoutWidget)
        self.LCDShow.setObjectName(u"LCDShow")

        #how many digits the calculator supports in theory
        self.LCDShow.setDigitCount(30)
        # The mode of the calculator, now it is Decimal values
        self.LCDShow.setDecMode()
        self.verticalLayout_2.addWidget(self.LCDShow)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(40, 220, 160, 80))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.NumberField = QLineEdit(self.verticalLayoutWidget_2)
        self.NumberField.setObjectName(u"NumberField")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.NumberField.sizePolicy().hasHeightForWidth())
        self.NumberField.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.NumberField)

        self.EqualButton = QPushButton(self.centralwidget)
        self.EqualButton.setObjectName(u"EqualButton")
        self.EqualButton.setGeometry(QRect(350, 290, 158, 61))
        sizePolicy.setHeightForWidth(self.EqualButton.sizePolicy().hasHeightForWidth())
        self.EqualButton.setSizePolicy(sizePolicy)
        self.ClearButton = QPushButton(self.centralwidget)
        self.ClearButton.setObjectName(u"ClearButton")
        self.ClearButton.setGeometry(QRect(580, 200, 211, 71))
        sizePolicy.setHeightForWidth(self.ClearButton.sizePolicy().hasHeightForWidth())
        self.ClearButton.setSizePolicy(sizePolicy)
        CalculatorMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CalculatorMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 808, 22))
        self.menuCalculator = QMenu(self.menubar)
        self.menuCalculator.setObjectName(u"menuCalculator")
        CalculatorMainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CalculatorMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        CalculatorMainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuCalculator.menuAction())

        self.retranslateUi(CalculatorMainWindow)

        QMetaObject.connectSlotsByName(CalculatorMainWindow)

        self.EqualButton.clicked.connect(self.loadLCD)
        self.ClearButton.clicked.connect(self.clear()) #assign clear function to clear button
        self.numberInMemory = 0 #Number stored in the memory of the calculator

    # setupUi

    def retranslateUi(self, CalculatorMainWindow):
        CalculatorMainWindow.setWindowTitle(QCoreApplication.translate("CalculatorMainWindow", u"MainWindow", None))
        self.SumButton.setText(QCoreApplication.translate("CalculatorMainWindow", u"+", None))
        self.MinusButton.setText(QCoreApplication.translate("CalculatorMainWindow", u"-", None))
        self.TimesButton.setText(QCoreApplication.translate("CalculatorMainWindow", u"x", None))
        self.DivisionButton.setText(QCoreApplication.translate("CalculatorMainWindow", u"/", None))
        self.label.setText(QCoreApplication.translate("CalculatorMainWindow", u"Enter the values into the fiel to the left, then select the operation using the buttons", None))
        self.NumberField.setText(QCoreApplication.translate("CalculatorMainWindow", u"Enter number here", None))
        self.EqualButton.setText(QCoreApplication.translate("CalculatorMainWindow", u"=", None))
        self.ClearButton.setText(QCoreApplication.translate("CalculatorMainWindow", u"CLEAR", None))
        self.menuCalculator.setTitle(QCoreApplication.translate("CalculatorMainWindow", u"Calculator", None))
    # retranslateUi
    

    # Loads result in LCD shower and cleans NumberField
    def loadLCD(self):
        self.LCDShow.display(int(self.NumberField.text()))
        self.numberInMemory = self.NumberField.text()
        self.NumberField.setText("")        

    def clear(self):
        self.numberInMemory = 0
        self.NumberField.setText("")



# Refactor: edit code to be used with one button per number like a normal calculator:
# - Learn how to be better at Designer
# - Button numbers one by one
# - Have a big expression string that just gets evaluated at the end
# - What to do with expression visor??




    # def OperationManager(self, operator: QPushButton):
    #     if operator == self.SumButton:
    #         if self.NumberField.text() == 0:
    #             self.loadLCD(self.NumberField)
                
    #         self.numberInMemory += eval(self.NumberField)

# MAIN
if __name__ == "__main__":
    appCalculadora = QApplication() #Initializes 
    CalculadoraMainWindow = QMainWindow()
    Interface = Ui_CalculatorMainWindow()
    Interface.setupUi(CalculadoraMainWindow)
    # CalculadoraMainWindow.setWindowTitle("Calculator") 
    CalculadoraMainWindow.show()
    sys.exit(appCalculadora.exec_())


