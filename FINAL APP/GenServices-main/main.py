#!/usr/bin/python
#
#     ____            ____                  _               
#   / ___| ___ _ __ / ___|  ___ _ ____   _(_) ___ ___  ___ 
#  | |  _ / _ \ '_ \\___ \ / _ \ '__\ \ / / |/ __/ _ \/ __|
#  | |_| |  __/ | | |___) |  __/ |   \ V /| | (_|  __/\__ \
#  \____|\___|_| |_|____/ \___|_|    \_/ |_|\___\___||___/
#                                                        

# ---------------------------------------------------Import statements-------------------------------------------------- #
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

# ---------------------------------------------------Variables and misc---------------------------------------------------- #

global loginpage_details
loginpage_details = []
global lineEdit_username
lineEdit_username = ""
global in_username
in_username = ""
global lineEdit_email
lineEdit_email = ""
global lineEdit_phnumber
lineEdit_phnumber = ""
global lineEdit_password
lineEdit_password = ""
global lineEdit_repeatpassword
lineEdit_repeatpassword = ""

global db

try:
    db = mysql.connector.connect(host='localhost', user = 'root', passwd = 'mysql', database = 'GenServices')
    print("Successfully Connected To Local SQL Server") 

except: print("Error Connecting to SQL Server")

if (db) :
    print(r'''
 ____   ___  _        ____                            _           _
/ ___| / _ \| |      / ___|___  _ __  _ __   ___  ___| |_ ___  __| |
\___ \| | | | |     | |   / _ \| '_ \| '_ \ / _ \/ __| __/ _ \/ _` |
 ___) | |_| | |___  | |__| (_) | | | | | | |  __/ (__| ||  __/ (_| |
|____/ \__\_\_____|  \____\___/|_| |_|_| |_|\___|\___|\__\___|\__,_|
''')

else :
    print(r'''
 ____   ___  _       __  __                        _
/ ___| / _ \| |     |  \/  | ___  ___ ___  ___  __| |  _   _ _ __
\___ \| | | | |     | |\/| |/ _ \/ __/ __|/ _ \/ _` | | | | | '_ \
 ___) | |_| | |___  | |  | |  __/\__ \__ \  __/ (_| | | |_| | |_) |
|____/ \__\_\_____| |_|  |_|\___||___/___/\___|\__,_|  \__,_| .__/
                                                            |_|''')




try:
    global server
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login('system.genservices@gmail.com', 'genservicespass')
except:
    print('Something went wrong with mail server')



global curs 
curs  = db.cursor()

def getLoginDetails():
    global loginpage_details
    curs.execute('select username, password from login_details')
    loginpage_details = curs.fetchall()
    loginpage_details = list(flatten(loginpage_details))

getLoginDetails()

# ----------------------------------------------------class declaration---------------------------------------------------- #

class loginregister(QMainWindow):
    def __init__(self):
        super(loginregister, self).__init__()
        loadUi("loginregister.ui", self)
        self.setWindowTitle("GenServices")
        self.login_button.clicked.connect(self.gotologin_page)
        self.register_button.clicked.connect(self.gotoregister_page)
        self.registerface_button.clicked.connect(self.gotofcregister_page)
        #self.iconName = "logo.jpg"
    def gotologin_page(self):
        widget.setCurrentIndex(1)

    def gotoregister_page(self):
        widget.setCurrentIndex(2)

    def gotofcregister_page(self):
        widget.setCurrentIndex(3)

# ------------------------------------------------------login_page--------------------------------------------------------- #

class login_page(QMainWindow):
    def __init__(self):
        super(login_page, self).__init__()
        loadUi("login_page.ui", self)
        self.pushButton_back.clicked.connect(self.back_button_pressed)
        self.pushbutton_login.clicked.connect(self.login_button_pressed)
        self.password_view.clicked.connect(self.pass_view_clicked)

    def pass_view_clicked(self):
        if self.password_view.isChecked():
            self.lineEdit_password.setEchoMode(QLineEdit.Normal)
        else:
            self.lineEdit_password.setEchoMode(QLineEdit.Password)

    def back_button_pressed(self):
        widget.setCurrentIndex(0)

    def login_button_pressed(self):
        getLoginDetails()
        if self.lineEdit_username.text() == "" or self.lineEdit_password.text() == "":
            print("empty")

            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.setWindowTitle('Empty Fields')
            error_dialog.showMessage("Please fill all the fields")
        else:
            if self.lineEdit_username.text() in loginpage_details:
                if self.lineEdit_password.text() == loginpage_details[loginpage_details.index(self.lineEdit_username.text()) + 1]:
                    login_page.logged_in_username = self.lineEdit_username.text()
                    global in_username
                    in_username = login_page.logged_in_username
                    login_page.logged_in_password = self.lineEdit_password.text()
                    self.lineEdit_username.setText("")
                    self.lineEdit_password.setText("")
                    error_dialog = QtWidgets.QErrorMessage(self)
                    error_dialog.setWindowTitle('Welcome')
                    error_dialog.showMessage(
                        f"Welcome back {login_page.logged_in_username}!")
                    widget.setCurrentIndex(4)
                else:
                    error_dialog = QtWidgets.QErrorMessage(self)
                    error_dialog.setWindowTitle('Password')
                    error_dialog.showMessage(
                        'Incorrect password, please try again')
                    self.lineEdit_password.setText("")
            else:
                error_dialog = QtWidgets.QErrorMessage(self)
                error_dialog.setWindowTitle('Account')
                error_dialog.showMessage('Please create an account')
                self.lineEdit_username.setText("")
                self.lineEdit_password.setText("")
                widget.setCurrentIndex(2)

# --------------------------------------------------------register_page---------------------------------------------------- #

class register_page(QMainWindow):
    def __init__(self):
        super(register_page, self).__init__()
        loadUi("registerpage.ui", self)
        self.pushButton_back.clicked.connect(self.backbutton_clicked)
        self.pushButton_register.clicked.connect(self.registerbutton_clicked)
        self.sp_view.clicked.connect(self.sp_view_clicked)
        self.cp_view.clicked.connect(self.cp_view_clicked)

    def sp_view_clicked(self):
        if self.sp_view.isChecked():
            self.lineEdit_password.setEchoMode(QLineEdit.Normal)
        else:
            self.lineEdit_password.setEchoMode(QLineEdit.Password)

    def cp_view_clicked(self):
        if self.cp_view.isChecked():
            self.lineEdit_repeatpassword.setEchoMode(QLineEdit.Normal)
        else:
            self.lineEdit_repeatpassword.setEchoMode(QLineEdit.Password)

    def backbutton_clicked(self):
        widget.setCurrentIndex(0)

    def registerbutton_clicked(self):

        if self.lineEdit_username.text() == "" or self.lineEdit_email.text() == "" or self.lineEdit_phnumber.text() == "" or self.lineEdit_password.text() == "" or self.lineEdit_repeatpassword.text() == "":
            print("empty")
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.setWindowTitle('Empty Fields')
            error_dialog.showMessage("Please fill all the fields")
        elif len(self.lineEdit_phnumber.text()) != 10:
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.setWindowTitle('Phone Number')
            error_dialog.showMessage('Please enter a valid phone number')
            self.lineEdit_phnumber.setText("")

        elif self.lineEdit_password.text() != self.lineEdit_repeatpassword.text():
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.setWindowTitle('Password')
            error_dialog.showMessage('Passwords are not matching, please try again.')
            self.lineEdit_password.setText("")
            self.lineEdit_repeatpassword.setText("")

        elif self.lineEdit_password.text() == self.lineEdit_repeatpassword.text():
            if validate_email(self.lineEdit_email.text()):
                if self.lineEdit_username.text() not in loginpage_details:

                    curs.execute(f"insert into login_details values('{self.lineEdit_username.text()}', '{self.lineEdit_password.text()}', '{self.lineEdit_email.text()}', '{self.lineEdit_phnumber.text()}')")  
                    db.commit()
                    getLoginDetails()
                    self.lineEdit_username.setText("")
                    self.lineEdit_email.setText("")
                    self.lineEdit_phnumber.setText("")
                    self.lineEdit_password.setText("")
                    self.lineEdit_repeatpassword.setText("")
                    error_dialog = QtWidgets.QErrorMessage(self)
                    error_dialog.setWindowTitle('Thank you')
                    error_dialog.showMessage('Creation of account is successful! Please login with the same credentials')
                    widget.setCurrentIndex(1)
                else:
                    error_dialog = QtWidgets.QErrorMessage(self)
                    error_dialog.setWindowTitle('Account')
                    error_dialog.showMessage('An account with these credentials is already registered, please try logging in.')
                    widget.setCurrentIndex(1)

            else:
                error_dialog = QtWidgets.QErrorMessage(self)
                error_dialog.setWindowTitle('Email')
                error_dialog.showMessage('Please enter a valid email ID')
                self.lineEdit_email.setText("")

# --------------------------------------------------facebook_register_page------------------------------------------------- #

class fcbk_register_page(QMainWindow):
    def __init__(self):
        super(fcbk_register_page, self).__init__()
        loadUi("fcbk_registerpage.ui", self)
        self.pushButton_back.clicked.connect(self.backbutton_clicked)
        self.pushButton_register.clicked.connect(self.registerbutton_clicked)
        self.sp_view.clicked.connect(self.sp_view_clicked)
        self.cp_view.clicked.connect(self.cp_view_clicked)

    def sp_view_clicked(self):
        if self.sp_view.isChecked():
            self.lineEdit_password.setEchoMode(QLineEdit.Normal)
        else:
            self.lineEdit_password.setEchoMode(QLineEdit.Password)

    def cp_view_clicked(self):
        if self.cp_view.isChecked():
            self.lineEdit_repeatpassword.setEchoMode(QLineEdit.Normal)
        else:
            self.lineEdit_repeatpassword.setEchoMode(QLineEdit.Password)

    def backbutton_clicked(self):
        widget.setCurrentIndex(0)

    def registerbutton_clicked(self):

        if self.lineEdit_username.text() == "" or self.lineEdit_fcemail.text() == "" or self.lineEdit_phnumber.text() == "" or self.lineEdit_password.text() == "" or self.lineEdit_repeatpassword.text() == "":
            print("empty")
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.setWindowTitle('Empty Fields')
            error_dialog.showMessage("Please fill all the fields")
        elif len(self.lineEdit_phnumber.text()) != 10:
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.setWindowTitle('Phone Number')
            error_dialog.showMessage('Please enter a valid phone number')
            self.lineEdit_phnumber.setText("")

        elif self.lineEdit_password.text() != self.lineEdit_repeatpassword.text():
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.setWindowTitle('Password')
            error_dialog.showMessage('Passwords are not matching, please try again.')
            self.lineEdit_password.setText("")
            self.lineEdit_repeatpassword.setText("")

        elif self.lineEdit_password.text() == self.lineEdit_repeatpassword.text():
            if self.lineEdit_username.text() not in loginpage_details:
                curs.execute(f"insert into login_details values('{self.lineEdit_username.text()}', '{self.lineEdit_password.text()}', '{self.lineEdit_fcemail.text()}', '{self.lineEdit_phnumber.text()}')")  
                db.commit()
                getLoginDetails()  
                self.lineEdit_password.setText("")
                self.lineEdit_repeatpassword.setText("")
                error_dialog = QtWidgets.QErrorMessage(self)
                error_dialog.setWindowTitle('Thank you')
                error_dialog.showMessage('Creation of account is successful! Please login with the same credentials')
                widget.setCurrentIndex(1)
            else:
                error_dialog = QtWidgets.QErrorMessage(self)
                error_dialog.setWindowTitle('Account')
                error_dialog.showMessage('An account with these credentials is already registered, please try logging in.')
                widget.setCurrentIndex(1)

# ---------------------------------------------------------home_page------------------------------------------------------- #

class home_page(QMainWindow):
    def __init__(self) -> None :
        super(home_page, self).__init__()
        loadUi("home.ui", self)
        #menubar.self.menubar()
        #menubar.setNativeMenuBar(False)
        self.pushButton_logout.clicked.connect(self.are_you_sure)
        self.pushButton_bookings.clicked.connect(self.gotobookings)

        self.electrical_button.clicked.connect(self.gotoelectricals)
        self.computerserv_button.clicked.connect(self.gotocomputerserv)
        self.mechanic_button.clicked.connect(self.gotomechanic)
        self.plumber_button.clicked.connect(self.gotoplumber)
        self.laundryserv_button.clicked.connect(self.gotolaundryserv)
        self.homedesign_button.clicked.connect(self.gotohomedesign)
        self.yardwork_button.clicked.connect(self.gotoyardwork)
        self.cleaning_button.clicked.connect(self.gotocleaning)

    def are_you_sure(self):
        msg = QMessageBox()
        msg.setWindowTitle("Logout")
        msg.setText("Are you sure?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        msg.buttonClicked.connect(self.popup_button)
        x = msg.exec_()

    def popup_button(self, button):
        button_pressed = button.text()

        if button_pressed == '&Yes':
            widget.setCurrentIndex(0)

        else:
            pass

    def gotobookings(self):
        widget.setCurrentIndex(5)
    
    def gotoelectricals(self):
        widget.setCurrentIndex(6)

    def gotocomputerserv(self):
        widget.setCurrentIndex(9)

    def gotomechanic(self):
        widget.setCurrentIndex(7)

    def gotoplumber(self):
        widget.setCurrentIndex(11)

    def gotolaundryserv(self):
        widget.setCurrentIndex(12)

    def gotohomedesign(self):
        widget.setCurrentIndex(13)

    def gotoyardwork(self):
        widget.setCurrentIndex(15)

    def gotocleaning(self):
        widget.setCurrentIndex(14)

# -------------------------------------------------------bookings_page----------------------------------------------------- #

class bookings_page(QMainWindow):
    def __init__(self) -> None :
        super(bookings_page, self).__init__()
        loadUi("booking_page.ui", self)
        self.pushButton_back.clicked.connect(self.backbutton_clicked)

    def backbutton_clicked(self):
        widget.setCurrentIndex(4) 

# -----------------------------------------------------electricals_page---------------------------------------------------- #

class electricals_page(QMainWindow):
    def __init__(self) -> None :
        super(electricals_page, self).__init__()
        loadUi("electrical_page.ui", self)
        self.pushButton_back.clicked.connect(self.backbutton_clicked)

        self.pushButton_switch.clicked.connect(self.switchbutton_clicked)
        self.pushButton_fan.clicked.connect(self.fanbutton_clicked)
        self.pushButton_heater.clicked.connect(self.heaterbutton_clicked)
        self.pushButton_light.clicked.connect(self.lightbutton_clicked)
        self.pushButton_chandeller.clicked.connect(self.chandellerbutton_clicked)
        self.pushButton_mcb.clicked.connect(self.mcbbutton_clicked)
        self.pushButton_inverter.clicked.connect(self.inverterbutton_clicked)
        self.pushButton_appliance.clicked.connect(self.appliancebutton_clicked)
        self.pushButton_aircooler.clicked.connect(self.aircoolerbutton_clicked)
        self.pushButton_wiring.clicked.connect(self.wiringbutton_clicked)
        self.pushButton_doorbell.clicked.connect(self.doorbellbutton_clicked)
        self.pushButton_drill.clicked.connect(self.drillbutton_clicked)

    def backbutton_clicked(self):
        widget.setCurrentIndex(4)

    def switchbutton_clicked(self):
        widget.setCurrentIndex(8)
    
    def fanbutton_clicked(self):
        widget.setCurrentIndex(8)

    def heaterbutton_clicked(self):
        widget.setCurrentIndex(8)

    def lightbutton_clicked(self):
        widget.setCurrentIndex(8)

    def chandellerbutton_clicked(self):
        widget.setCurrentIndex(8)

    def mcbbutton_clicked(self):
        widget.setCurrentIndex(8)

    def inverterbutton_clicked(self):
        widget.setCurrentIndex(8)

    def appliancebutton_clicked(self):
        widget.setCurrentIndex(8)

    def aircoolerbutton_clicked(self):
        widget.setCurrentIndex(8)

    def wiringbutton_clicked(self):
        widget.setCurrentIndex(8)

    def doorbellbutton_clicked(self):
        widget.setCurrentIndex(8)

    def drillbutton_clicked(self):
        widget.setCurrentIndex(8)

# ------------------------------------------------------mechanicals_page--------------------------------------------------- #

class mechanicals_page(QMainWindow):
    def __init__(self) -> None :
        super(mechanicals_page, self).__init__()
        loadUi("mechanical_page.ui", self)
        self.pushButton_back.clicked.connect(self.backbutton_clicked)

        self.pushButton_fuelcars.clicked.connect(self.fuelcarbutton_clicked)
        self.pushButton_fuelbikes.clicked.connect(self.fuelbikebutton_clicked)
        self.pushButton_scooters.clicked.connect(self.fuelscooterbutton_clicked)
        self.pushButton_elecars.clicked.connect(self.elecarbutton_clicked)
        self.pushButton_elebikes.clicked.connect(self.elebikebutton_clicked)
        self.pushButton_elescooters.clicked.connect(self.elescooterbutton_clicked)
        self.pushButton_bulldozers.clicked.connect(self.bulldozerbutton_clicked)
        self.pushButton_autos.clicked.connect(self.autobutton_clicked)
        self.pushButton_vans.clicked.connect(self.vanbutton_clicked)
        self.pushButton_buses.clicked.connect(self.busbutton_clicked)
        self.pushButton_tractors.clicked.connect(self.tractorbutton_clicked)
        self.pushButton_cycles.clicked.connect(self.cyclebutton_clicked)

    def backbutton_clicked(self):
        widget.setCurrentIndex(4)

    def fuelcarbutton_clicked(self):
        widget.setCurrentIndex(10)
    
    def fuelbikebutton_clicked(self):
        widget.setCurrentIndex(10)

    def fuelscooterbutton_clicked(self):
        widget.setCurrentIndex(10)

    def elecarbutton_clicked(self):
        widget.setCurrentIndex(10)

    def elebikebutton_clicked(self):
        widget.setCurrentIndex(10)

    def elescooterbutton_clicked(self):
        widget.setCurrentIndex(10)

    def bulldozerbutton_clicked(self):
        widget.setCurrentIndex(10)

    def autobutton_clicked(self):
        widget.setCurrentIndex(10)

    def vanbutton_clicked(self):
        widget.setCurrentIndex(10)

    def busbutton_clicked(self):
        widget.setCurrentIndex(10)

    def tractorbutton_clicked(self):
        widget.setCurrentIndex(10)

    def cyclebutton_clicked(self):
        widget.setCurrentIndex(10)

# ------------------------------------------------choose_need_electrical_page---------------------------------------------- #

class choose_need_electrical(QMainWindow):
    def __init__(self) -> None :
        super(choose_need_electrical, self).__init__()
        loadUi("choose_need_electricals.ui", self)
        self.pushButton_back.clicked.connect(self.backbutton_clicked)

        self.pushButton_installation.clicked.connect(self.installbutton_clicked)
        self.pushButton_repair.clicked.connect(self.repairbutton_clicked)
        self.pushButton_reinstallation.clicked.connect(self.reinstallbutton_clicked)

    def backbutton_clicked(self):
        widget.setCurrentIndex(4)

    def installbutton_clicked(self):
        widget.setCurrentIndex(15)

    def repairbutton_clicked(self):
        widget.setCurrentIndex(15)

    def reinstallbutton_clicked(self):
        widget.setCurrentIndex(15)

# ----------------------------------------------choose_need_computerservices_page------------------------------------------ #

class choose_need_computer(QMainWindow):
    def __init__(self) -> None :
        super(choose_need_computer, self).__init__()
        loadUi("choose_need_comp.ui", self)
        self.pushButton_back.clicked.connect(self.backbutton_clicked)

        self.pushButton_installparts.clicked.connect(self.installpartbutton_clicked)
        self.pushButton_repaircomp.clicked.connect(self.repaircompbutton_clicked)
        self.pushButton_buildcomp.clicked.connect(self.buildcompbutton_clicked)

    def backbutton_clicked(self):
        widget.setCurrentIndex(4)

    def installpartbutton_clicked(self):
        widget.setCurrentIndex(15)

    def repaircompbutton_clicked(self):
        widget.setCurrentIndex(15)

    def buildcompbutton_clicked(self):
        widget.setCurrentIndex(15)

# -------------------------------------------------choose_need_mechanical_page--------------------------------------------- #

class choose_need_mechanical(QMainWindow):
    def __init__(self) -> None :
        super(choose_need_mechanical, self).__init__()
        loadUi("choose_need_mech.ui", self)
        self.pushButton_back.clicked.connect(self.backbutton_clicked)

        self.pushButton_maintenance.clicked.connect(self.maintenancebutton_clicked)
        self.pushButton_repair.clicked.connect(self.repairbutton_clicked)
        self.pushButton_reinstallation.clicked.connect(self.reinstallbutton_clicked)

    def backbutton_clicked(self):
        widget.setCurrentIndex(4)

    def maintenancebutton_clicked(self):
        widget.setCurrentIndex(15)

    def repairbutton_clicked(self):
        widget.setCurrentIndex(15)

    def reinstallbutton_clicked(self):
        widget.setCurrentIndex(15)

# --------------------------------------------------choose_need_plumbing_page---------------------------------------------- #

class choose_need_plumbing(QMainWindow):
    def __init__(self) -> None :
        super(choose_need_plumbing, self).__init__()
        loadUi("choose_need_plumbing.ui", self)
        self.pushButton_back.clicked.connect(self.backbutton_clicked)

        self.pushButton_fix.clicked.connect(self.fixbutton_clicked)
        self.pushButton_build.clicked.connect(self.buildbutton_clicked)
        self.pushButton_install_sparewater.clicked.connect(self.install_sparebutton_clicked)

    def backbutton_clicked(self):
        widget.setCurrentIndex(4)

    def fixbutton_clicked(self):
        widget.setCurrentIndex(15)

    def buildbutton_clicked(self):
        widget.setCurrentIndex(15)

    def install_sparebutton_clicked(self):
        widget.setCurrentIndex(15)

# --------------------------------------------------choose_need_laundry_page----------------------------------------------- #

class choose_need_laundry(QMainWindow):
    def __init__(self) -> None :
        super(choose_need_laundry, self).__init__()
        loadUi("choose_need_laundry.ui", self)
        self.pushButton_back.clicked.connect(self.backbutton_clicked)

        self.pushButton_whitecloth.clicked.connect(self.whiteclothbutton_clicked)
        self.pushButton_darkcloth.clicked.connect(self.darkclothbutton_clicked)
        self.pushButton_towel.clicked.connect(self.towelbutton_clicked)
        self.pushButton_sarees.clicked.connect(self.sareesbutton_clicked)

    def backbutton_clicked(self):
        widget.setCurrentIndex(4)

    def whiteclothbutton_clicked(self):
        widget.setCurrentIndex(15)

    def darkclothbutton_clicked(self):
        widget.setCurrentIndex(15)

    def towelbutton_clicked(self):
        widget.setCurrentIndex(15)

    def sareesbutton_clicked(self):
        widget.setCurrentIndex(15)

# -------------------------------------------------choose_need_homedesign_page--------------------------------------------- #

class choose_need_homedesign(QMainWindow):
    def __init__(self) -> None :
        super(choose_need_homedesign, self).__init__()
        loadUi("choose_need_homedesign.ui", self)
        self.pushButton_back.clicked.connect(self.backbutton_clicked)

        self.pushButton_paintdesign.clicked.connect(self.paintdesignbutton_clicked)
        self.pushButton_holepatch.clicked.connect(self.holepatchbutton_clicked)
        self.pushButton_repaint.clicked.connect(self.repaintbutton_clicked)

    def backbutton_clicked(self):
        widget.setCurrentIndex(4)

    def paintdesignbutton_clicked(self):
        widget.setCurrentIndex(15)

    def holepatchbutton_clicked(self):
        widget.setCurrentIndex(15)

    def repaintbutton_clicked(self):
        widget.setCurrentIndex(15)

# --------------------------------------------------choose_need_cleaning_page---------------------------------------------- #

class choose_need_cleaning(QMainWindow):
    def __init__(self) -> None :
        super(choose_need_cleaning, self).__init__()
        loadUi("choose_need_cleaning.ui", self)
        self.pushButton_back.clicked.connect(self.backbutton_clicked)

        self.pushButton_genclean.clicked.connect(self.gencleanbutton_clicked)
        self.pushButton_commclean.clicked.connect(self.commcleanbutton_clicked)
        self.pushButton_sprclean.clicked.connect(self.sprcleanbutton_clicked)
        self.pushButton_decclean.clicked.connect(self.deccleanbutton_clicked)
        self.pushButton_partyclean.clicked.connect(self.partycleanbutton_clicked)
        self.pushButton_eotclean.clicked.connect(self.eotcleanbutton_clicked)

    def backbutton_clicked(self):
        widget.setCurrentIndex(4)

    def gencleanbutton_clicked(self):
        widget.setCurrentIndex(15)

    def commcleanbutton_clicked(self):
        widget.setCurrentIndex(15)

    def sprcleanbutton_clicked(self):
        widget.setCurrentIndex(15)

    def deccleanbutton_clicked(self):
        widget.setCurrentIndex(15)

    def partycleanbutton_clicked(self):
        widget.setCurrentIndex(15)

    def eotcleanbutton_clicked(self):
        widget.setCurrentIndex(15)

# ------------------------------------------------------transactions_page-------------------------------------------------- #

class transaction_page(QMainWindow):
    def __init__(self) -> None :
        super(transaction_page, self).__init__()
        loadUi("transaction_page.ui", self)
        self.pushButton_back.clicked.connect(self.backbutton_clicked)
        self.pushButton_paytm.clicked.connect(self.paytmbutton_clicked)
        self.pushButton_upi.clicked.connect(self.upibutton_clicked)
        self.pushButton_netbank.clicked.connect(self.netbankbutton_clicked)

    def backbutton_clicked(self):
        widget.setCurrentIndex(4)

    def paytmbutton_clicked(self):
        widget.setCurrentIndex(16)

    def upibutton_clicked(self):
        widget.setCurrentIndex(17)

    def netbankbutton_clicked(self):
        widget.setCurrentIndex(18)

# ---------------------------------------------------transactions_paytm_page----------------------------------------------- #

class transaction_paytm_page(QMainWindow):
    def __init__(self) -> None :
        super(transaction_paytm_page, self).__init__()
        loadUi("transaction_paytm.ui", self)
        self.pushButton_pay.clicked.connect(self.paybutton_clicked)
        self.pushButton_cancel.clicked.connect(self.cancelbutton_clicked)

    def paybutton_clicked(self):
        error_dialog = QtWidgets.QErrorMessage(self)
        error_dialog.setWindowTitle('Booking')
        error_dialog.showMessage('Your booking has been placed.')
        widget.setCurrentIndex(4)

    def cancelbutton_clicked(self):
        widget.setCurrentIndex(4)

# ----------------------------------------------------transactions_upi_page------------------------------------------------ #

class transaction_upi_page(QMainWindow):
    def __init__(self) -> None :
        super(transaction_upi_page, self).__init__()
        loadUi("transaction_upi.ui", self)
        self.pushButton_pay.clicked.connect(self.paybutton_clicked)
        self.pushButton_cancel.clicked.connect(self.cancelbutton_clicked)

    def paybutton_clicked(self):
        error_dialog = QtWidgets.QErrorMessage(self)
        error_dialog.setWindowTitle('Booking')
        error_dialog.showMessage('Your booking has been placed.')
        widget.setCurrentIndex(4)

    def cancelbutton_clicked(self):
        widget.setCurrentIndex(4)

# ------------------------------------------------transactions_netbanking_page--------------------------------------------- #

class transaction_netbanking_page(QMainWindow):
    def __init__(self) -> None :
        super(transaction_netbanking_page, self).__init__()
        loadUi("transaction_netbanking.ui", self)
        self.pushButton_pay.clicked.connect(self.paybutton_clicked)
        self.pushButton_cancel.clicked.connect(self.cancelbutton_clicked)

    def paybutton_clicked(self):
        error_dialog = QtWidgets.QErrorMessage(self)
        error_dialog.setWindowTitle('Booking')
        error_dialog.showMessage('Your booking has been placed.')
        widget.setCurrentIndex(4)
        
    def cancelbutton_clicked(self):
        widget.setCurrentIndex(4)

# -----------------------------------------------indexing for stacked widget----------------------------------------------- #

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
widget.setMaximumHeight(600)
widget.setMaximumWidth(800)
widget.setMinimumHeight(600)
widget.setMinimumWidth(800)

login_register = loginregister()
login = login_page()
register = register_page()
fcbkregister = fcbk_register_page()
home = home_page()
bookings = bookings_page()
electricals = electricals_page()
mechanicals = mechanicals_page()
choose_need_electricals = choose_need_electrical()
choose_need_computers = choose_need_computer()
choose_need_mechanicals = choose_need_mechanical()
choose_need_plumbings = choose_need_plumbing()
choose_need_laundrys = choose_need_laundry()
choose_need_homedesigns = choose_need_homedesign()
choose_need_cleanings = choose_need_cleaning()
transactions = transaction_page()
transactions_paytm = transaction_paytm_page()
transactions_upi = transaction_upi_page()
transactions_netbanking = transaction_netbanking_page()

widget.addWidget(login_register)                #00
widget.addWidget(login)                         #01
widget.addWidget(register)                      #02
widget.addWidget(fcbkregister)                  #03
widget.addWidget(home)                          #04
widget.addWidget(bookings)                      #05
widget.addWidget(electricals)                   #06
widget.addWidget(mechanicals)                   #07
widget.addWidget(choose_need_electricals)       #08
widget.addWidget(choose_need_computers)         #09
widget.addWidget(choose_need_mechanicals)       #10
widget.addWidget(choose_need_plumbings)         #11
widget.addWidget(choose_need_laundrys)          #12
widget.addWidget(choose_need_homedesigns)       #13
widget.addWidget(choose_need_cleanings)         #14
widget.addWidget(transactions)                  #15
widget.addWidget(transactions_paytm)            #16
widget.addWidget(transactions_upi)              #17
widget.addWidget(transactions_netbanking)       #18

widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")

