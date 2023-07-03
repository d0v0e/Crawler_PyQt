# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from sys import argv,exit
from PyQt5 import QtWidgets
import crawler #crawlert文件

if __name__ == '__main__':
    #获取UIC窗口操作权限
    app = QtWidgets.QApplication(argv)
    MainWindow = QtWidgets.QMainWindow()
    #调自定义的界面（即刚转换的.py对象）
    Ui = crawler.Ui_MainWindow()
    Ui.setupUi(MainWindow)
    #显示窗口并释放资源
    MainWindow.show()
    exit(app.exec_())