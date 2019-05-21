import os
import sys
from datetime import datetime

from PyQt5 import QtWidgets

from test import Ui_MainWindow


class MainTemplete(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainTemplete, self).__init__(parent)
        self.setupUi(self)

        self.bind_view_event()

    ##
    # Bind view event
    # ##
    def bind_view_event(self):
        print("========bind_view_event============")
        self.btn_devices.clicked.connect(self.btn_devices_info)
        self.btn_root.clicked.connect(self.btn_root_click)
        self.btn_reboot.clicked.connect(self.btn_reboot_click)
        self.btn_export_log.clicked.connect(self.btn_export_click)
        self.btn_sys_prop.clicked.connect(self.btn_sys_prop_click)

    # 一键root
    def btn_root_click(self):
        print("========btn_devices_info============")
        self.show_log("adb root && adb remount")

    # 一键重启
    def btn_reboot_click(self):
        self.show_log("adb reboot")

    # 查看设备信息
    def btn_devices_info(self):
        print("========btn_devices_info============")
        self.show_log("adb devices")

    # 导出日志
    def btn_export_click(self):
        try:
            os.rmdir("c:/export_log")
            os.mkdir("c:/export_log")
        except:
            Exception("export dir not exists")
        print(self.le_log_export.text())
        self.show_log("adb pull data/local/log " + self.le_log_export.text())

    # 显示操作记录
    def show_log(self, cmd):
        self.te_show.append("------------------" + str(datetime.now()) + "-------------------------")
        self.te_show.append(os.popen(cmd).read())

    # 显示系统属性
    def btn_sys_prop_click(self):
        self.show_log("adb shell getprop")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainTemplete = MainTemplete()
    mainTemplete.show()
    sys.exit(app.exec_())
