########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinndesign.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import sys
import os
from PySide2 import *


########################################################################
# IMPORT GUI FILE
from ui_Gen_Services import *
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
        self.ui.open_close_side_bar_btn.clicked.connect(lambda: self.slideLeftMenu())


        self.show()




    ########################################################################
    # Slide left menu function
    ########################################################################
    def slideLeftMenu(self):
        # Get current left menu width
        width = self.ui.slideMenuSubContainer.width()

        # If minimized
        if width == 0:
            # Expand menu
            newWidth = 200
            
        # If maximized
        else:
            # Restore menu
            newWidth = 0
            

        # Animate the transition
        self.animation = QPropertyAnimation(self.ui.slideMenuSubContainer, b"maximumWidth")#Animate minimumWidht
        self.animation.setDuration(250)
        self.animation.setStartValue(width)#Start value is the current menu width
        self.animation.setEndValue(newWidth)#end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    #######################################################################





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