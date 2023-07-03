# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crawler.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from requests import get
from bs4 import BeautifulSoup
from re import findall
from tkinter import filedialog, Tk
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1071, 632)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setWindowIcon(QIcon(':/images/image.ico'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(70, 80, 101, 41))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 150, 101, 41))
        self.label_2.setObjectName("label_2")
        self.lineEdit_url = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_url.setGeometry(QtCore.QRect(210, 80, 781, 41))
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.RunButton = QtWidgets.QPushButton(self.centralwidget)
        self.RunButton.setGeometry(QtCore.QRect(60, 240, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RunButton.setFont(font)
        self.RunButton.setIconSize(QtCore.QSize(18, 18))
        self.RunButton.setObjectName("RunButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(210, 160, 781, 381))
        self.textBrowser.setObjectName("textBrowser")
        self.FOutButton = QtWidgets.QPushButton(self.centralwidget)
        self.FOutButton.setGeometry(QtCore.QRect(60, 330, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FOutButton.setFont(font)
        self.FOutButton.setIconSize(QtCore.QSize(18, 18))
        self.FOutButton.setObjectName("FOutButton")
        self.ClearButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearButton.setGeometry(QtCore.QRect(60, 420, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ClearButton.setFont(font)
        self.ClearButton.setIconSize(QtCore.QSize(18, 18))
        self.ClearButton.setObjectName("ClearButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.RunButton.clicked.connect(self.runCrawler) # type: ignore
        self.FOutButton.clicked.connect(self.saveFile) # type: ignore
        self.ClearButton.clicked.connect(self.clearText) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "爬虫v1.0上电计算机DEMO"))
        self.label_1.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:11pt;\">输入网址：</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:11pt;\">爬取结果：</span></p></body></html>"))
        self.lineEdit_url.setText(_translate("MainWindow", "https://www.chinanews.com.cn/"))
        self.RunButton.setText(_translate("MainWindow", "开始爬取"))
        self.FOutButton.setText(_translate("MainWindow", "导出结果"))
        self.ClearButton.setText(_translate("MainWindow", "清空内容"))

    def runCrawler(self):
        url = self.lineEdit_url.text()
        keyword = ''
        filename = ''
        print(url)
        try:
            scrap_url(self, url, keyword, filename)

        except Exception as e:
            self.textBrowser.append(str(e))

    def clearText(self):
        self.textBrowser.clear()

    def saveFile(self):
        Folderpath = ''
        Filepath = ''
        url = self.lineEdit_url.text()
        keyword = ''
        filename = ''
        try:
            root = Tk()
            root.withdraw()
            Folderpath = filedialog.askdirectory()  # 获得选择好的文件夹
            #Filepath = filedialog.askopenfilename()  # 获得选择好的文件
            if Folderpath != '':
                filename = Folderpath + '/output.txt'
                scrap_url(self, url, keyword, filename)
            elif Filepath != '':
                filename = Filepath
                scrap_url(self, url, keyword, filename)
        except Exception as e:
            self.textBrowser.append("\n文件保存失败")
            self.textBrowser.append(str(e))
        else:
            self.textBrowser.clear()
            self.textBrowser.append("\n输出结果成功保存到：%s" % filename)

def scrap_url(self, url, keyword='', filename=''):
    self.textBrowser.append("\n正在获取%s页面中的标题信息...\n" % url)
    my_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34"}

    response = get(url, headers=my_headers)
    # print(response.status_code)
    if response.status_code >= 400:
        self.textBrowser.append("页面访问失败！请检查URL或者网络设置！")
        exit(0)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    news_list_mus2 = soup.select('div[class="w1280"] div div ul li')

    all_titles = []
    for ele in news_list_mus2:
        res1 = findall(r"<a.*?href=.*?shtml.*?title=(.*?)>", str(ele))
        if res1 != []:
            all_titles.append(res1[0])
            # print("res1=%s"%res1)
            continue
        res2 = findall(r"<a.*?href=.*?shtml\">(.*?)</a>", str(ele))
        if 'img ' in str(res2):
            continue
        if 'shtml' in str(res2):
            res2 = findall(r".*?shtml\">(.*?)", str(res2))
        if res2 != []:
            # print("res2=%s"%res2)
            if res2[0] == '':
                continue
            all_titles.append(res2[0])
    # print(all_titles)

    if all_titles != []:
        self.textBrowser.append("已成功获取到该页面的标题信息！\n")
        if keyword == '':
            self.textBrowser.append("所有查找结果如下：\n")
        else:
            self.textBrowser.append("包含关键字 “" + str(keyword) + "” 的信息查找结果如下：\n")

    if filename != '':
        f = open(filename, "w")
        if keyword == '':
            for each_title in all_titles:
                f.write(each_title + '\n')
                self.textBrowser.append(each_title)
        else:
            for each_title in all_titles:
                if keyword in each_title:
                    f.write(each_title + '\n')
                    self.textBrowser.append(each_title)
        self.textBrowser.append("\n输出结果成功保存到：%s" % filename)
        f.close()
    else:
        if keyword == '':
            for each_title in all_titles:
                self.textBrowser.append(each_title)
        else:
            for each_title in all_titles:
                if str(keyword) in each_title:
                    self.textBrowser.append(each_title)