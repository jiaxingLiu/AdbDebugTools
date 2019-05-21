# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(551, 304)
        MainWindow.setMinimumSize(QtCore.QSize(551, 304))
        MainWindow.setMaximumSize(QtCore.QSize(551, 304))
        MainWindow.setMouseTracking(False)
        MainWindow.setAcceptDrops(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_export_log = QtWidgets.QPushButton(self.centralwidget)
        self.btn_export_log.setGeometry(QtCore.QRect(440, 230, 91, 23))
        self.btn_export_log.setObjectName("btn_export_log")
        self.btn_root = QtWidgets.QPushButton(self.centralwidget)
        self.btn_root.setGeometry(QtCore.QRect(10, 260, 91, 23))
        self.btn_root.setObjectName("btn_root")
        self.le_log_export = QtWidgets.QLineEdit(self.centralwidget)
        self.le_log_export.setGeometry(QtCore.QRect(110, 230, 301, 20))
        self.le_log_export.setReadOnly(True)
        self.le_log_export.setObjectName("le_log_export")
        self.btn_devices = QtWidgets.QPushButton(self.centralwidget)
        self.btn_devices.setGeometry(QtCore.QRect(140, 260, 121, 23))
        self.btn_devices.setObjectName("btn_devices")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 230, 91, 16))
        self.label.setObjectName("label")
        self.btn_sys_prop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sys_prop.setGeometry(QtCore.QRect(300, 260, 101, 23))
        self.btn_sys_prop.setObjectName("btn_sys_prop")
        self.te_show = QtWidgets.QTextEdit(self.centralwidget)
        self.te_show.setGeometry(QtCore.QRect(10, 10, 531, 211))
        self.te_show.setReadOnly(True)
        self.te_show.setObjectName("te_show")
        self.btn_reboot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reboot.setGeometry(QtCore.QRect(440, 260, 91, 23))
        self.btn_reboot.setObjectName("btn_reboot")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ADB调试工具1.0"))
        self.btn_export_log.setText(_translate("MainWindow", "export"))
        self.btn_root.setText(_translate("MainWindow", "一键root"))
        self.le_log_export.setText(_translate("MainWindow", "C:\\export_log"))
        self.btn_devices.setText(_translate("MainWindow", "查看设备信息"))
        self.label.setText(_translate("MainWindow", "Log保存地址："))
        self.btn_sys_prop.setText(_translate("MainWindow", "查看系统属性"))
        self.btn_reboot.setText(_translate("MainWindow", "一键重启"))

