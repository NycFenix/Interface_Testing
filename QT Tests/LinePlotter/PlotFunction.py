
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
    QWidget)


import matplotlib.pyplot as plt
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(320, 470, 187, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)


        self.coefA = QLineEdit(self.horizontalLayoutWidget)
        self.coefA.setObjectName(u"Coefficient A")
        self.horizontalLayout.addWidget(self.coefA)

        self.coefB = QLineEdit(self.horizontalLayoutWidget)
        self.coefB.setObjectName(u"Coefficient B")
        self.horizontalLayout.addWidget(self.coefB)


        # labels
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 751, 361))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(330, 410, 81, 81))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(430, 410, 81, 81))
        self.label4 = QLabel(self.centralwidget)
        self.label4.setObjectName("name")
        self.label4.setGeometry(QRect(370, 370, 200, 81))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 807, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Graph", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Coefficient A", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Coeficient B", None))
        self.label4.setText(QCoreApplication.translate("MainWindow", u"Function: y = Ax + B", None))
    # retranslateUi

    def plotFuntion(coefA, coefB):
        A, B = float(coefA.text()), float(coefB.text())
        x = np.linspace(-50, 50, 100)
        y = (A * x) + B 
        fig = plt.figure(figsize = (20, 10))
        plt.plot(x, y)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    PlotUI = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(PlotUI)
    PlotUI.show()
    sys.exit(app.exec())



 
