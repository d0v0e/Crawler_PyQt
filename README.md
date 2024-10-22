

# Crawler_PyQt

## 零基础PyCharm+PyQt+QTDesigner实现QT前端界面开发

#### 0x00 简介

* 这个项目是一个简单的Python爬虫demo，该练手小项目希望能帮助到大家，熟悉Python和QT的整合开发。

##### 运行环境及所需工具

* 编译器：PyCharm
* Python版本：3.6+
* QT Designer版本：5.15.2

##### 功能介绍

* 点击“开始爬取”即可对指定网址进行爬取，并将内容显示在界面中。目前仅能分析中国新闻网这一个URL，可以将页面中所有新闻的标题输出。

<img src=".\pyqt.assets\image-20230703150536932.png" alt="image-20230703150536932" style="zoom:80%;" />

* 点击“导出结果”即可选择文件夹进行结果导出，

<img src=".\pyqt.assets\image-20230703150914949.png" alt="image-20230703150914949" style="zoom:50%;" />

* 导出完成后会有路径提示。

<img src=".\pyqt.assets\image-20230703151014987.png" alt="image-20230703151014987" style="zoom:80%;" />

接下来第1到4节将介绍PyCharm和QT Designer的基本用法以及环境配置，第5节将详细介绍本项目实现过程。



#### 0x01 安装工具

* 首先需要安装 PyCharm 和 QtDesigner，PyCharm 直接在官网上选择社区版就可以免费下载了， QtDesigner 也需要单独下载安装。若之前安装过 QtCreator，可能同时也安装了 QtDesigner，在windows搜索栏中搜索 Designer 即可找到该应用。(一般都有安装)

<img src=".\pyqt.assets\image-20230703102854607.png" alt="image-20230703102854607" style="zoom:80%;" />

如果只有QtCreator的话，可以安装pyqt5-tools，然后在工具目录找到，例如可以是

```
D:\ProgramData\Anaconda3\Library\bin\designer.exe
D:\ProgramData\Anaconda3\envs\py3-10\Lib\site-packages\qt5_applications\Qt\bin\designer.exe
F:\Python\python3.6.3\Lib\site-packages\pyqt5_tools\designer.exe
```

pip安装

```
pip install pyqt5-tools
```

若安装时报错：error: Microsoft Visual C++ 14.0 or greater is required.

需要安装Visual C++ 或者使用Conda添加环境

```
conda install libpython m2w64-toolchain -c msys2
```

* 为了方便后续配置，选择两次打开文件位置，找到最终的应用程序路径。

例如我的就在这个路径：

```
D:\Qt\5.15.2\mingw81_64\bin\designer.exe
```

<img src=".\pyqt.assets\image-20230703103059881.png" alt="image-20230703103059881" style="zoom:80%;" />



#### 0x02 PyCharm新建项目

* 打开PyCharm，新建一个qt_helloworld项目

<img src=".\pyqt.assets\image-20230703101836762.png" alt="image-20230703101836762" style="zoom:80%;" />

* PyCharm会自动帮我们生成一个main.py文件，点击运行可看到Hi，PyCharm的输出

<img src=".\pyqt.assets\image-20230703102202476.png" alt="image-20230703102202476" style="zoom:80%;" />

#### 0x03 PyCharm配置外部工具

* 选择 File-Settings 打开设置界面

<img src=".\pyqt.assets\image-20230703104821893.png" alt="image-20230703104821893" style="zoom:80%;" />

* 在 Tools--->External Tools 找到外部工具配置界面，点击加号新建工具，添加 QT Designer 工具。

Program（应用程序）把之前找到的应用路径输入，例如我这里是：

```
D:\Qt\5.15.2\mingw81_64\bin\designer.exe
```

Arguments（实参）留空；

Working directory（工作目录）设为 `$FileDir$` 表示默认当前 PyCharm 的工作目录，可根据实际情况调整。

<img src=".\pyqt.assets\image-20230703105146838.png" alt="image-20230703105146838" style="zoom:80%;" />

* 同理，我们再配置python自带的pyUIC工具。

Program 为你电脑里Python路径下的`\Scripts\pyuic5.exe`，或者`pyuic5.bat`例如我这里是

```
C:\Users\12420\AppData\Local\Programs\Python\Python37\Scripts\pyuic5.exe
```

Arguments 这里设置成这个命令，表示将当前文件转化成py文件，使用该工具时会自动执行该命令，在这里就是将QT Designer生成的`.ui`文件转化为`.py`文件

```
$FileName$ -o $FileNameWithoutExtension$.py
```

Working directory 这里同上，我这里设成当前工作目录

```
$FileDir$
```

配置完成就可以开始设计界面了

<img src=".\pyqt.assets\image-20230703105703418.png" alt="image-20230703105703418" style="zoom:80%;" />

#### 0x04 QT Designer 界面设计

* 通过 PyCharm 打开 QT Designer，选择 Tools--->External Tools--->QT Designer。

<img src=".\pyqt.assets\image-20230703111559257.png" alt="image-20230703111559257" style="zoom:80%;" />

* 点击后会打开QT Designer的界面，这里我们以 `Main Window` 窗口为例，点击创建即可。

<img src=".\pyqt.assets\image-20230703111757407.png" alt="image-20230703111757407" style="zoom:80%;" />

* 选择左侧 Display Widgets 栏下的Label标签，拖入界面即可创建一个文本，双击可输入HelloWorld!

<img src=".\pyqt.assets\image-20230703112035622.png" alt="image-20230703112035622" style="zoom:80%;" />

* 右键选择“改变多信息文本...”可修改文本框和字体的基本属性，这里我们可以把字体调大一些。

<img src=".\pyqt.assets\image-20230703112233787.png" alt="image-20230703112233787" style="zoom: 50%;" />

* 点击文件-->保存，或者 `Ctrl+s` 保存项目为`helloworld.ui`，可看见保存的路径为PyCharm的工作路径。

<img src=".\pyqt.assets\image-20230703112350438.png" alt="image-20230703112350438" style="zoom: 67%;" />

#### 0x05 导入PyCharm编辑

* 使用pyUIC工具将`helloworld.ui`转化为`helloworld.py`。

<img src=".\pyqt.assets\image-20230703112829361.png" alt="image-20230703112829361" style="zoom:80%;" />

* 这里转化的本质实际上就是调用了pyuic5.exe，通过之前设好的指令转化，在PyCharm的命令窗口可看见转化逻辑。通过cmd执行命令也是同样可行的。

<img src=".\pyqt.assets\image-20230703113127792.png" alt="image-20230703113127792" style="zoom:80%;" />

* 转化成功后可看到`helloworld.py`文件

<img src=".\pyqt.assets\image-20230703112948210.png" alt="image-20230703112948210" style="zoom:80%;" />

`helloworld.py`

```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helloworld.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 250, 91, 21))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">HelloWorld！</span></p></body></html>"))

```

* 修改main.py中的文件，替换为如下代码。其中需要引入刚刚生成的helloworld文件，并设置主函数调用窗口。

`main.py`

```python
import sys
from PyQt5 import QtWidgets
import helloworld #导入helloworld文件

if __name__ == '__main__':
    #获取UIC窗口操作权限
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    #调自定义的界面（即刚转换的.py对象）
    Ui = helloworld.Ui_MainWindow() #这里也引用了一次helloworld.py文件的名字注意
    Ui.setupUi(MainWindow)
    #显示窗口并释放资源
    MainWindow.show()
    sys.exit(app.exec_())
```

* 在`helloworld.py`中发现导入包爆红。我们需要在PyCharm中导入PyQt5包。

注：之前在Windows cmd中通过指令`pip install PyQt5`是可以安装的，但是由于PyCharm的每个项目都会分配一个全新的虚拟环境，我们还需要在其中重新导入包。

<img src=".\pyqt.assets\image-20230703114255754.png" alt="image-20230703114255754" style="zoom:80%;" />

* 可以在PyCharm的命令行窗口输入pip安装指令安装，也可以在设置中查找包进行添加：点击Files--Settings打开设置界面，选择Project--->Python Interpreter查看当前的包，点击加号进行添加。

<img src=".\pyqt.assets\image-20230703114757128.png" alt="image-20230703114757128" style="zoom:80%;" />

* 查找PyQt5，点击Install Package进行安装即可。

<img src=".\pyqt.assets\image-20230703114952474.png" alt="image-20230703114952474" style="zoom:80%;" />

* 安装完成后可看到安装好的包

<img src=".\pyqt.assets\image-20230703115158122.png" alt="image-20230703115158122" style="zoom:80%;" />

* 回到代码界面，点击绿色三角运行程序即可生成程序界面。

<img src=".\pyqt.assets\image-20230703115347068.png" alt="image-20230703115347068" style="zoom:80%;" />

* 成功生成了界面，但可发现HelloWorld标签并没有显示完全。这是由于QT Designer设计好的标签大小在实际转化中会产生误差，例如这里标签宽度变小了导致显示不完全。

<img src=".\pyqt.assets\image-20230703115430091.png" alt="image-20230703115430091" style="zoom:50%;" />

* 我们回到QT Designer增加标签的长度，保存并重新将helloworld.ui转化为py文件。

<img src=".\pyqt.assets\image-20230703115802428.png" alt="image-20230703115802428" style="zoom:50%;" />

* 重新运行，可发现这次显示完全了。

<img src=".\pyqt.assets\image-20230703115915850.png" alt="image-20230703115915850" style="zoom:50%;" />

至此，已经成功配置了PyQt的环境、熟悉了PyCharm和QT Designer的基本使用，并且对开发PyQt前端界面的完整流程有所熟悉。下面我将再讲解一个项目，这次会在QT Desinger中设计更加复杂的界面，包含输入输出框，熟悉前后端的交互。





#### 0x06 实际案例

* 一个实际案例为例，假设我打算做一个爬虫软件界面，要求在前端可以输入url，并将该url的爬取结果输出在界面上。
* 同上，新建项目后，选择 Tools--->External Tools--->QT Designer 打开QT界面，并新建一个 `Main Window` 窗口，并拖动左侧的组建设计软件界面。软件界面如下，红色字体标识组建名称。

<img src=".\pyqt.assets\image-20230703135913400.png" alt="image-20230703135913400" style="zoom:80%;" />

* 左上角的标题名称可在右侧的属性编辑器中，搜索关键词title进行搜索并修改；

<img src=".\pyqt.assets\image-20230703140050081.png" alt="image-20230703140050081" style="zoom:50%;" />

* 搜索icon，可找到图标对应的属性，这里将Theme改成你想要调用的图标文件名。注：图标一般为icon文件，需要将`.png`转化为`.ico`文件，并需要把该资源文件导入PyCharm才可以使用，这里大小默认是24x24。

<img src=".\pyqt.assets\image-20230703141319222.png" alt="image-20230703141319222" style="zoom:50%;" />

* 在右侧的对象查看器可查看所有对象，并可修改对象名称，这里我将三个按钮的名称修改为`RunButton` 、`FOutButton`、`ClearButton`，条形文本编辑框改为 `lineEdit_url`，文本浏览框保持不变，方便后续代码编辑区分。

<img src=".\pyqt.assets\image-20230703140211185.png" alt="image-20230703140211185" style="zoom:50%;" />

* 在右侧的信号/槽编辑器添加信号发生器和接收器，这里表示在获取到 `clicked()` 信号即点击信号后，通过对应的按钮会给接收者发送信号，随即接收者调用槽函数进行一些操作。这里最重要的是定义发送者和信号产生的方法，接收者和槽函数我们之后会修改成自定义的内容。

<img src=".\pyqt.assets\image-20230703140444618.png" alt="image-20230703140444618" style="zoom:50%;" />

* 保存ui文件，并按照之前的方法，使用pyUIC工具转化为py文件，可以看到这里的信号发生和接收对应的三条代码，这三条代码中的内容就是我们之前编辑的几个参数。

<img src=".\pyqt.assets\image-20230703142248353.png" alt="image-20230703142248353" style="zoom:80%;" />

* 这里我们需要进行修改，将这三个clicked触发的槽函数show()改为自定义函数runCrawler，saveFile和clearText，将self下的对象centralwidget删去，直接作用于self本身，并在该函数外自主定义这三个函数的内容。

```python
self.RunButton.clicked.connect(self.runCrawler) # type: ignore
self.FOutButton.clicked.connect(self.saveFile) # type: ignore
self.ClearButton.clicked.connect(self.clearText) # type: ignore
```

* 自定义函数的实现如下。其中 `runCrawler` 中，`url=self.lineEdit_url.text()` 表示获取条形文本编辑框 `lineEdit_url`中的内容，`self.textBrowser.append()` 函数可将内容展示在文本浏览框中；`clearText` 中`.clear()`函数可清空内容； `saveFile` 中的内容是可以调出可视化的 Windows 资源浏览器，选择需要保存到的文件夹，通过`filedialog.askdirectory()`实现，若是需要选择文件则是 `filedialog.askopenfilename()` 实现。

```python
# saveFile用
import tkinter as tk
from tkinter import filedialog

def runCrawler(self):
    url = self.lineEdit_url.text()
    keyword = ''
    filename = ''
    print(url)
    try:
        scrap_url(self, url, keyword, filename) # 开始爬虫

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
        root = tk.Tk()
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
```

* 最后附上 `crawler.py` 的全部代码，注：关于icon文件这里，可能自动生成的代码实现会出问题，这里我有所改动

```python
from PyQt5.QtGui import QIcon
MainWindow.setWindowIcon(QIcon("./logo.ico"))
```

crawler.py

```python
# -*- coding: utf-8 --

# Form implementation generated from reading ui file 'crawler.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import requests
from bs4 import BeautifulSoup
import re
import tkinter as tk
from tkinter import filedialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1071, 632)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setWindowIcon(QIcon("./logo.ico"))
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
            root = tk.Tk()
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

    response = requests.get(url, headers=my_headers)
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
        res1 = re.findall(r"<a.*?href=.*?shtml.*?title=(.*?)>", str(ele))
        if res1 != []:
            all_titles.append(res1[0])
            # print("res1=%s"%res1)
            continue
        res2 = re.findall(r"<a.*?href=.*?shtml\">(.*?)</a>", str(ele))
        if 'img ' in str(res2):
            continue
        if 'shtml' in str(res2):
            res2 = re.findall(r".*?shtml\">(.*?)", str(res2))
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
```

* 再给主函数添加代码：

main.py

```python
import sys
from PyQt5 import QtWidgets
import crawler #导入Qt文件

if __name__ == '__main__':
    #获取UIC窗口操作权限
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    #调自定义的界面（即刚转换的.py对象）
    Ui = crawler.Ui_MainWindow() #这里也引用了一次crawler.py文件的名字注意
    Ui.setupUi(MainWindow)
    #显示窗口并释放资源
    MainWindow.show()
    sys.exit(app.exec_())
```

* 运行可看到生成的界面，左上角可以看到我们自己添加的icon图标，点击“开始爬取”即可调用 `runCrawler` 中的 `scrap_url` 函数进行爬取。

<img src=".\pyqt.assets\image-20230703150536932.png" alt="image-20230703150536932" style="zoom:80%;" />

* 点击“导出结果”即可选择文件夹进行导出，

<img src=".\pyqt.assets\image-20230703150914949.png" alt="image-20230703150914949" style="zoom:50%;" />

* 导出完成后会有路径提示。

<img src=".\pyqt.assets\image-20230703151014987.png" alt="image-20230703151014987" style="zoom:80%;" />

* 最后，当代码测试完毕后，我们可以使用 `pyinstaller` 将所有文件打包成一个 exe文件，更加方便传输。这里添加pyinstaller工具

<img src=".\pyqt.assets\image-20230703151812680.png" alt="image-20230703151812680" style="zoom:80%;" />

* 右键main.py选择External tools中的pyinstaller进行打包，可以看到在命令提示窗口显示了我们预设的指令，并成功开始打包文件。

这里直接去main.py目录下在cmd窗口中输入指令同样可以打包（需要有pyinstaller.exe的环境变量）

```
pyinstaller -F -w main.py
```

<img src=".\pyqt.assets\image-20230703151939136.png" alt="image-20230703151939136" style="zoom:80%;" />

注：pyinstaller部分参数的含义如下

```text
-F 表示生成单个可执行文件
-w 表示去掉控制台窗口，这在GUI界面时非常有用。不过如果是命令行程序的话那就把这个选项删除吧！
-i 表示可执行文件的图标
```

* 右键项目文件夹，点击Open in Explorer打开保存路径

<img src=".\pyqt.assets\image-20230703152559538.png" alt="image-20230703152559538" style="zoom:80%;" />

* 找到自动生成的 dist 文件夹，可找到打包好的exe文件。

<img src=".\pyqt.assets\image-20230703152446088.png" alt="image-20230703152446088" style="zoom:80%;" />

* 运行exe文件可发现功能正常，但是左上角的logo没有显示

<img src=".\pyqt.assets\image-20230703152219906.png" alt="image-20230703152219906" style="zoom:80%;" />

* 将logo文件放进来，就可以正常显示了，说明资源文件没有被封装到exe中，需要进行一些其他操作进行处理

<img src=".\pyqt.assets\image-20230703153655338.png" alt="image-20230703153655338" style="zoom:80%;" />

<img src=".\pyqt.assets\image-20230703153734881.png" alt="image-20230703153734881" style="zoom:80%;" />

* 在主函数模块同级目录下创建`resources_rc.qrc`文件和`images`文件夹，`images`文件夹内存放图标文件，`resources_rc.qrc`的内容如下(删掉注释)

```html
<!DOCTYPE RCC><RCC version="1.0">
<!--带上前缀，将qrc生成的图标伪装成images目录下的文件 -->
<qresource prefix="/images">
<!--images/logo.ico为图标位置 -->
<!--qrc生成的图标名称为image.ico，之后主函数调用的就是这个名称 -->
<file alias="image.ico">images/logo.ico</file>
</qresource>
</RCC>
```

* 将`resources_rc.qrc` 转为 `.py`文件

```
pyrcc5 -o resources_rc.py resources_rc.qrc
```

<img src=".\pyqt.assets\image-20230703154935275.png" alt="image-20230703154935275" style="zoom:80%;" />

* 在`crawler.py`中引用生成的图标

```python
import resources_rc
# 此处的:/images/image.ico为.py生成的图标，与之前的存储路径无关
# 可以运行测试，如果显示图标，则调用成功
self.setWindowIcon(QIcon(':/images/image.ico'))
```

* 打包exe时需要带上 -i 参数，表示图标的绝对路径

```
pyinstaller -F -w -i C:\Users\12420\PycharmProjects\pythonProject\images\logo.ico main.py
```

<img src=".\pyqt.assets\image-20230703162336171.png" alt="image-20230703162336171" style="zoom:80%;" />

* 打包前我顺便删了一些不用的包，用什么函数就import什么函数，最后减小了一些体积，并且最后功能实现正常。

<img src=".\pyqt.assets\image-20230703162518976.png" alt="image-20230703162518976" style="zoom:80%;" />
