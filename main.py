

########################################################################
## IMPORTS
########################################################################
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
        loadUi("RegisterLogin_UI.ui", self)
        self.setWindowTitle("Gen-Services")

########################################################################
# IMPORT GUI FILE
#from ui_Gen_Services import *
########################################################################


########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #######################################################################
        ## # Remove window tittle bar
        ########################################################################    
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 

        #######################################################################
        ## # Set main background to transparent
        ########################################################################  
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
      
        #######################################################################
        ## # Shadow effect style
        ########################################################################  
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))
        
        #######################################################################
        ## # Appy shadow to central widget
        ########################################################################  
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        #######################################################################
        # Set window Icon
        # This icon and title will not appear on our app main window because we removed the title bar
        #######################################################################
        
        # Set window tittle
        self.setWindowTitle("Gen Services v1.0")

        #################################################################################
        # Window Size grip to resize window
        #################################################################################
        QSizeGrip(self.ui.sizeGrip)

        #######################################################################
        #Minimize window
        self.ui.minimizeBtn.clicked.connect(lambda: self.showMinimized())
        #######################################################################
        #Close window
        self.ui.closeBtn.clicked.connect(lambda: self.close())


        #######################################################################
        #Restore/Maximize window
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())


        # ###############################################
        # Function to Move window on mouse drag event on the tittle bar
        # ###############################################
        def moveWindow(e):
            # Detect if the window is  normal size
            # ###############################################  
            if self.isMaximized() == False: #Not maximized
                # Move window only when window is normal size  
                # ###############################################
                #if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:  
                    #Move window 
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        #######################################################################

        #######################################################################
        # Add click event/Mouse move event/drag event to the top header to move the window
        #######################################################################
        self.ui.headerFrame.mouseMoveEvent = moveWindow
        #######################################################################


        #######################################################################
        #Left Menu toggle button
        


        self.show()



    #######################################################################
    # Add mouse events to the window
    #######################################################################
    def mousePressEvent(self, event):
        # ###############################################
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        # We will use this value to move the window
    #######################################################################
    #######################################################################



    #######################################################################
    # Update restore button icon on msximizing or minimizing window
    #######################################################################
    def restore_or_maximize_window(self):
        # If window is maxmized
        if self.isMaximized():
            self.showNormal()
            # Change Icon
           
        else:
            self.showMaximized()
           

########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
