import sys
#pip install PyQt5  
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QLineEdit, QWidget, QFileDialog, QLabel, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from validate_email import validate_email
# pip install validate_email
import mysql.connector 
# pip install mysql-connector 
# pip install pandas 
from pandas.core.common import flatten
#Email libraries
import smtplib
from email.mime.multipart import MIMEMultipart
#import os
#from PySide2 import *

class RegisterLogin(QMainWindow):
    def __init__(self):
        super(RegisterLogin, self).__init__()
        loadUi("./LoginRegisterUI/RegisterLogin_UI.ui", self)
        self.setWindowTitle("Gen-Services")

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

register_login = RegisterLogin()

widget.addWidget(register_login)    #00

widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")