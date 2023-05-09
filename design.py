# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTextBrowser,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1275, 797)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.103448 rgba(234, 139, 255, 229), stop:1 rgba(67, 60, 255, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(880, 100, 341, 43))
        font = QFont()
        font.setFamilies([u".Apple SD Gothic NeoI"])
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 0));")
        self.label_3.setMargin(10)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(380, 10, 571, 71))
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 0));")
        self.label.setMargin(10)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(900, 140, 321, 261))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 0));\n"
"")
        self.button1 = QPushButton(self.frame)
        self.button1.setObjectName(u"button1")
        self.button1.setGeometry(QRect(90, 190, 131, 41))
        self.button1.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,70);\n"
"}")
        self.rez3 = QTextBrowser(self.frame)
        self.rez3.setObjectName(u"rez3")
        self.rez3.setGeometry(QRect(0, 140, 321, 41))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(1, 1, 321, 16))
        self.label_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 0));")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(1, 67, 321, 16))
        self.label_5.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 0));")
        self.label_5.setTextFormat(Qt.AutoText)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.comboBox3_speed = QComboBox(self.frame)
        self.comboBox3_speed.addItem("")
        self.comboBox3_speed.addItem("")
        self.comboBox3_speed.addItem("")
        self.comboBox3_speed.addItem("")
        self.comboBox3_speed.addItem("")
        self.comboBox3_speed.addItem("")
        self.comboBox3_speed.setObjectName(u"comboBox3_speed")
        self.comboBox3_speed.setGeometry(QRect(1, 91, 321, 32))
        self.comboBox3_speed.setStyleSheet(u"QComboBox{\n"
"color: black;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 30px;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 2px solid rgb(194, 194, 255);\n"
"}\n"
"QComboBox:focus {\n"
"    border: 2px solid rgb(140, 146, 255);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(243, 244, 255);\n"
"    selection-background-color: rgb(140, 146, 255);\n"
"}")
        self.comboBox3_speed.setMaxVisibleItems(8)
        self.comboBox1_itu_4 = QComboBox(self.frame)
        self.comboBox1_itu_4.addItem("")
        self.comboBox1_itu_4.addItem("")
        self.comboBox1_itu_4.addItem("")
        self.comboBox1_itu_4.addItem("")
        self.comboBox1_itu_4.addItem("")
        self.comboBox1_itu_4.addItem("")
        self.comboBox1_itu_4.addItem("")
        self.comboBox1_itu_4.addItem("")
        self.comboBox1_itu_4.addItem("")
        self.comboBox1_itu_4.addItem("")
        self.comboBox1_itu_4.addItem("")
        self.comboBox1_itu_4.addItem("")
        self.comboBox1_itu_4.addItem("")
        self.comboBox1_itu_4.addItem("")
        self.comboBox1_itu_4.addItem("")
        self.comboBox1_itu_4.addItem("")
        self.comboBox1_itu_4.addItem("")
        self.comboBox1_itu_4.setObjectName(u"comboBox1_itu_4")
        self.comboBox1_itu_4.setEnabled(True)
        self.comboBox1_itu_4.setGeometry(QRect(0, 30, 321, 32))
        self.comboBox1_itu_4.setStyleSheet(u"QComboBox{\n"
"color: black;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 30px;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 2px solid rgb(194, 194, 255);\n"
"}\n"
"QComboBox:focus {\n"
"    border: 2px solid rgb(140, 146, 255);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(200, 130, 255);    \n"
"    background-color: rgb(243, 244, 255);\n"
"    selection-background-color: rgb(200, 130, 255);\n"
"}")
        self.comboBox1_itu_4.setEditable(False)
        self.comboBox1_itu_4.setDuplicatesEnabled(False)
        self.label_5.raise_()
        self.label_2.raise_()
        self.comboBox3_speed.raise_()
        self.button1.raise_()
        self.rez3.raise_()
        self.comboBox1_itu_4.raise_()
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 100, 396, 43))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 0));")
        self.label_7.setMargin(10)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(70, 230, 321, 451))
        self.frame_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 0));\n"
"")
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(1, 1, 321, 16))
        self.label_8.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 0));")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(1, 67, 321, 16))
        self.label_9.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 0));")
        self.label_9.setTextFormat(Qt.AutoText)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.comboBox1_speed_2 = QComboBox(self.frame_2)
        self.comboBox1_speed_2.addItem("")
        self.comboBox1_speed_2.addItem("")
        self.comboBox1_speed_2.addItem("")
        self.comboBox1_speed_2.addItem("")
        self.comboBox1_speed_2.addItem("")
        self.comboBox1_speed_2.setObjectName(u"comboBox1_speed_2")
        self.comboBox1_speed_2.setGeometry(QRect(1, 91, 321, 32))
        self.comboBox1_speed_2.setStyleSheet(u"QComboBox{\n"
"color: black;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 30px;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 2px solid rgb(194, 194, 255);\n"
"}\n"
"QComboBox:focus {\n"
"    border: 2px solid rgb(140, 146, 255);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(243, 244, 255);\n"
"    selection-background-color: rgb(140, 146, 255);\n"
"}")
        self.comboBox1_speed_2.setMaxVisibleItems(8)
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(1, 133, 321, 16))
        self.label_10.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 0));")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.comboBox1_per = QComboBox(self.frame_2)
        self.comboBox1_per.addItem("")
        self.comboBox1_per.addItem("")
        self.comboBox1_per.addItem("")
        self.comboBox1_per.setObjectName(u"comboBox1_per")
        self.comboBox1_per.setGeometry(QRect(0, 160, 321, 32))
        self.comboBox1_per.setStyleSheet(u"QComboBox{\n"
"color: black;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 30px;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 2px solid rgb(194, 194, 255);\n"
"}\n"
"QComboBox:focus {\n"
"    border: 2px solid rgb(140, 146, 255);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(243, 244, 255);\n"
"    selection-background-color: rgb(140, 146, 255);\n"
"}")
        self.comboBox1_itu_2 = QComboBox(self.frame_2)
        self.comboBox1_itu_2.addItem("")
        self.comboBox1_itu_2.addItem("")
        self.comboBox1_itu_2.addItem("")
        self.comboBox1_itu_2.addItem("")
        self.comboBox1_itu_2.addItem("")
        self.comboBox1_itu_2.addItem("")
        self.comboBox1_itu_2.addItem("")
        self.comboBox1_itu_2.addItem("")
        self.comboBox1_itu_2.addItem("")
        self.comboBox1_itu_2.addItem("")
        self.comboBox1_itu_2.addItem("")
        self.comboBox1_itu_2.addItem("")
        self.comboBox1_itu_2.addItem("")
        self.comboBox1_itu_2.addItem("")
        self.comboBox1_itu_2.addItem("")
        self.comboBox1_itu_2.addItem("")
        self.comboBox1_itu_2.addItem("")
        self.comboBox1_itu_2.setObjectName(u"comboBox1_itu_2")
        self.comboBox1_itu_2.setEnabled(True)
        self.comboBox1_itu_2.setGeometry(QRect(0, 30, 321, 32))
        self.comboBox1_itu_2.setStyleSheet(u"QComboBox{\n"
"color: black;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 30px;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 2px solid rgb(194, 194, 255);\n"
"}\n"
"QComboBox:focus {\n"
"    border: 2px solid rgb(140, 146, 255);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(200, 130, 255);    \n"
"    background-color: rgb(243, 244, 255);\n"
"    selection-background-color: rgb(200, 130, 255);\n"
"}")
        self.comboBox1_itu_2.setEditable(False)
        self.comboBox1_itu_2.setDuplicatesEnabled(False)
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 200, 321, 16))
        self.label_11.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 0));")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.comboBox1_pr = QComboBox(self.frame_2)
        self.comboBox1_pr.addItem("")
        self.comboBox1_pr.addItem("")
        self.comboBox1_pr.setObjectName(u"comboBox1_pr")
        self.comboBox1_pr.setGeometry(QRect(0, 220, 321, 32))
        self.comboBox1_pr.setStyleSheet(u"QComboBox{\n"
"color: black;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 30px;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 2px solid rgb(194, 194, 255);\n"
"}\n"
"QComboBox:focus {\n"
"    border: 2px solid rgb(140, 146, 255);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(243, 244, 255);\n"
"    selection-background-color: rgb(140, 146, 255);\n"
"}")
        self.rez1_2 = QTextBrowser(self.frame_2)
        self.rez1_2.setObjectName(u"rez1_2")
        self.rez1_2.setGeometry(QRect(10, 320, 301, 111))
        self.button1_2 = QPushButton(self.frame_2)
        self.button1_2.setObjectName(u"button1_2")
        self.button1_2.setGeometry(QRect(90, 270, 131, 41))
        self.button1_2.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,70);\n"
"}")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(40, 140, 381, 91))
        self.label_12.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 0));")
        self.button1_que = QPushButton(self.centralwidget)
        self.button1_que.setObjectName(u"button1_que")
        self.button1_que.setGeometry(QRect(420, 110, 21, 21))
        self.button1_que.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,70);\n"
"}")
        self.button3_que = QPushButton(self.centralwidget)
        self.button3_que.setObjectName(u"button3_que")
        self.button3_que.setGeometry(QRect(1220, 110, 21, 21))
        self.button3_que.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,70);\n"
"}")
        self.button2_que = QPushButton(self.centralwidget)
        self.button2_que.setObjectName(u"button2_que")
        self.button2_que.setGeometry(QRect(840, 110, 21, 21))
        self.button2_que.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,70);\n"
"}")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(500, 150, 321, 621))
        self.frame_3.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 0));\n"
"")
        self.button2 = QPushButton(self.frame_3)
        self.button2.setObjectName(u"button2")
        self.button2.setGeometry(QRect(90, 520, 131, 41))
        self.button2.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,70);\n"
"}")
        self.rez2 = QTextBrowser(self.frame_3)
        self.rez2.setObjectName(u"rez2")
        self.rez2.setGeometry(QRect(0, 570, 321, 41))
        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(1, 1, 321, 16))
        self.label_14.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 0));")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(0, 140, 321, 21))
        self.label_15.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 0));")
        self.label_15.setTextFormat(Qt.AutoText)
        self.label_15.setAlignment(Qt.AlignCenter)
        self.tb2_Lstr = QTextEdit(self.frame_3)
        self.tb2_Lstr.setObjectName(u"tb2_Lstr")
        self.tb2_Lstr.setGeometry(QRect(0, 160, 321, 31))
        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(0, 340, 321, 41))
        self.label_17.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 0));")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(self.frame_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 430, 321, 41))
        self.label_18.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 0));")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.tb2_dop_nrs = QTextEdit(self.frame_3)
        self.tb2_dop_nrs.setObjectName(u"tb2_dop_nrs")
        self.tb2_dop_nrs.setGeometry(QRect(0, 390, 321, 31))
        self.tb2_dop_rs = QTextEdit(self.frame_3)
        self.tb2_dop_rs.setObjectName(u"tb2_dop_rs")
        self.tb2_dop_rs.setGeometry(QRect(0, 480, 321, 31))
        self.comboBox1_itu_3 = QComboBox(self.frame_3)
        self.comboBox1_itu_3.addItem("")
        self.comboBox1_itu_3.addItem("")
        self.comboBox1_itu_3.addItem("")
        self.comboBox1_itu_3.addItem("")
        self.comboBox1_itu_3.addItem("")
        self.comboBox1_itu_3.addItem("")
        self.comboBox1_itu_3.addItem("")
        self.comboBox1_itu_3.addItem("")
        self.comboBox1_itu_3.addItem("")
        self.comboBox1_itu_3.addItem("")
        self.comboBox1_itu_3.addItem("")
        self.comboBox1_itu_3.addItem("")
        self.comboBox1_itu_3.addItem("")
        self.comboBox1_itu_3.addItem("")
        self.comboBox1_itu_3.addItem("")
        self.comboBox1_itu_3.addItem("")
        self.comboBox1_itu_3.addItem("")
        self.comboBox1_itu_3.setObjectName(u"comboBox1_itu_3")
        self.comboBox1_itu_3.setEnabled(True)
        self.comboBox1_itu_3.setGeometry(QRect(0, 30, 321, 32))
        self.comboBox1_itu_3.setStyleSheet(u"QComboBox{\n"
"color: black;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 30px;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 2px solid rgb(194, 194, 255);\n"
"}\n"
"QComboBox:focus {\n"
"    border: 2px solid rgb(140, 146, 255);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(200, 130, 255);    \n"
"    background-color: rgb(243, 244, 255);\n"
"    selection-background-color: rgb(200, 130, 255);\n"
"}")
        self.comboBox1_itu_3.setEditable(False)
        self.comboBox1_itu_3.setDuplicatesEnabled(False)
        self.tb2_Lstr_2 = QTextEdit(self.frame_3)
        self.tb2_Lstr_2.setObjectName(u"tb2_Lstr_2")
        self.tb2_Lstr_2.setGeometry(QRect(0, 100, 321, 31))
        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(0, 70, 321, 21))
        self.label_16.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 0));")
        self.label_16.setTextFormat(Qt.AutoText)
        self.label_16.setAlignment(Qt.AlignCenter)
        self.comboBox2_pr = QComboBox(self.frame_3)
        self.comboBox2_pr.addItem("")
        self.comboBox2_pr.addItem("")
        self.comboBox2_pr.setObjectName(u"comboBox2_pr")
        self.comboBox2_pr.setGeometry(QRect(0, 290, 321, 32))
        self.comboBox2_pr.setStyleSheet(u"QComboBox{\n"
"color: black;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 30px;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 2px solid rgb(194, 194, 255);\n"
"}\n"
"QComboBox:focus {\n"
"    border: 2px solid rgb(140, 146, 255);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(243, 244, 255);\n"
"    selection-background-color: rgb(140, 146, 255);\n"
"}")
        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(1, 203, 321, 16))
        self.label_13.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 0));")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.comboBox2_per = QComboBox(self.frame_3)
        self.comboBox2_per.addItem("")
        self.comboBox2_per.addItem("")
        self.comboBox2_per.addItem("")
        self.comboBox2_per.setObjectName(u"comboBox2_per")
        self.comboBox2_per.setGeometry(QRect(0, 230, 321, 32))
        self.comboBox2_per.setStyleSheet(u"QComboBox{\n"
"color: black;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 30px;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 2px solid rgb(194, 194, 255);\n"
"}\n"
"QComboBox:focus {\n"
"    border: 2px solid rgb(140, 146, 255);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(243, 244, 255);\n"
"    selection-background-color: rgb(140, 146, 255);\n"
"}")
        self.label_20 = QLabel(self.frame_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(0, 270, 321, 16))
        self.label_20.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 0));")
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.button2.raise_()
        self.rez2.raise_()
        self.tb2_Lstr.raise_()
        self.tb2_dop_nrs.raise_()
        self.tb2_dop_rs.raise_()
        self.comboBox1_itu_3.raise_()
        self.tb2_Lstr_2.raise_()
        self.label_16.raise_()
        self.comboBox2_pr.raise_()
        self.label_13.raise_()
        self.comboBox2_per.raise_()
        self.label_20.raise_()
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(490, 100, 341, 42))
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 0));")
        self.label_19.setMargin(10)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.comboBox3_speed.setCurrentIndex(0)
        self.comboBox1_itu_4.setCurrentIndex(0)
        self.comboBox1_speed_2.setCurrentIndex(0)
        self.comboBox1_itu_2.setCurrentIndex(0)
        self.comboBox1_itu_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">\u0420\u0430\u0441\u0447\u0451\u0442 \u0434\u0438\u0441\u043f\u0435\u0440\u0441\u0438\u043e\u043d\u043d\u043e\u0439 \u0434\u043b\u0438\u043d\u044b</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">\u0412 \u0434\u0430\u043d\u043d\u043e\u043c \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u044b \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u043a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440\u043e\u0432 <br/>\u0434\u043b\u044f \u0440\u0430\u0441\u0447\u0435\u0442\u0430 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 \u0432 \u043e\u043f\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u043c \u0432\u043e\u043b\u043e\u043a\u043d\u0435</span></p></body></html>", None))
        self.button1.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442 \u0432\u043e\u043b\u043e\u043a\u043d\u0430</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043f\u0435\u0440\u0435\u0434\u0430\u0447\u0438</p></body></html>", None))
        self.comboBox3_speed.setItemText(0, QCoreApplication.translate("MainWindow", u"STM-1 (155 \u041c\u0431\u0438\u0442/\u0441)", None))
        self.comboBox3_speed.setItemText(1, QCoreApplication.translate("MainWindow", u"STM-4 (622 \u041c\u0431\u0438\u0442/\u0441)", None))
        self.comboBox3_speed.setItemText(2, QCoreApplication.translate("MainWindow", u"STM-16 (2,5 \u0413\u0431\u0438\u0442/\u0441)", None))
        self.comboBox3_speed.setItemText(3, QCoreApplication.translate("MainWindow", u"STM-64 (10 \u0413\u0431\u0438\u0442/\u0441)", None))
        self.comboBox3_speed.setItemText(4, QCoreApplication.translate("MainWindow", u"STM-256 (40 \u0413\u0431\u0438\u0442/\u0441)", None))
        self.comboBox3_speed.setItemText(5, QCoreApplication.translate("MainWindow", u"STM-1024 (160 \u0413\u0431\u0438\u0442/\u0441)", None))

        self.comboBox1_itu_4.setItemText(0, QCoreApplication.translate("MainWindow", u"G-652.A", None))
        self.comboBox1_itu_4.setItemText(1, QCoreApplication.translate("MainWindow", u"G-652.B", None))
        self.comboBox1_itu_4.setItemText(2, QCoreApplication.translate("MainWindow", u"G-652.C", None))
        self.comboBox1_itu_4.setItemText(3, QCoreApplication.translate("MainWindow", u"G-652.D", None))
        self.comboBox1_itu_4.setItemText(4, QCoreApplication.translate("MainWindow", u"G-653.A", None))
        self.comboBox1_itu_4.setItemText(5, QCoreApplication.translate("MainWindow", u"G-653.B", None))
        self.comboBox1_itu_4.setItemText(6, QCoreApplication.translate("MainWindow", u"G-654.A", None))
        self.comboBox1_itu_4.setItemText(7, QCoreApplication.translate("MainWindow", u"G-654.B", None))
        self.comboBox1_itu_4.setItemText(8, QCoreApplication.translate("MainWindow", u"G-654.C", None))
        self.comboBox1_itu_4.setItemText(9, QCoreApplication.translate("MainWindow", u"G-654.D", None))
        self.comboBox1_itu_4.setItemText(10, QCoreApplication.translate("MainWindow", u"G-654.E", None))
        self.comboBox1_itu_4.setItemText(11, QCoreApplication.translate("MainWindow", u"G-655.A", None))
        self.comboBox1_itu_4.setItemText(12, QCoreApplication.translate("MainWindow", u"G-655.B", None))
        self.comboBox1_itu_4.setItemText(13, QCoreApplication.translate("MainWindow", u"G-655.C", None))
        self.comboBox1_itu_4.setItemText(14, QCoreApplication.translate("MainWindow", u"G-655.D", None))
        self.comboBox1_itu_4.setItemText(15, QCoreApplication.translate("MainWindow", u"G-655.E", None))
        self.comboBox1_itu_4.setItemText(16, QCoreApplication.translate("MainWindow", u"G-656", None))

        self.comboBox1_itu_4.setCurrentText(QCoreApplication.translate("MainWindow", u"G-652.A", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">\u0420\u0430\u0441\u0447\u0451\u0442 \u0434\u043b\u0438\u043d\u044b \u0440\u0435\u0433\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u043e\u0433\u043e \u0443\u0447\u0430\u0441\u0442\u043a\u0430</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442 \u0432\u043e\u043b\u043e\u043a\u043d\u0430</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043f\u0435\u0440\u0435\u0434\u0430\u0447\u0438</p></body></html>", None))
        self.comboBox1_speed_2.setItemText(0, QCoreApplication.translate("MainWindow", u"STM-1 (155 \u041c\u0431\u0438\u0442/\u0441)", None))
        self.comboBox1_speed_2.setItemText(1, QCoreApplication.translate("MainWindow", u"STM-4 (622 \u041c\u0431\u0438\u0442/\u0441)", None))
        self.comboBox1_speed_2.setItemText(2, QCoreApplication.translate("MainWindow", u"STM-16 (2,5 \u0413\u0431\u0438\u0442/\u0441)", None))
        self.comboBox1_speed_2.setItemText(3, QCoreApplication.translate("MainWindow", u"STM-64 (10 \u0413\u0431\u0438\u0442/\u0441)", None))
        self.comboBox1_speed_2.setItemText(4, QCoreApplication.translate("MainWindow", u"STM-256 (40 \u0413\u0431\u0438\u0442/\u0441)", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c \u043f\u0435\u0440\u0435\u0434\u0430\u0442\u0447\u0438\u043a\u0430</p></body></html>", None))
        self.comboBox1_per.setItemText(0, QCoreApplication.translate("MainWindow", u"7 dB", None))
        self.comboBox1_per.setItemText(1, QCoreApplication.translate("MainWindow", u"9 dB", None))
        self.comboBox1_per.setItemText(2, QCoreApplication.translate("MainWindow", u"10 dB", None))

        self.comboBox1_itu_2.setItemText(0, QCoreApplication.translate("MainWindow", u"G-652.A", None))
        self.comboBox1_itu_2.setItemText(1, QCoreApplication.translate("MainWindow", u"G-652.B", None))
        self.comboBox1_itu_2.setItemText(2, QCoreApplication.translate("MainWindow", u"G-652.C", None))
        self.comboBox1_itu_2.setItemText(3, QCoreApplication.translate("MainWindow", u"G-652.D", None))
        self.comboBox1_itu_2.setItemText(4, QCoreApplication.translate("MainWindow", u"G-653.A", None))
        self.comboBox1_itu_2.setItemText(5, QCoreApplication.translate("MainWindow", u"G-653.B", None))
        self.comboBox1_itu_2.setItemText(6, QCoreApplication.translate("MainWindow", u"G-654.A", None))
        self.comboBox1_itu_2.setItemText(7, QCoreApplication.translate("MainWindow", u"G-654.B", None))
        self.comboBox1_itu_2.setItemText(8, QCoreApplication.translate("MainWindow", u"G-654.C", None))
        self.comboBox1_itu_2.setItemText(9, QCoreApplication.translate("MainWindow", u"G-654.D", None))
        self.comboBox1_itu_2.setItemText(10, QCoreApplication.translate("MainWindow", u"G-654.E", None))
        self.comboBox1_itu_2.setItemText(11, QCoreApplication.translate("MainWindow", u"G-655.A", None))
        self.comboBox1_itu_2.setItemText(12, QCoreApplication.translate("MainWindow", u"G-655.B", None))
        self.comboBox1_itu_2.setItemText(13, QCoreApplication.translate("MainWindow", u"G-655.C", None))
        self.comboBox1_itu_2.setItemText(14, QCoreApplication.translate("MainWindow", u"G-655.D", None))
        self.comboBox1_itu_2.setItemText(15, QCoreApplication.translate("MainWindow", u"G-655.E", None))
        self.comboBox1_itu_2.setItemText(16, QCoreApplication.translate("MainWindow", u"G-656", None))

        self.comboBox1_itu_2.setCurrentText(QCoreApplication.translate("MainWindow", u"G-652.A", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u0422\u0438\u043f \u043f\u0440\u0438\u0451\u043c\u043d\u0438\u043a\u0430</p></body></html>", None))
        self.comboBox1_pr.setItemText(0, QCoreApplication.translate("MainWindow", u"p-i-n \u0444\u043e\u0442\u043e\u0434\u0438\u043e\u0434", None))
        self.comboBox1_pr.setItemText(1, QCoreApplication.translate("MainWindow", u"\u043b\u0430\u0432\u0438\u043d\u043d\u044b\u0439 \u0444\u043e\u0442\u043e\u0434\u0438\u043e\u0434", None))

        self.button1_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u0412 \u0434\u0430\u043d\u043d\u043e\u043c \u043a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440\u0435 \u043e\u0441\u0443\u0449\u0435\u0441\u0442\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0440\u0430\u0441\u0447\u0451\u0442:<br/>\u0420\u0423 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u0437\u0430\u0442\u0443\u0445\u0430\u043d\u0438\u0435\u043c,<br/>\u0420\u0423 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u0445\u0440\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u0434\u0435\u0438\u0441\u043f\u0435\u0440\u0441\u0438\u0435\u0439,<br/>\u0420\u0423 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u043f\u043e\u043b\u044f\u0440\u0438\u0437\u0430\u0446\u0438\u043e\u043d\u043d\u043e\u0439 \u043c\u043e\u0434\u043e\u0432\u043e\u0439 \u0434\u0438\u0441\u043f\u0435\u0440\u0441\u0438\u0435\u0439.</p></body></html>", None))
        self.button1_que.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.button3_que.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.button2_que.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.button2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442 \u0432\u043e\u043b\u043e\u043a\u043d\u0430</p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u0421\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0434\u043b\u0438\u043d\u0430 \u043a\u0430\u0431\u0435\u043b\u044f. \u043a\u043c</p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u0412 \u0441\u043b\u0443\u0447\u0430\u0435 \u043d\u0430\u043b\u0438\u0447\u0438\u044f \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043d\u0435\u0440\u0430\u0437\u044a\u0435\u043c\u043d\u044b\u0445 <br/>\u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u0439, \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u0445 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e</p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u0412 \u0441\u043b\u0443\u0447\u0430\u0435 \u043d\u0430\u043b\u0438\u0447\u0438\u044f \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0437\u044a\u0435\u043c\u043d\u044b\u0445 <br/>\u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u0439, \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u0445 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e</p></body></html>", None))
        self.tb2_dop_nrs.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None))
        self.tb2_dop_rs.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None))
        self.comboBox1_itu_3.setItemText(0, QCoreApplication.translate("MainWindow", u"G-652.A", None))
        self.comboBox1_itu_3.setItemText(1, QCoreApplication.translate("MainWindow", u"G-652.B", None))
        self.comboBox1_itu_3.setItemText(2, QCoreApplication.translate("MainWindow", u"G-652.C", None))
        self.comboBox1_itu_3.setItemText(3, QCoreApplication.translate("MainWindow", u"G-652.D", None))
        self.comboBox1_itu_3.setItemText(4, QCoreApplication.translate("MainWindow", u"G-653.A", None))
        self.comboBox1_itu_3.setItemText(5, QCoreApplication.translate("MainWindow", u"G-653.B", None))
        self.comboBox1_itu_3.setItemText(6, QCoreApplication.translate("MainWindow", u"G-654.A", None))
        self.comboBox1_itu_3.setItemText(7, QCoreApplication.translate("MainWindow", u"G-654.B", None))
        self.comboBox1_itu_3.setItemText(8, QCoreApplication.translate("MainWindow", u"G-654.C", None))
        self.comboBox1_itu_3.setItemText(9, QCoreApplication.translate("MainWindow", u"G-654.D", None))
        self.comboBox1_itu_3.setItemText(10, QCoreApplication.translate("MainWindow", u"G-654.E", None))
        self.comboBox1_itu_3.setItemText(11, QCoreApplication.translate("MainWindow", u"G-655.A", None))
        self.comboBox1_itu_3.setItemText(12, QCoreApplication.translate("MainWindow", u"G-655.B", None))
        self.comboBox1_itu_3.setItemText(13, QCoreApplication.translate("MainWindow", u"G-655.C", None))
        self.comboBox1_itu_3.setItemText(14, QCoreApplication.translate("MainWindow", u"G-655.D", None))
        self.comboBox1_itu_3.setItemText(15, QCoreApplication.translate("MainWindow", u"G-655.E", None))
        self.comboBox1_itu_3.setItemText(16, QCoreApplication.translate("MainWindow", u"G-656", None))

        self.comboBox1_itu_3.setCurrentText(QCoreApplication.translate("MainWindow", u"G-652.A", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u0414\u043b\u0438\u043d\u0430 \u043a\u0430\u0431\u0435\u043b\u044f. \u043a\u043c</p></body></html>", None))
        self.comboBox2_pr.setItemText(0, QCoreApplication.translate("MainWindow", u"p-i-n \u0444\u043e\u0442\u043e\u0434\u0438\u043e\u0434", None))
        self.comboBox2_pr.setItemText(1, QCoreApplication.translate("MainWindow", u"\u043b\u0430\u0432\u0438\u043d\u043d\u044b\u0439 \u0444\u043e\u0442\u043e\u0434\u0438\u043e\u0434", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c \u043f\u0435\u0440\u0435\u0434\u0430\u0442\u0447\u0438\u043a\u0430</p></body></html>", None))
        self.comboBox2_per.setItemText(0, QCoreApplication.translate("MainWindow", u"7 dB", None))
        self.comboBox2_per.setItemText(1, QCoreApplication.translate("MainWindow", u"9 dB", None))
        self.comboBox2_per.setItemText(2, QCoreApplication.translate("MainWindow", u"10 dB", None))

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u0422\u0438\u043f \u043f\u0440\u0438\u0451\u043c\u043d\u0438\u043a\u0430</p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">\u0420\u0430\u0441\u0447\u0435\u0442 \u043e\u043f\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u0431\u044e\u0434\u0436\u0435\u0442\u0430</span></p></body></html>", None))
    # retranslateUi

