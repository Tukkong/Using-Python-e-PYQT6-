# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHeaderView, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)
import icons__rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1286, 690)
        MainWindow.setStyleSheet(u"background-color: rgb(173, 173, 173);")
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border:none;\n"
"}\n"
"\n"
"QLabel{\n"
"	color:rgb(255, 255, 255);\n"
"}")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1321, 691))
        self.frame.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btnImport = QPushButton(self.frame)
        self.btnImport.setObjectName(u"btnImport")
        self.btnImport.setGeometry(QRect(180, 10, 131, 51))
        self.btnImport.setStyleSheet(u"border: solid 1px blue;\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"    border-radius: 20px;\n"
"    color: blue;\n"
"    background-color: white;\n"
"    transition: background-color 0.5s ease, color 0.5s ease, transform 0.5s ease;")
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 20):
            self.tableWidget.setColumnCount(20)
        font = QFont()
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(18, __qtablewidgetitem18)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 80, 1271, 561))
        self.tableWidget.setMouseTracking(True)
        self.tableWidget.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"font: 75 11pt \"Segoe UI\";\n"
"\n"
"\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.tableWidget.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.SelectedClicked)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setColumnCount(20)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.btnListar = QPushButton(self.frame)
        self.btnListar.setObjectName(u"btnListar")
        self.btnListar.setGeometry(QRect(970, 10, 131, 51))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.btnListar.setFont(font1)
        self.btnListar.setStyleSheet(u"	border: solid 1px blue;\n"
"    border-radius: 20px;\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"    color: blue;\n"
"    background-color: white;\n"
"    transition: background-color 0.5s ease, color 0.5s ease, transform 0.5s ease;")
        self.btnSalvar = QPushButton(self.frame)
        self.btnSalvar.setObjectName(u"btnSalvar")
        self.btnSalvar.setGeometry(QRect(1120, 10, 151, 51))
        self.btnSalvar.setStyleSheet(u"	border: solid 1px blue;\n"
"    border-radius: 20px;\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"    color: blue;\n"
"    background-color: white;\n"
"    transition: background-color 0.5s ease, color 0.5s ease, transform 0.5s ease;")
        self.comboBox2 = QComboBox(self.frame)
        self.comboBox2.setObjectName(u"comboBox2")
        self.comboBox2.setGeometry(QRect(720, 10, 201, 51))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.comboBox2.setFont(font2)
        self.tableWidget.raise_()
        self.btnImport.raise_()
        self.btnListar.raise_()
        self.btnSalvar.raise_()
        self.comboBox2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.btnImport.setText(QCoreApplication.translate("MainWindow", u"Importar Excel", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Filial", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nota Fiscal", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Data de Registro", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"CFOP", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o da Opera\u00e7\u00e3o", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Difal", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"FCP", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Juros/Multa", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"%", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Controle de Pagamento", None));
        ___qtablewidgetitem15 = self.tableWidget.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Data de Pagamento", None));
        ___qtablewidgetitem16 = self.tableWidget.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"NFD", None));
        ___qtablewidgetitem17 = self.tableWidget.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Valor NFD", None));
        ___qtablewidgetitem18 = self.tableWidget.horizontalHeaderItem(18)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00e3o", None));
        self.btnListar.setText(QCoreApplication.translate("MainWindow", u"Listar Planilha", None))
        self.btnSalvar.setText(QCoreApplication.translate("MainWindow", u"Salvar Dados", None))
    # retranslateUi

