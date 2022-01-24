from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QTableWidgetItem
from PySide2.QtCore import Qt
import re
import requests
from threading import Thread
import time





class Stats:

    def __init__(self):
        # 从文件中加载UI定义
        global res
        res = []

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('readpath2.ui')
        # 表格设计
        self.ui.excel.setColumnWidth(0, 110)
        self.ui.excel.setColumnWidth(1, 90)
        self.ui.excel.setColumnWidth(2, 600)
        self.ui.copy2.clicked.connect(self.copy2)
        self.ui.qingchu2.clicked.connect(self.qingchu2)
        # 信号处理
        self.ui.button.clicked.connect(self.handleCalc)
        self.ui.clear.clicked.connect(self.clear)
        self.ui.copy.clicked.connect(self.copy)
        self.ui.geturl.clicked.connect(self.geturl)
        self.ui.replace.clicked.connect(self.repl)
        self.ui.setpack.clicked.connect(self.setpack)
        self.ui.qingchu.clicked.connect(self.qingchu)
        self.ui.excel.clicked.connect(self.copy2)


    def qingchu2(self,res):
        self.ui.excel.clearContents()
        res.clear()

    def copy2(self):

        # num = 1
        # self.ui.excel.insertRow(num)
        # self.ui.excel.setItem(num, 0, QTableWidgetItem('白月黑羽-江老师'))
        # self.ui.excel.setItem(num, 1, QTableWidgetItem('GODV-王老师'))
        # self.ui.excel.setItem(num, 2, QTableWidgetItem('王老师吊打江老师'))
        # num += 1
        # while True:

        row = self.ui.excel.currentRow()
        onse = res[row]
        self.ui.response.clear()
        self.ui.response.appendPlainText(onse)



        # item = QTableWidgetItem()
        # self.ui.excel.setItem(1, 0, QTableWidgetItem('白月黑羽'))
        # self.ui.excel.item(num, 1).setText('GODV-王老师')
        # self.ui.excel.item(num, 2).setText('王老师吊打江老师')

    def qingchu(self):
        self.ui.result.clear()
        res.clear()

    def requests(self):
        pass

    def setpack(self):

        i = 'GET'
        url4 = self.ui.url.toPlainText()
        url5 = url4.split('\n')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
        }

        def threadFunc():
            num = len(res)
            print(num)
            if i == 'POST':
                data = self.ui.path.toPlainText()
                for url6 in url5:
                    try:
                        requests.packages.urllib3.disable_warnings()
                        response = requests.post(url=url6, headers=headers, data=data, verify=False,timeout=3)
                        txt = response.text
                        res.append(txt)
                        length = str(len(txt))
                        code = str(response.status_code)

                        self.ui.result.appendPlainText('#' + url6 + '#')
                        self.ui.result.appendPlainText(txt)
                        self.ui.result.appendPlainText('#' * 29)
                        self.ui.result.appendPlainText('\n')

                        self.ui.excel.insertRow(num)
                        self.ui.excel.setItem(num, 2, QTableWidgetItem(url6))

                        self.ui.excel.setItem(num, 1, QTableWidgetItem(length))

                        item = QTableWidgetItem()
                        item.setText(code)
                        item.setTextAlignment(Qt.AlignCenter)
                        self.ui.excel.setItem(num, 0, item)

                        # self.ui.excel.setItem(num, 2, QTableWidgetItem(url6))

                        # item2 = QTableWidgetItem()
                        # item2.setText(length)
                        # item2.setTextAlignment(Qt.AlignCenter)
                        # self.ui.excel.setItem(num, 1, item2)

                        self.ui.result.appendPlainText('#' + url6 + '#')
                        self.ui.result.appendPlainText(txt)
                        self.ui.result.appendPlainText('#' * 29)
                        self.ui.result.appendPlainText('\n')
                        num += 1

                    except Exception as e:
                        self.ui.result.appendPlainText(e)
            else:
                for url6 in url5:
                    try:
                        requests.packages.urllib3.disable_warnings()
                        response = requests.get(url=url6, headers=headers, verify=False,timeout=3)
                        txt = response.text
                        res.append(txt)
                        length = str(len(txt))
                        code = str(response.status_code)

                        self.ui.result.appendPlainText('#' + url6 + '#')
                        self.ui.result.appendPlainText(txt)
                        self.ui.result.appendPlainText('#' * 29)
                        self.ui.result.appendPlainText('\n')

                        self.ui.excel.setItem(num, 2, QTableWidgetItem(url6))
                        self.ui.excel.setItem(num, 1, QTableWidgetItem(length))

                        item = QTableWidgetItem()
                        item.setText(code)
                        item.setTextAlignment(Qt.AlignCenter)
                        self.ui.excel.setItem(num, 0, item)

                        num += 1
                    except Exception as e:
                        pass

        thread = Thread(target=threadFunc)
        thread.start()






    def print_value(self, i):

        return i

    def repl(self):
        path1 = self.ui.url.toPlainText()
        path2 = path1.split('\n')
        self.ui.url.clear()
        # print(path1)
        host = self.ui.host.text()
        # print(host)
        url3 = []
        for path0 in path2:
            # url = 'http://'+host + '/' +path0
            # urls0 = url.replace('./','/').replace('//','/').replace('http:/','http://').replace('https:/','https://')
            url = 'https://' + host + '/' + path0
            urls1 = url.replace('./', '/').replace('//', '/').replace('http:/', 'http://').replace('https:/',
                                                                                                   'https://')
            self.ui.url.appendPlainText(urls1)
            url3.append(urls1)
        return url3

    def geturl(self):
        urls = self.ui.path.toPlainText()
        self.ui.url.appendPlainText(urls)

    def copy(self):
        self.ui.path.copy()

    def clear(self):
        self.ui.js.clear()

    def handleCalc(self):
        # retxt = ''''([^=<\+):;,'"]*/[^;(']*\?*[^,(:'\s"])'|"([^:=<\+),\s"]*/[^(;"]*[^,=(:\s"])"'''
        info = self.ui.js.toPlainText()
        reruls = open('re.txt', mode='r').read()
        pattern = re.compile(reruls)
        text = pattern.findall(info)
        text2 = []
        text3 = []
        for a in text:
            if a not in text2:
                text2.append(a)
        for one in text2:
            opath = one[1]
            tpath = one[0]
            if opath:
                self.ui.path.appendPlainText(opath)
                text3.append(opath)
            if tpath:
                self.ui.path.appendPlainText(tpath)
                text3.append(tpath)
        return text3

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
