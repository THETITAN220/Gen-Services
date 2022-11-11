# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'geninterfacePFSxNP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1040, 635)
        MainWindow.setStyleSheet(u"*{\n"
"  border:none;\n"
"  background-color:transparent;\n"
"  background:none;\n"
"  padding:0;\n"
"  margin:0;\n"
"  color:#fff;\n"
"}\n"
"\n"
"#centralwidget{\n"
"\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0.278607 rgba(12, 12, 12, 255), stop:0.701493 rgba(102, 102, 102, 255));\n"
"	background-color: rgb(31, 35, 42);\n"
"}\n"
"#leftMenuSubContainer{\n"
"background-color: #16191d\n"
"}\n"
"\n"
"#leftMenuSubContainer QPushButton{\n"
" text-align:left;\n"
" padding:5px 10px;\n"
" border-top-left-radius:10px;\n"
" border-bottom-left-radius:10px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slide_menu_container = QWidget(self.centralwidget)
        self.slide_menu_container.setObjectName(u"slide_menu_container")
        self.slide_menu_container.setMinimumSize(QSize(115, 100))
        self.slide_menu_container.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout = QVBoxLayout(self.slide_menu_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.slideMenuSubContainer = QWidget(self.slide_menu_container)
        self.slideMenuSubContainer.setObjectName(u"slideMenuSubContainer")
        self.slideMenuSubContainer.setMinimumSize(QSize(128, 100))
        self.slideMenuSubContainer.setMaximumSize(QSize(0, 16777215))
        self.frame_2 = QFrame(self.slideMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 150, 117, 441))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(117, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 10, 0, 10)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setMinimumSize(QSize(115, 0))
        self.homeBtn.setStyleSheet(u"selection-color: rgb(117, 113, 143);")
        icon = QIcon()
        icon.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon)
        self.homeBtn.setIconSize(QSize(24, 24))
        self.homeBtn.setCheckable(False)

        self.verticalLayout_2.addWidget(self.homeBtn)

        self.myprofileBtn = QPushButton(self.frame_2)
        self.myprofileBtn.setObjectName(u"myprofileBtn")
        self.myprofileBtn.setMinimumSize(QSize(115, 0))
        self.myprofileBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.myprofileBtn.setMouseTracking(True)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.myprofileBtn.setIcon(icon1)
        self.myprofileBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.myprofileBtn)

        self.yourorderBtn = QPushButton(self.frame_2)
        self.yourorderBtn.setObjectName(u"yourorderBtn")
        self.yourorderBtn.setMinimumSize(QSize(115, 0))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/shopping-cart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.yourorderBtn.setIcon(icon2)
        self.yourorderBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.yourorderBtn)

        self.settingsBtn = QPushButton(self.frame_2)
        self.settingsBtn.setObjectName(u"settingsBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon3)
        self.settingsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.settingsBtn)

        self.helpBtn = QPushButton(self.frame_2)
        self.helpBtn.setObjectName(u"helpBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon4)
        self.helpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.helpBtn)

        self.aboutusBtn = QPushButton(self.frame_2)
        self.aboutusBtn.setObjectName(u"aboutusBtn")
        self.aboutusBtn.setMinimumSize(QSize(100, 0))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aboutusBtn.setIcon(icon5)
        self.aboutusBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.aboutusBtn)

        self.frame = QFrame(self.slideMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(11, 11, 181, 120))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(0, -1, 171, 121))
        self.logo.setMinimumSize(QSize(50, 20))

        self.verticalLayout.addWidget(self.slideMenuSubContainer)


        self.horizontalLayout.addWidget(self.slide_menu_container, 0, Qt.AlignLeft)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy1)
        self.mainBodyContainer.setStyleSheet(u"background-color:{rgb(0, 255, 255)}")
        self.verticalLayout_5 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QFrame(self.mainBodyContainer)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setFrameShape(QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.search_2 = QFrame(self.headerFrame)
        self.search_2.setObjectName(u"search_2")
        self.search_2.setMinimumSize(QSize(685, 60))
        self.search_2.setMaximumSize(QSize(686, 16777215))
        self.search_2.setFrameShape(QFrame.StyledPanel)
        self.search_2.setFrameShadow(QFrame.Raised)
        self.searchBtn = QPushButton(self.search_2)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setGeometry(QRect(640, 10, 24, 45))
        self.searchBtn.setMinimumSize(QSize(0, 45))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.searchBtn.setIcon(icon6)
        self.search = QLineEdit(self.search_2)
        self.search.setObjectName(u"search")
        self.search.setGeometry(QRect(80, 10, 539, 32))
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.search.sizePolicy().hasHeightForWidth())
        self.search.setSizePolicy(sizePolicy2)
        self.search.setMinimumSize(QSize(539, 32))
        self.search.setMaximumSize(QSize(300, 20))
        self.search.setSizeIncrement(QSize(75, 0))
        self.search.setBaseSize(QSize(201, 0))
        self.search.setAutoFillBackground(False)
        self.search.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-bottom: 3px solid rgb(230,5,64);")
        self.search.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.search_2)

        self.windowOption = QFrame(self.headerFrame)
        self.windowOption.setObjectName(u"windowOption")
        self.windowOption.setFrameShape(QFrame.StyledPanel)
        self.windowOption.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.windowOption)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.minimizeBtn = QPushButton(self.windowOption)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.minimizeBtn.sizePolicy().hasHeightForWidth())
        self.minimizeBtn.setSizePolicy(sizePolicy3)
        self.minimizeBtn.setMinimumSize(QSize(0, 0))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon7)

        self.horizontalLayout_5.addWidget(self.minimizeBtn)

        self.restore_window_button = QPushButton(self.windowOption)
        self.restore_window_button.setObjectName(u"restore_window_button")
        sizePolicy3.setHeightForWidth(self.restore_window_button.sizePolicy().hasHeightForWidth())
        self.restore_window_button.setSizePolicy(sizePolicy3)
        self.restore_window_button.setMinimumSize(QSize(0, 0))
        self.restore_window_button.setMaximumSize(QSize(16777215, 16777215))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.restore_window_button)

        self.closeBtn = QPushButton(self.windowOption)
        self.closeBtn.setObjectName(u"closeBtn")
        sizePolicy3.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy3)
        self.closeBtn.setMinimumSize(QSize(0, 0))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon9)

        self.horizontalLayout_5.addWidget(self.closeBtn)


        self.horizontalLayout_3.addWidget(self.windowOption)


        self.verticalLayout_5.addWidget(self.headerFrame)

        self.mainBodyFrame = QFrame(self.mainBodyContainer)
        self.mainBodyFrame.setObjectName(u"mainBodyFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.mainBodyFrame.sizePolicy().hasHeightForWidth())
        self.mainBodyFrame.setSizePolicy(sizePolicy4)
        self.mainBodyFrame.setFrameShape(QFrame.StyledPanel)
        self.mainBodyFrame.setFrameShadow(QFrame.Raised)
        self.Cab = QFrame(self.mainBodyFrame)
        self.Cab.setObjectName(u"Cab")
        self.Cab.setGeometry(QRect(11, 11, 331, 271))
        self.Cab.setMinimumSize(QSize(0, 0))
        self.Cab.setFrameShape(QFrame.StyledPanel)
        self.Cab.setFrameShadow(QFrame.Raised)
        self.CabBtn = QPushButton(self.Cab)
        self.CabBtn.setObjectName(u"CabBtn")
        self.CabBtn.setGeometry(QRect(100, 220, 131, 31))
        self.label_2 = QLabel(self.Cab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 0, 275, 183))
        self.label_2.setSizeIncrement(QSize(0, 0))
        self.label_2.setPixmap(QPixmap(u"fuelcar.png"))
        self.label_2.setScaledContents(False)
        self.Cleaning = QFrame(self.mainBodyFrame)
        self.Cleaning.setObjectName(u"Cleaning")
        self.Cleaning.setGeometry(QRect(370, 20, 240, 277))
        self.Cleaning.setFrameShape(QFrame.StyledPanel)
        self.Cleaning.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.Cleaning)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 10, 218, 201))
        self.label_3.setPixmap(QPixmap(u"cleaning.png"))
        self.label_3.setScaledContents(True)
        self.CleaningBtn = QPushButton(self.Cleaning)
        self.CleaningBtn.setObjectName(u"CleaningBtn")
        self.CleaningBtn.setGeometry(QRect(70, 220, 57, 16))
        self.Laundry = QFrame(self.mainBodyFrame)
        self.Laundry.setObjectName(u"Laundry")
        self.Laundry.setGeometry(QRect(620, 10, 322, 277))
        self.Laundry.setFrameShape(QFrame.StyledPanel)
        self.Laundry.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.Laundry)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(11, 11, 300, 168))
        self.label_4.setPixmap(QPixmap(u"laundry.png"))
        self.label_4.setScaledContents(False)
        self.LaundryBtn = QPushButton(self.Laundry)
        self.LaundryBtn.setObjectName(u"LaundryBtn")
        self.LaundryBtn.setGeometry(QRect(120, 210, 53, 16))
        self.Electrical = QFrame(self.mainBodyFrame)
        self.Electrical.setObjectName(u"Electrical")
        self.Electrical.setGeometry(QRect(30, 290, 321, 251))
        self.Electrical.setFrameShape(QFrame.StyledPanel)
        self.Electrical.setFrameShadow(QFrame.Raised)
        self.ElectricalBtn = QPushButton(self.Electrical)
        self.ElectricalBtn.setObjectName(u"ElectricalBtn")
        self.ElectricalBtn.setGeometry(QRect(90, 210, 131, 41))
        self.label_5 = QLabel(self.Electrical)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 40, 221, 151))
        self.label_5.setPixmap(QPixmap(u"light.png"))
        self.label_5.setScaledContents(True)
        self.Yard = QFrame(self.mainBodyFrame)
        self.Yard.setObjectName(u"Yard")
        self.Yard.setGeometry(QRect(620, 290, 322, 261))
        self.Yard.setFrameShape(QFrame.StyledPanel)
        self.Yard.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.Yard)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(11, 11, 244, 207))
        self.label_7.setPixmap(QPixmap(u"yard_work.png"))
        self.YardBtn = QPushButton(self.Yard)
        self.YardBtn.setObjectName(u"YardBtn")
        self.YardBtn.setGeometry(QRect(130, 230, 31, 16))
        self.Repair = QFrame(self.mainBodyFrame)
        self.Repair.setObjectName(u"Repair")
        self.Repair.setGeometry(QRect(380, 280, 211, 261))
        self.Repair.setFrameShape(QFrame.StyledPanel)
        self.Repair.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.Repair)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 216, 233))
        self.label_6.setPixmap(QPixmap(u"mechanic.png"))
        self.RepairsBtn = QPushButton(self.Repair)
        self.RepairsBtn.setObjectName(u"RepairsBtn")
        self.RepairsBtn.setGeometry(QRect(60, 220, 91, 51))

        self.verticalLayout_5.addWidget(self.mainBodyFrame)

        self.footer = QFrame(self.mainBodyContainer)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.footer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.footer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.appVersion = QLabel(self.frame_9)
        self.appVersion.setObjectName(u"appVersion")

        self.verticalLayout_7.addWidget(self.appVersion, 0, Qt.AlignBottom)


        self.horizontalLayout_4.addWidget(self.frame_9)

        self.frame_8 = QFrame(self.footer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame_8)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/box.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon10)

        self.verticalLayout_6.addWidget(self.pushButton_4, 0, Qt.AlignBottom)


        self.horizontalLayout_4.addWidget(self.frame_8, 0, Qt.AlignBottom)

        self.sizeGrip = QFrame(self.footer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(10, 10))
        self.sizeGrip.setMaximumSize(QSize(10, 10))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.sizeGrip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_5.addWidget(self.footer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
#if QT_CONFIG(tooltip)
        self.myprofileBtn.setToolTip(QCoreApplication.translate("MainWindow", u"My Profile", None))
#endif // QT_CONFIG(tooltip)
        self.myprofileBtn.setText(QCoreApplication.translate("MainWindow", u"MY PROFILE", None))
#if QT_CONFIG(tooltip)
        self.yourorderBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Your Order", None))
#endif // QT_CONFIG(tooltip)
        self.yourorderBtn.setText(QCoreApplication.translate("MainWindow", u"YOUR ORDER", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"HELP", None))
#if QT_CONFIG(tooltip)
        self.aboutusBtn.setToolTip(QCoreApplication.translate("MainWindow", u"About Us", None))
#endif // QT_CONFIG(tooltip)
        self.aboutusBtn.setText(QCoreApplication.translate("MainWindow", u"ABOUT US", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"logo", None))
        self.searchBtn.setText("")
        self.search.setText("")
        self.search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search", None))
        self.minimizeBtn.setText("")
        self.restore_window_button.setText("")
        self.closeBtn.setText("")
        self.CabBtn.setText(QCoreApplication.translate("MainWindow", u"CAB", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.CleaningBtn.setText(QCoreApplication.translate("MainWindow", u"CLEANING", None))
        self.label_4.setText("")
        self.LaundryBtn.setText(QCoreApplication.translate("MainWindow", u"LAUNDRY", None))
        self.ElectricalBtn.setText(QCoreApplication.translate("MainWindow", u"ELECTRICAL", None))
        self.label_5.setText("")
        self.label_7.setText("")
        self.YardBtn.setText(QCoreApplication.translate("MainWindow", u"YARD", None))
        self.label_6.setText("")
        self.RepairsBtn.setText(QCoreApplication.translate("MainWindow", u"REPAIRS", None))
        self.appVersion.setText(QCoreApplication.translate("MainWindow", u"Gen Servives v1.0", None))
        self.pushButton_4.setText("")
    # retranslateUi

