# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\1\Desktop\kurs\application\ui\branch_employee.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1122, 725)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 1121, 701))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.contractsTable = QtWidgets.QTableWidget(self.tab)
        self.contractsTable.setGeometry(QtCore.QRect(10, 220, 1091, 391))
        self.contractsTable.setObjectName("contractsTable")
        self.contractsTable.setColumnCount(5)
        self.contractsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.contractsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.contractsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.contractsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.contractsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.contractsTable.setHorizontalHeaderItem(4, item)
        self.contractsTable.verticalHeader().setVisible(False)
        self.addcontractButton = QtWidgets.QPushButton(self.tab)
        self.addcontractButton.setGeometry(QtCore.QRect(180, 620, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addcontractButton.setFont(font)
        self.addcontractButton.setObjectName("addcontractButton")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(480, 170, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.deletecontractButton = QtWidgets.QPushButton(self.tab)
        self.deletecontractButton.setGeometry(QtCore.QRect(740, 620, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deletecontractButton.setFont(font)
        self.deletecontractButton.setObjectName("deletecontractButton")
        self.searchcontractButton = QtWidgets.QPushButton(self.tab)
        self.searchcontractButton.setGeometry(QtCore.QRect(460, 620, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchcontractButton.setFont(font)
        self.searchcontractButton.setObjectName("searchcontractButton")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(390, 0, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(160, 50, 381, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(160, 140, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(160, 90, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(620, 50, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(620, 150, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(620, 100, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(120, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.addclientcontractButton = QtWidgets.QPushButton(self.tab_2)
        self.addclientcontractButton.setGeometry(QtCore.QRect(450, 590, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addclientcontractButton.setFont(font)
        self.addclientcontractButton.setObjectName("addclientcontractButton")
        self.deleteclientcontractButton = QtWidgets.QPushButton(self.tab_2)
        self.deleteclientcontractButton.setGeometry(QtCore.QRect(780, 590, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deleteclientcontractButton.setFont(font)
        self.deleteclientcontractButton.setObjectName("deleteclientcontractButton")
        self.clientsTable = QtWidgets.QTableWidget(self.tab_2)
        self.clientsTable.setGeometry(QtCore.QRect(0, 60, 351, 521))
        self.clientsTable.setObjectName("clientsTable")
        self.clientsTable.setColumnCount(2)
        self.clientsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.clientsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientsTable.setHorizontalHeaderItem(1, item)
        self.clientsTable.verticalHeader().setVisible(False)
        self.addclientButton = QtWidgets.QPushButton(self.tab_2)
        self.addclientButton.setGeometry(QtCore.QRect(0, 590, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addclientButton.setFont(font)
        self.addclientButton.setObjectName("addclientButton")
        self.deleteclientButton = QtWidgets.QPushButton(self.tab_2)
        self.deleteclientButton.setGeometry(QtCore.QRect(240, 590, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deleteclientButton.setFont(font)
        self.deleteclientButton.setObjectName("deleteclientButton")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(670, 130, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(450, 20, 381, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(450, 60, 381, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(450, 100, 381, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.contractsTable_2 = QtWidgets.QTableWidget(self.tab_2)
        self.contractsTable_2.setGeometry(QtCore.QRect(360, 170, 751, 411))
        self.contractsTable_2.setObjectName("contractsTable_2")
        self.contractsTable_2.setColumnCount(4)
        self.contractsTable_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.contractsTable_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.contractsTable_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.contractsTable_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.contractsTable_2.setHorizontalHeaderItem(3, item)
        self.contractsTable_2.verticalHeader().setVisible(False)
        self.searchclientButton = QtWidgets.QPushButton(self.tab_2)
        self.searchclientButton.setGeometry(QtCore.QRect(120, 590, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchclientButton.setFont(font)
        self.searchclientButton.setObjectName("searchclientButton")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1122, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Сотрудник"))
        item = self.contractsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.contractsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Клиент"))
        item = self.contractsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Вид страхования"))
        item = self.contractsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Сумма страхования"))
        item = self.contractsTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Дата заключения"))
        self.addcontractButton.setText(_translate("MainWindow", "Добавить"))
        self.label.setText(_translate("MainWindow", "Договоры"))
        self.deletecontractButton.setText(_translate("MainWindow", "Убрать"))
        self.searchcontractButton.setText(_translate("MainWindow", "Найти"))
        self.label_14.setText(_translate("MainWindow", "Информация о филиале"))
        self.label_3.setText(_translate("MainWindow", "Компания:"))
        self.label_5.setText(_translate("MainWindow", "Город:"))
        self.label_4.setText(_translate("MainWindow", "Название:"))
        self.label_6.setText(_translate("MainWindow", "Адрес:"))
        self.label_8.setText(_translate("MainWindow", "Количество сотрудников:"))
        self.label_7.setText(_translate("MainWindow", "Телефон:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Договоры"))
        self.label_9.setText(_translate("MainWindow", "Клиенты"))
        self.addclientcontractButton.setText(_translate("MainWindow", "Добавить"))
        self.deleteclientcontractButton.setText(_translate("MainWindow", "Убрать"))
        item = self.clientsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.clientsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ФИО"))
        self.addclientButton.setText(_translate("MainWindow", "Добавить"))
        self.deleteclientButton.setText(_translate("MainWindow", "Убрать"))
        self.label_10.setText(_translate("MainWindow", "Договоры"))
        self.label_11.setText(_translate("MainWindow", "Дата рождения:"))
        self.label_12.setText(_translate("MainWindow", "Социальное положение:"))
        self.label_13.setText(_translate("MainWindow", "Телефон:"))
        item = self.contractsTable_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.contractsTable_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Вид страхования"))
        item = self.contractsTable_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Сумма страхования"))
        item = self.contractsTable_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Дата заключения"))
        self.searchclientButton.setText(_translate("MainWindow", "Найти"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Клиенты"))
