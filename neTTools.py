import pprint
import os
import sys
import sublist3r
import requests

from bs4 import BeautifulSoup
from googlesearch import search
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from PyQt5.QtGui import QIntValidator
from echofunc import *


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login Form')
        self.resize(500, 120)

        layout = QGridLayout()

        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    def check_password(self):
        msg = QMessageBox()

        if self.lineEdit_username.text() == 'admin' and self.lineEdit_password.text() == 'admin':
            msg.setText('Login Success')
            msg.exec_()
            MainWindow.show()
            login_form.close()
        else:
            msg.setText('Incorrect Password')
            msg.exec_()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(25, 115, 750, 450))
        self.tabWidget.setObjectName("tabWidget")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(20, 30, 85, 20))
        self.label_5.setObjectName("label_5")
        self.lineTextEdit_4 = QtWidgets.QLineEdit(self.tab_3)
        self.lineTextEdit_4.setGeometry(QtCore.QRect(125, 20, 150, 35))
        self.lineTextEdit_4.setObjectName("lineTextEdit_4") 
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 135, 700, 250))
        self.textEdit_3.setObjectName("textEdit_3")     
        self.textEdit_3.setReadOnly(True)
        self.pushButton3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton3.setGeometry(QtCore.QRect(285, 20, 150, 85))
        self.pushButton3.setObjectName("pushButton_3")
        self.pushButton3.clicked.connect(self.getdomain)
        self.tabWidget.addTab(self.tab_3, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 85, 20))
        self.label_4.setObjectName("label_4")
        self.lineTextEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineTextEdit_3.setGeometry(QtCore.QRect(125, 20, 150, 35))
        self.lineTextEdit_3.setObjectName("lineTextEdit_3") 
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 135, 700, 250))
        self.textEdit_2.setObjectName("textEdit_2")     
        self.textEdit_2.setReadOnly(True)
        self.pushButton2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton2.setGeometry(QtCore.QRect(285, 20, 150, 85))
        self.pushButton2.setObjectName("pushButton_2")
        self.pushButton2.clicked.connect(self.scansubdomain)
        self.tabWidget.addTab(self.tab_2, "")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 35, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 35, 15))
        self.label_3.setObjectName("label_3")
        self.lineTextEdit = QtWidgets.QLineEdit(self.tab)
        self.lineTextEdit.setGeometry(QtCore.QRect(85, 20, 150, 35))
        self.lineTextEdit.setObjectName("lineTextEdit")
        self.lineTextEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineTextEdit_2.setGeometry(QtCore.QRect(85, 75, 150, 35))
        self.lineTextEdit_2.setObjectName("lineTextEdit_2")
        self.lineTextEdit_2.setPlaceholderText('0')
        self.lineTextEdit_2.setValidator(QIntValidator(1, 999999)) 
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(10, 135, 700, 250))
        self.textEdit.setObjectName("textEdit")     
        self.textEdit.setReadOnly(True)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(275, 20, 150, 85))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.runechotest)
        self.tabWidget.addTab(self.tab, "") 

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_4.setGeometry(QtCore.QRect(10, 10, 710, 400))
        self.textEdit_4.setObjectName("textEdit_3")     
        self.textEdit_4.setReadOnly(True)
        self.tabWidget.addTab(self.tab_4, "")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 10, 350, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 506, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pbar = QtWidgets.QProgressBar(MainWindow)
        self.pbar.setGeometry(QtCore.QRect(30, 580, 765, 35))
        self.pbar.setObjectName("progressbar")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def get_pathfile(self, filename):
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        ret_path = application_path + "\\" + filename
        return ret_path

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "neTTools v 0.1"))
        self.label_2.setText(_translate("MainWindow", "IP"))
        self.label_3.setText(_translate("MainWindow", "Port"))
        self.label_4.setText(_translate("MainWindow", "File domain"))
        self.label_5.setText(_translate("MainWindow", "File domain"))

        self.textEdit_4.append("neTTools" + '\n' + "v 0.1" + '\n') 
        self.textEdit_4.append("This bundling GUI apps goal is compiled several python code & tools for red team purpose")
        self.textEdit_4.append('\n' + "Current tools : " + '\n' + "1. sublist3r by aboul3la [https://github.com/aboul3la/Sublist3r]")
        self.textEdit_4.append('\n' + "2. subbrute by TheRook [https://github.com/TheRook/subbrute]")
        self.textEdit_4.append('\n' + "3. get domain")

        self.pushButton.setText(_translate("MainWindow", "SEND MESSAGE"))
        self.pushButton2.setText(_translate("MainWindow", "SCAN SUBDOMAIN"))
        self.pushButton3.setText(_translate("MainWindow", "GET DOMAIN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "ECHO Test"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Scan Subdomain"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Get Domain"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Credit"))
        self.label.setText(_translate("MainWindow", "neTTools"))

    def runechotest(self):
        # Step 2: Send 0800 message and receive response
        response_0800 = send_0800_message(self.lineTextEdit.text(),int(float(self.lineTextEdit_2.text())))
        
        # Step 3: Parse header and trailer
        header, trailer = parse_header_trailer(response_0800)

        # Step 4: Resend message with correct header and trailer
        response_0810 = resend_message(header, trailer)

        # Step 5: Confirm response, ignoring bit 39
        confirmed_response = confirm_response(response_0810)

        responseTextEdit = 'RESP 0800 = ' + response_0800 + '\n' 
        + 'HEADER = ' + header + '\n' + 'TRAILER = ' + trailer + '\n' 
        + 'RESP 0810 = ' + response_0810 + '\n' + 'RESPON = ' + confirmed_response

        self.textEdit.setText(responseTextEdit)

    def getdomain(self):
        file1 = open(self.get_pathfile(self.lineTextEdit_4.text()), 'r', encoding="utf8")
        Lines = file1.readlines()

        filename = self.get_pathfile("output_scan\\result_getdomain.txt")

        count = 0
        
        for count, line in enumerate(file1):
            pass

        count += 1
        prog_bar = int(101 / count)
        pbarresult = 0
        self.pbar.setValue(pbarresult)

        for line in Lines:
            query = line.strip()

            with open(filename, 'at') as f:
                for j in search(query, num=1, stop=1, pause=5):
                    res_header = j.replace("https://",'')
                    res_header = res_header.replace("http://",'')
                    print(res_header)
                    head, sep, tail = res_header.partition('/')
                    f.write(head + '\n')
                    self.textEdit_3.append(line.strip() + " DOMAIN = " + head)
                
            pbarresult += prog_bar
            self.pbar.setValue(pbarresult)

                
        self.textEdit_3.append("Get Domain Completed !")
        self.pbar.setValue(100)

    def scansubdomain(self):
        file1 = open(self.get_pathfile(self.lineTextEdit_3.text()), 'r',encoding="utf8")
        Lines = file1.readlines()

        count = 0
        
        for count, line in enumerate(file1):
            pass

        count += 1
        prog_bar = 101 / (count * 3 * 10)
        pbarresult = 0
        for line in Lines:
            nameFile = "output_scan\\resultsubdomain_rdp_"+line.strip()+".txt"
            self.pbar.setValue(pbarresult)
            subdomains = sublist3r.main(line.strip(), 25, self.get_pathfile(nameFile), ports="3389" , silent=False, verbose= True, enable_bruteforce= False, engines=None)
            self.textEdit_2.append("Process RDP " + nameFile + " DONE")
            pbarresult += prog_bar 
            nameFile = "output_scan\\resultsubdomain_ssh_"+line.strip()+".txt"
            self.pbar.setValue(pbarresult)
            subdomains = sublist3r.main(line.strip(), 25, self.get_pathfile(nameFile), ports="22" , silent=False, verbose= True, enable_bruteforce= False, engines=None)
            self.textEdit_2.append("Process SSH " + nameFile + " DONE")
            pbarresult += prog_bar
            nameFile = "output_scan\\resultsubdomain_vnc_"+line.strip()+".txt"
            self.pbar.setValue(pbarresult)
            subdomains = sublist3r.main(line.strip(), 25, self.get_pathfile(nameFile), ports="5902" , silent=False, verbose= True, enable_bruteforce= False, engines=None)
            self.textEdit_2.append("Process VNC " + nameFile + " DONE")
            pbarresult += prog_bar 
                        
        self.textEdit_2.append("Scan subdomain Completed !")
        self.pbar.setValue(100)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    login_form = LoginForm()
    login_form.show()
    sys.exit(app.exec_())
