# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\danie\Documents\Programming Projects\Python\Personal Projects\Bank App\Code\intr.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(462, 590)
        Form.setMinimumSize(QtCore.QSize(419, 548))
        self.menustack = QtWidgets.QStackedWidget(Form)
        self.menustack.setGeometry(QtCore.QRect(0, 0, 461, 591))
        self.menustack.setObjectName("menustack")
        self.Intropg = QtWidgets.QWidget()
        self.Intropg.setObjectName("Intropg")
        self.bckgrnd = QtWidgets.QFrame(self.Intropg)
        self.bckgrnd.setGeometry(QtCore.QRect(20, 20, 419, 548))
        self.bckgrnd.setMinimumSize(QtCore.QSize(419, 548))
        self.bckgrnd.setStyleSheet("background-color: rgb(25, 25, 25);\n"
"border-radius: 21px;")
        self.bckgrnd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bckgrnd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bckgrnd.setObjectName("bckgrnd")
        self.Logincall = QtWidgets.QPushButton(self.bckgrnd)
        self.Logincall.setGeometry(QtCore.QRect(110, 350, 211, 43))
        self.Logincall.setMinimumSize(QtCore.QSize(211, 43))
        font = QtGui.QFont()
        font.setFamily("Inria Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Logincall.setFont(font)
        self.Logincall.setStyleSheet("background-color: rgb(58, 58, 58);\n"
"border-radius: 21px;\n"
"color: rgb(255, 255, 255);")
        self.Logincall.setObjectName("Logincall")
        self.Signupcall = QtWidgets.QPushButton(self.bckgrnd)
        self.Signupcall.setGeometry(QtCore.QRect(110, 420, 211, 43))
        self.Signupcall.setMinimumSize(QtCore.QSize(211, 43))
        font = QtGui.QFont()
        font.setFamily("Inria Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Signupcall.setFont(font)
        self.Signupcall.setStyleSheet("background-color: rgb(58, 58, 58);\n"
"border-radius: 21px;\n"
"color: rgb(255, 255, 255);")
        self.Signupcall.setObjectName("Signupcall")
        self.Exitbtn = QtWidgets.QPushButton(self.bckgrnd)
        self.Exitbtn.setGeometry(QtCore.QRect(360, 20, 31, 31))
        self.Exitbtn.setAutoFillBackground(False)
        self.Exitbtn.setStyleSheet("border-image: url(:/strt/icons8-close-50.png);\n"
"image: url(:/srt/Images/icons8-close-50.png);")
        self.Exitbtn.setText("")
        self.Exitbtn.setObjectName("Exitbtn")
        self.Logo = QtWidgets.QLabel(self.bckgrnd)
        self.Logo.setGeometry(QtCore.QRect(100, 60, 241, 251))
        self.Logo.setAutoFillBackground(False)
        self.Logo.setStyleSheet("image: url(:/strt/circle  mask the logo.png);")
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap(":/srt/Images/circle  mask the logo.png"))
        self.Logo.setScaledContents(True)
        self.Logo.setObjectName("Logo")
        self.menustack.addWidget(self.Intropg)
        self.Loginpg = QtWidgets.QWidget()
        self.Loginpg.setObjectName("Loginpg")
        self.bckgrnd_2 = QtWidgets.QFrame(self.Loginpg)
        self.bckgrnd_2.setGeometry(QtCore.QRect(20, 20, 419, 548))
        self.bckgrnd_2.setMinimumSize(QtCore.QSize(419, 548))
        self.bckgrnd_2.setStyleSheet("background-color: rgb(25, 25, 25);\n"
"border-radius: 21px;")
        self.bckgrnd_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bckgrnd_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bckgrnd_2.setObjectName("bckgrnd_2")
        self.Loginbtn = QtWidgets.QPushButton(self.bckgrnd_2)
        self.Loginbtn.setGeometry(QtCore.QRect(110, 360, 211, 43))
        self.Loginbtn.setMinimumSize(QtCore.QSize(211, 43))
        font = QtGui.QFont()
        font.setFamily("Inria Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Loginbtn.setFont(font)
        self.Loginbtn.setStyleSheet("background-color: rgb(76, 165, 99);\n"
"border-radius: 21px;\n"
"color: rgb(255, 255, 255);")
        self.Loginbtn.setObjectName("Loginbtn")
        self.logExitbtn = QtWidgets.QPushButton(self.bckgrnd_2)
        self.logExitbtn.setGeometry(QtCore.QRect(360, 20, 31, 31))
        self.logExitbtn.setAutoFillBackground(False)
        self.logExitbtn.setStyleSheet("border-image: url(:/strt/icons8-close-50.png);\n"
"image: url(:/srt/Images/icons8-close-50.png);")
        self.logExitbtn.setText("")
        self.logExitbtn.setObjectName("logExitbtn")
        self.Userfield = QtWidgets.QLineEdit(self.bckgrnd_2)
        self.Userfield.setGeometry(QtCore.QRect(70, 160, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Userfield.setFont(font)
        self.Userfield.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-bottom: 2px solid white;\n"
"background-color: rgb(58, 58, 58);")
        self.Userfield.setText("")
        self.Userfield.setObjectName("Userfield")
        self.Backbtn = QtWidgets.QPushButton(self.bckgrnd_2)
        self.Backbtn.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.Backbtn.setAutoFillBackground(False)
        self.Backbtn.setStyleSheet("border-image: url(:/srt/Images/icons8-back-50.png);\n"
"")
        self.Backbtn.setText("")
        self.Backbtn.setObjectName("Backbtn")
        self.Passfield = QtWidgets.QLineEdit(self.bckgrnd_2)
        self.Passfield.setGeometry(QtCore.QRect(70, 230, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Passfield.setFont(font)
        self.Passfield.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-bottom: 2px solid white;\n"
"background-color: rgb(58, 58, 58);")
        self.Passfield.setText("")
        self.Passfield.setObjectName("Passfield")
        self.statusmess = QtWidgets.QLabel(self.bckgrnd_2)
        self.statusmess.setGeometry(QtCore.QRect(70, 300, 291, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.statusmess.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.statusmess.setFont(font)
        self.statusmess.setStyleSheet("color: rgb(255, 0, 0);")
        self.statusmess.setText("")
        self.statusmess.setObjectName("statusmess")
        self.menustack.addWidget(self.Loginpg)
        self.Signuppg = QtWidgets.QWidget()
        self.Signuppg.setObjectName("Signuppg")
        self.bckgrnd_3 = QtWidgets.QFrame(self.Signuppg)
        self.bckgrnd_3.setGeometry(QtCore.QRect(20, 20, 419, 548))
        self.bckgrnd_3.setMinimumSize(QtCore.QSize(419, 548))
        self.bckgrnd_3.setStyleSheet("background-color: rgb(25, 25, 25);\n"
"border-radius: 21px;")
        self.bckgrnd_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bckgrnd_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bckgrnd_3.setObjectName("bckgrnd_3")
        self.signupbtn = QtWidgets.QPushButton(self.bckgrnd_3)
        self.signupbtn.setGeometry(QtCore.QRect(110, 420, 211, 43))
        self.signupbtn.setMinimumSize(QtCore.QSize(211, 43))
        font = QtGui.QFont()
        font.setFamily("Inria Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.signupbtn.setFont(font)
        self.signupbtn.setStyleSheet("background-color: rgb(76, 165, 99);\n"
"border-radius: 21px;\n"
"color: rgb(255, 255, 255);")
        self.signupbtn.setObjectName("signupbtn")
        self.SignExitbtn_2 = QtWidgets.QPushButton(self.bckgrnd_3)
        self.SignExitbtn_2.setGeometry(QtCore.QRect(360, 20, 31, 31))
        self.SignExitbtn_2.setAutoFillBackground(False)
        self.SignExitbtn_2.setStyleSheet("border-image: url(:/strt/icons8-close-50.png);\n"
"image: url(:/srt/Images/icons8-close-50.png);")
        self.SignExitbtn_2.setText("")
        self.SignExitbtn_2.setObjectName("SignExitbtn_2")
        self.Backbtn2 = QtWidgets.QPushButton(self.bckgrnd_3)
        self.Backbtn2.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.Backbtn2.setAutoFillBackground(False)
        self.Backbtn2.setStyleSheet("border-image: url(:/srt/Images/icons8-back-50.png);\n"
"")
        self.Backbtn2.setText("")
        self.Backbtn2.setObjectName("Backbtn2")
        self.usernamefield = QtWidgets.QLineEdit(self.bckgrnd_3)
        self.usernamefield.setGeometry(QtCore.QRect(70, 270, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.usernamefield.setFont(font)
        self.usernamefield.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-bottom: 2px solid white;\n"
"background-color: rgb(58, 58, 58);")
        self.usernamefield.setText("")
        self.usernamefield.setObjectName("usernamefield")
        self.Passfield_2 = QtWidgets.QLineEdit(self.bckgrnd_3)
        self.Passfield_2.setGeometry(QtCore.QRect(70, 330, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Passfield_2.setFont(font)
        self.Passfield_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-bottom: 2px solid white;\n"
"background-color: rgb(58, 58, 58);")
        self.Passfield_2.setText("")
        self.Passfield_2.setObjectName("Passfield_2")
        self.fnamefield = QtWidgets.QLineEdit(self.bckgrnd_3)
        self.fnamefield.setGeometry(QtCore.QRect(70, 90, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.fnamefield.setFont(font)
        self.fnamefield.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-bottom: 2px solid white;\n"
"background-color: rgb(58, 58, 58);")
        self.fnamefield.setText("")
        self.fnamefield.setObjectName("fnamefield")
        self.lnamefield = QtWidgets.QLineEdit(self.bckgrnd_3)
        self.lnamefield.setGeometry(QtCore.QRect(70, 150, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lnamefield.setFont(font)
        self.lnamefield.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-bottom: 2px solid white;\n"
"background-color: rgb(58, 58, 58);")
        self.lnamefield.setText("")
        self.lnamefield.setObjectName("lnamefield")
        self.dobfield = QtWidgets.QDateEdit(self.bckgrnd_3)
        self.dobfield.setGeometry(QtCore.QRect(170, 210, 191, 41))
        self.dobfield.setStyleSheet("background-color: rgb(58, 58, 58);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom: 2px solid white;")
        self.dobfield.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dobfield.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.dobfield.setCalendarPopup(True)
        self.dobfield.setObjectName("dobfield")
        self.doblabel = QtWidgets.QLabel(self.bckgrnd_3)
        self.doblabel.setGeometry(QtCore.QRect(70, 210, 101, 41))
        self.doblabel.setStyleSheet("background-color: rgb(58, 58, 58);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom: 2px solid white;")
        self.doblabel.setObjectName("doblabel")
        self.statmess = QtWidgets.QLabel(self.bckgrnd_3)
        self.statmess.setGeometry(QtCore.QRect(100, 380, 47, 13))
        self.statmess.setObjectName("statmess")
        self.statusmess_2 = QtWidgets.QLabel(self.bckgrnd_3)
        self.statusmess_2.setGeometry(QtCore.QRect(70, 380, 291, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.statusmess_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.statusmess_2.setFont(font)
        self.statusmess_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.statusmess_2.setText("")
        self.statusmess_2.setObjectName("statusmess_2")
        self.dobfield.raise_()
        self.doblabel.raise_()
        self.signupbtn.raise_()
        self.SignExitbtn_2.raise_()
        self.Backbtn2.raise_()
        self.usernamefield.raise_()
        self.Passfield_2.raise_()
        self.fnamefield.raise_()
        self.lnamefield.raise_()
        self.statmess.raise_()
        self.statusmess_2.raise_()
        self.menustack.addWidget(self.Signuppg)

        self.retranslateUi(Form)
        self.menustack.setCurrentIndex(0)
        self.Exitbtn.clicked.connect(Form.close) # type: ignore
        self.logExitbtn.clicked.connect(Form.close) # type: ignore
        self.SignExitbtn_2.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Logincall.setText(_translate("Form", "Log In"))
        self.Signupcall.setText(_translate("Form", "Sign Up"))
        self.Loginbtn.setText(_translate("Form", "Log In"))
        self.Userfield.setPlaceholderText(_translate("Form", "Username"))
        self.Passfield.setPlaceholderText(_translate("Form", "Password"))
        self.signupbtn.setText(_translate("Form", "Sign Up"))
        self.usernamefield.setPlaceholderText(_translate("Form", "Username"))
        self.Passfield_2.setPlaceholderText(_translate("Form", "Password"))
        self.fnamefield.setPlaceholderText(_translate("Form", "Firstname"))
        self.lnamefield.setPlaceholderText(_translate("Form", "Lastname"))
        self.dobfield.setDisplayFormat(_translate("Form", "yyyy-M-d"))
        self.doblabel.setText(_translate("Form", "Date of birth"))
        self.statmess.setText(_translate("Form", "TextLabel"))
import pics_rc
