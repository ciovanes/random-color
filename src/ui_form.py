# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_RandomColor(object):
    def setupUi(self, RandomColor):
        if not RandomColor.objectName():
            RandomColor.setObjectName(u"RandomColor")
        RandomColor.resize(440, 280)
        RandomColor.setMinimumSize(QSize(440, 280))
        RandomColor.setMaximumSize(QSize(440, 280))
        RandomColor.setStyleSheet(u"QWidget {\n"
"background-color:#333333\n"
"\n"
"}\n"
"\n"
"QFrame#colorViewer {\n"
"border-radius:5px;\n"
"border: 1px solid #454545;\n"
"}\n"
"\n"
"/* Generate button*/\n"
"QPushButton#pushButton {\n"
"background-color: #444444;\n"
"color:white;\n"
"border-radius:5px;\n"
"border:.5px solid #454545;\n"
"	\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"background-color:#515151;\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed {\n"
"background-color: #717171;\n"
"}\n"
"\n"
"/* Show fields */\n"
"QFrame#showRGB {\n"
"background-color: #454545;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QFrame#showRGB:hover {\n"
"border-bottom: 1px solid white;\n"
"}\n"
"\n"
"QFrame#showHEX {\n"
"background-color: #454545;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QFrame#showHEX:hover {\n"
"border-bottom: 1px solid white;\n"
"}\n"
"\n"
" QPushButton#copyRGB, QPushButton#copyHEX {\n"
"background-color:#454545;\n"
"background-position: center;\n"
"background-repeat:no-repeat;\n"
"border-radius:5px\n"
"}\n"
"QPushButton#copyRGB:hover , QPus"
                        "hButton#copyHEX:hover {\n"
"background-color:#515151;\n"
"}\n"
"\n"
"QPushButton#copyRGB:pressed , QPushButton#copyHEX:pressed{\n"
"background-color: #717171;\n"
"}\n"
"")
        self.pushButton = QPushButton(RandomColor)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 220, 121, 41))
        font = QFont()
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"")
        self.colorViewer = QFrame(RandomColor)
        self.colorViewer.setObjectName(u"colorViewer")
        self.colorViewer.setGeometry(QRect(20, 20, 401, 50))
        self.colorViewer.setFrameShape(QFrame.StyledPanel)
        self.colorViewer.setFrameShadow(QFrame.Raised)
        self.showRGB = QFrame(RandomColor)
        self.showRGB.setObjectName(u"showRGB")
        self.showRGB.setGeometry(QRect(20, 100, 401, 43))
        self.showRGB.setStyleSheet(u"")
        self.showRGB.setFrameShape(QFrame.StyledPanel)
        self.showRGB.setFrameShadow(QFrame.Raised)
        self.rgbLabel = QLabel(self.showRGB)
        self.rgbLabel.setObjectName(u"rgbLabel")
        self.rgbLabel.setGeometry(QRect(10, 10, 49, 21))
        self.rgbLabel.setFont(font)
        self.rgbLabel.setStyleSheet(u"background-color:454545;\n"
"color:#a9a9a9;")
        self.rgbColor = QLabel(self.showRGB)
        self.rgbColor.setObjectName(u"rgbColor")
        self.rgbColor.setGeometry(QRect(80, 10, 121, 21))
        self.rgbColor.setFont(font)
        self.rgbColor.setStyleSheet(u"background-color:454545;\n"
"color:#f5f5f5;")
        self.copyRGB = QPushButton(self.showRGB)
        self.copyRGB.setObjectName(u"copyRGB")
        self.copyRGB.setGeometry(QRect(360, 0, 41, 41))
        self.copyRGB.setStyleSheet(u"")
        self.rgbLabel_2 = QLabel(self.showRGB)
        self.rgbLabel_2.setObjectName(u"rgbLabel_2")
        self.rgbLabel_2.setGeometry(QRect(310, 10, 49, 21))
        self.rgbLabel_2.setFont(font)
        self.rgbLabel_2.setStyleSheet(u"background-color:454545;\n"
"color:#a9a9a9;")
        self.showHEX = QFrame(RandomColor)
        self.showHEX.setObjectName(u"showHEX")
        self.showHEX.setGeometry(QRect(20, 160, 401, 43))
        self.showHEX.setStyleSheet(u"")
        self.showHEX.setFrameShape(QFrame.StyledPanel)
        self.showHEX.setFrameShadow(QFrame.Raised)
        self.hexLabel = QLabel(self.showHEX)
        self.hexLabel.setObjectName(u"hexLabel")
        self.hexLabel.setGeometry(QRect(10, 10, 49, 21))
        self.hexLabel.setFont(font)
        self.hexLabel.setStyleSheet(u"background-color:454545;\n"
"color:#a9a9a9;")
        self.hexColor = QLabel(self.showHEX)
        self.hexColor.setObjectName(u"hexColor")
        self.hexColor.setGeometry(QRect(80, 10, 51, 21))
        self.hexColor.setFont(font)
        self.hexColor.setStyleSheet(u"background-color:454545;\n"
"color:#f5f5f5;")
        self.copyHEX = QPushButton(self.showHEX)
        self.copyHEX.setObjectName(u"copyHEX")
        self.copyHEX.setGeometry(QRect(360, 0, 41, 41))
        self.copyHEX.setStyleSheet(u"")
        self.hexLabel_2 = QLabel(self.showHEX)
        self.hexLabel_2.setObjectName(u"hexLabel_2")
        self.hexLabel_2.setGeometry(QRect(310, 10, 49, 21))
        self.hexLabel_2.setFont(font)
        self.hexLabel_2.setStyleSheet(u"background-color:454545;\n"
"color:#a9a9a9;")

        self.retranslateUi(RandomColor)

        QMetaObject.connectSlotsByName(RandomColor)
    # setupUi

    def retranslateUi(self, RandomColor):
        RandomColor.setWindowTitle(QCoreApplication.translate("RandomColor", u"RandomColor", None))
        self.pushButton.setText(QCoreApplication.translate("RandomColor", u"Generar", None))
        self.rgbLabel.setText(QCoreApplication.translate("RandomColor", u"RGB", None))
        self.rgbColor.setText("")
        self.copyRGB.setText("")
        self.rgbLabel_2.setText("")
        self.hexLabel.setText(QCoreApplication.translate("RandomColor", u"HEX", None))
        self.hexColor.setText("")
        self.copyHEX.setText("")
        self.hexLabel_2.setText("")
    # retranslateUi

