# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\SuperMarket\QtUI\UI\WareRegisterWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WareRegisterWindow(object):
    def setupUi(self, WareRegisterWindow):
        WareRegisterWindow.setObjectName("WareRegisterWindow")
        WareRegisterWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(WareRegisterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 801, 101))
        self.textBrowser.setObjectName("textBrowser")
        self.Submit_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Submit_PushButton.setGeometry(QtCore.QRect(440, 470, 93, 28))
        self.Submit_PushButton.setObjectName("Submit_PushButton")
        self.Clear_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Clear_PushButton.setGeometry(QtCore.QRect(290, 470, 93, 28))
        self.Clear_PushButton.setObjectName("Clear_PushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(230, 160, 351, 271))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Name_Label = QtWidgets.QLabel(self.widget)
        self.Name_Label.setObjectName("Name_Label")
        self.gridLayout.addWidget(self.Name_Label, 0, 0, 1, 1)
        self.Name_LineEdit = QtWidgets.QLineEdit(self.widget)
        self.Name_LineEdit.setObjectName("Name_LineEdit")
        self.gridLayout.addWidget(self.Name_LineEdit, 0, 1, 1, 1)
        self.ID_Label = QtWidgets.QLabel(self.widget)
        self.ID_Label.setObjectName("ID_Label")
        self.gridLayout.addWidget(self.ID_Label, 1, 0, 1, 1)
        self.ID_LineEdit = QtWidgets.QLineEdit(self.widget)
        self.ID_LineEdit.setObjectName("ID_LineEdit")
        self.gridLayout.addWidget(self.ID_LineEdit, 1, 1, 1, 1)
        self.Format_Label = QtWidgets.QLabel(self.widget)
        self.Format_Label.setObjectName("Format_Label")
        self.gridLayout.addWidget(self.Format_Label, 2, 0, 1, 1)
        self.Format_LineEdit = QtWidgets.QLineEdit(self.widget)
        self.Format_LineEdit.setObjectName("Format_LineEdit")
        self.gridLayout.addWidget(self.Format_LineEdit, 2, 1, 1, 1)
        self.Quantity_Label = QtWidgets.QLabel(self.widget)
        self.Quantity_Label.setObjectName("Quantity_Label")
        self.gridLayout.addWidget(self.Quantity_Label, 3, 0, 1, 1)
        self.Quantity_SpinBox = QtWidgets.QSpinBox(self.widget)
        self.Quantity_SpinBox.setObjectName("Quantity_SpinBox")
        self.gridLayout.addWidget(self.Quantity_SpinBox, 3, 1, 1, 1)
        self.MaxStock_Label = QtWidgets.QLabel(self.widget)
        self.MaxStock_Label.setObjectName("MaxStock_Label")
        self.gridLayout.addWidget(self.MaxStock_Label, 4, 0, 1, 1)
        self.MaxStock_SpinBox = QtWidgets.QSpinBox(self.widget)
        self.MaxStock_SpinBox.setObjectName("MaxStock_SpinBox")
        self.gridLayout.addWidget(self.MaxStock_SpinBox, 4, 1, 1, 1)
        self.MinStock_Label = QtWidgets.QLabel(self.widget)
        self.MinStock_Label.setObjectName("MinStock_Label")
        self.gridLayout.addWidget(self.MinStock_Label, 5, 0, 1, 1)
        self.MinStock_SpinBox = QtWidgets.QSpinBox(self.widget)
        self.MinStock_SpinBox.setObjectName("MinStock_SpinBox")
        self.gridLayout.addWidget(self.MinStock_SpinBox, 5, 1, 1, 1)
        WareRegisterWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WareRegisterWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        WareRegisterWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WareRegisterWindow)
        self.statusbar.setObjectName("statusbar")
        WareRegisterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(WareRegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(WareRegisterWindow)

    def retranslateUi(self, WareRegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        WareRegisterWindow.setWindowTitle(_translate("WareRegisterWindow", "商品注册"))
        self.textBrowser.setHtml(_translate("WareRegisterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">商品登记界面</span></p></body></html>"))
        self.Submit_PushButton.setText(_translate("WareRegisterWindow", "提交"))
        self.Clear_PushButton.setText(_translate("WareRegisterWindow", "清空"))
        self.Name_Label.setText(_translate("WareRegisterWindow", "商品名称"))
        self.ID_Label.setText(_translate("WareRegisterWindow", "商品编号"))
        self.Format_Label.setText(_translate("WareRegisterWindow", "商品规格"))
        self.Quantity_Label.setText(_translate("WareRegisterWindow", "商品数量"))
        self.MaxStock_Label.setText(_translate("WareRegisterWindow", "最大库存"))
        self.MinStock_Label.setText(_translate("WareRegisterWindow", "最小库存"))

