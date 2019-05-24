import os
import sys
from datetime import datetime

from PyQt5 import QtWidgets

from test import Ui_MainWindow


class MainTemplete(QtWidgets.QMainWindow, Ui_MainWindow):
    secret = 0

    def __init__(self, parent=None):
        super(MainTemplete, self).__init__(parent)
        self.setupUi(self)

        self.bind_view_event()

    ##
    # Bind view event
    # ##
    def bind_view_event(self):
        print("========bind_view_event============")
        # 查看设备信息
        self.btn_devices.clicked.connect(self.btn_devices_info)
        # 一键root
        self.btn_onekey_root.clicked.connect(self.btn_onekey_root_click)
        # 重新挂载文件系统
        self.btn_remount_file.clicked.connect(self.btn_remount_file_click)
        # 一键重启
        self.btn_reboot.clicked.connect(self.btn_reboot_click)
        # 导出日志
        self.btn_export_log.clicked.connect(self.btn_export_click)
        # 查看系统属性
        self.btn_sys_prop.clicked.connect(self.btn_sys_prop_click)
        # 监测属性变化
        self.btn_check_prop.clicked.connect(self.btn_check_prop_click)
        # 一键清屏
        self.btn_clear_info.clicked.connect(self.btn_clear_info_click)
        # push
        self.btn_push.clicked.connect(self.btn_push_click)
        # 加密ADB
        self.btn_secret_adb.clicked.connect(self.btn_secret_adb_click)
        # 非加密ADB
        self.btn_normal_adb.clicked.connect(self.btn_normal_adb_click)
        # 处理拖入文件路径
        self.te_file_path.textChanged.connect(self.te_file_path_change)

    def btn_onekey_root_click(self):
        print("========btn_onekey_root_click============")
        self.show_log("adb root")

    def btn_remount_file_click(self):
        self.show_log("adb remount")

    def btn_reboot_click(self):
        self.show_log("adb reboot")

    def btn_devices_info(self):
        print("========btn_devices_info============")
        self.show_log("adb devices")

    def btn_export_click(self):
        try:
            os.rmdir("c:/export_log")
            os.mkdir("c:/export_log")
        except:
            Exception("export dir not exists")
        print(self.le_log_export.text())
        self.show_log("adb pull data/local/log " + self.le_log_export.text())

    def btn_sys_prop_click(self):
        self.show_log("adb shell getprop")

    def btn_check_prop_click(self):
        self.show_log("adb shell watchprops")

    def btn_clear_info_click(self):
        self.te_show.clear()

    def btn_push_click(self):
        print("adb push" + " " + self.te_file_path.toPlainText() + " " + self.cb_total_path.currentText())
        self.show_log(
            "adb push" + " " + self.te_file_path.toPlainText() + " "
            + self.cb_total_path.currentText() + " " + "&&" + " "
            + "adb reboot")

    def btn_secret_adb_click(self):
        self.secret = 1
        self.te_show.append("------------------" + str(datetime.now()) + "-------------------------")
        self.te_show.append("已切换为加密ADB...")

    def btn_normal_adb_click(self):
        self.secret = 0
        self.te_show.append("------------------" + str(datetime.now()) + "-------------------------")
        self.te_show.append("已切换为正常ADB...")

    def show_log(self, cmd):
        if self.secret == 0:
            print("非加密")
            self.te_show.append("------------------" + str(datetime.now()) + "-------------------------")
            self.te_show.append(os.popen(cmd).read())
        else:
            print("加密")
            self.te_show.append("------------------" + str(datetime.now()) + "-------------------------")
            self.te_show.append(os.popen(cmd.replace("adb", "sadb")).read())

    def te_file_path_change(self):
        if 0 == self.te_file_path.toPlainText().find('file:///'):
            self.te_file_path.setText(self.te_file_path.toPlainText().replace('file:///', ''))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainTemplete = MainTemplete()
    mainTemplete.show()
    sys.exit(app.exec_())
