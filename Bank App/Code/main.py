import random
import sys
from time import sleep
import mysql.connector
from PyQt5.QtWidgets import QWidget, QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QPoint, QDateTime
from intr_ui import Ui_Form
import dashboard_ui

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "bank"
)
myc = mydb.cursor()

class dash(QMainWindow,dashboard_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class Intro(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)        
                           
        flags = Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint) # type: ignore
        self.setAttribute(Qt.WA_TranslucentBackground) # type: ignore
        self.setWindowFlags(flags)
        
        setupbtn =[self.Logincall, self.Signupcall, self.Backbtn, self.Backbtn2]
        for btn in setupbtn:
            btn.clicked.connect(self.call)
        
        self.Loginbtn.clicked.connect(self.login)
        self.signupbtn.clicked.connect(self.signup)
        
        self.dobfield.setMaximumDateTime(QDateTime.currentDateTime())
        
        self.show()
        
    def signup(self):
        fnameval = self.fnamefield.text()
        lnameval = self.lnamefield.text()
        dob = self.dobfield.text()
        ufield = self.usernamefield.text()
        pfield = self.Passfield_2.text()
        inpt = "INSERT INTO accounts (username, fname, lname, accno, password, dob) VALUES ('{}','{}','{}','{}','{}','{}')"
        m = 0

        
        if fnameval == '' or lnameval == '' or ufield == ''or pfield == ''or dob == '':
            self.statusmess_2.setText('Please Fill in all Fields!')            
        elif len(pfield) not in range(5,13):
            self.statusmess_2.setText("Password must be 5-12 characters long")
        elif fnameval != '' and lnameval != '' and ufield != '' and pfield != '' and dob != '':
            myc.execute("SELECT * FROM accounts")
            mycval = myc.fetchall()
            for val in mycval:
                if ufield in val:
                    self.statusmess_2.setText("Username Unavailable")
                else:
                    self.statusmess_2.setText('')
                    while m == 0:
                        acc = random.randrange(300000000, 999999999)
                        print(acc)
                        for val in mycval:
                            if acc not in val:
                                myc.execute(inpt.format(ufield, fnameval, lnameval, acc, pfield, dob))
                                mydb.commit()
                                self.statusmess_2.setText('Sign Up Successful')
                                sleep(2)
                                m = 1
                                koy = 109
                                self.menustack.setCurrentIndex(0)

    def login(self):
        userlog = self.Userfield.text()
        passlog = self.Passfield.text()
        stat = self.statusmess.text()
        fetch = "SELECT * FROM accounts"
        m=1
        
        if userlog == '' or passlog == '':
            self.statusmess.setText('Please Fill in all Fields!')
        else:
            myc.execute(fetch)
            val = myc.fetchall()
            for x in val:
                if userlog == x[1] and passlog == x[5]:
                    self.close()
                    self.window = dash()
                    self.window.show()
                    m = 2
            if m == 1:
                self.statusmess.setText("Invalid Username or Password")
                    
    def call(self):
        x = self.sender()
        if x.text() == 'Log In': # type: ignore
            self.menustack.setCurrentIndex(1)
        if x.text() == 'Sign Up': # type: ignore
            self.menustack.setCurrentIndex(2)
        if x.objectName() == 'Backbtn' or x.objectName() == 'Backbtn2':
            self.menustack.setCurrentIndex(0)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta =QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()        
        
app = QApplication(sys.argv)
dis = Intro()
app.exec()  