# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\1\Desktop\kurs\application\ui\employee.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_clientsTable(object):
    def setupUi(self, clientsTable):
        clientsTable.setObjectName("clientsTable")
        clientsTable.resize(977, 536)
        font = QtGui.QFont()
        font.setPointSize(10)
        clientsTable.setFont(font)
        self.tabWidget = QtWidgets.QWidget()
        self.tabWidget.setObjectName("tabWidget")
        self.label = QtWidgets.QLabel(self.tabWidget)
        self.label.setGeometry(QtCore.QRect(430, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.tabWidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 951, 391))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.pushButton = QtWidgets.QPushButton(self.tabWidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 460, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tabWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 460, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        clientsTable.addTab(self.tabWidget, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 460, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(440, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 460, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 60, 951, 391))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.tableWidget_2.verticalHeader().setVisible(False)
        clientsTable.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(250, 10, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(310, 100, 231, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(30, 270, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 220, 231, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(30, 210, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 160, 231, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(310, 280, 231, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(310, 340, 231, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(30, 330, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(310, 400, 231, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(30, 390, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        clientsTable.addTab(self.tab_2, "")

        self.retranslateUi(clientsTable)
        clientsTable.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(clientsTable)

    def retranslateUi(self, clientsTable):
        _translate = QtCore.QCoreApplication.translate
        clientsTable.setWindowTitle(_translate("clientsTable", "Сотрудник"))
        self.label.setText(_translate("clientsTable", "Договоры"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("clientsTable", "№"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("clientsTable", "Филиал"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("clientsTable", "Клиент"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("clientsTable", "Вид страхования"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("clientsTable", "Сумма страхования"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("clientsTable", "Дата заключения"))
        self.pushButton.setText(_translate("clientsTable", "Добавить"))
        self.pushButton_2.setText(_translate("clientsTable", "Убрать"))
        clientsTable.setTabText(clientsTable.indexOf(self.tabWidget), _translate("clientsTable", "Договоры"))
        self.pushButton_3.setText(_translate("clientsTable", "Убрать"))
        self.label_9.setText(_translate("clientsTable", "Клиенты"))
        self.pushButton_4.setText(_translate("clientsTable", "Добавить"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("clientsTable", "№"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("clientsTable", "ФИО"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("clientsTable", "Дата рождения"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("clientsTable", "Социальное положение"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("clientsTable", "Телефон"))
        clientsTable.setTabText(clientsTable.indexOf(self.tab_3), _translate("clientsTable", "Клиенты"))
        self.label_2.setText(_translate("clientsTable", "Информация о филиале"))
        self.label_6.setText(_translate("clientsTable", "Адрес:"))
        self.label_3.setText(_translate("clientsTable", "Компания:"))
        self.label_5.setText(_translate("clientsTable", "Город:"))
        self.label_4.setText(_translate("clientsTable", "Название:"))
        self.label_7.setText(_translate("clientsTable", "Телефон:"))
        self.label_8.setText(_translate("clientsTable", "Количество сотрудников:"))
        clientsTable.setTabText(clientsTable.indexOf(self.tab_2), _translate("clientsTable", "О филиале"))