# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'geninterfaceuggYZu.ui'
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
        MainWindow.resize(990, 608)
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
        self.slideMenu = QWidget(self.centralwidget)
        self.slideMenu.setObjectName(u"slideMenu")
        self.slideMenu.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout = QVBoxLayout(self.slideMenu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.slideMenuSubContainer = QWidget(self.slideMenu)
        self.slideMenuSubContainer.setObjectName(u"slideMenuSubContainer")
        self.slideMenuSubContainer.setMinimumSize(QSize(0, 0))
        self.slideMenuSubContainer.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.slideMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.slideMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 10, 0, 10)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.slideMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setStyleSheet(u"selection-color: rgb(117, 113, 143);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(24, 24))
        self.homeBtn.setCheckable(False)

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.myprofileBtn = QPushButton(self.frame_2)
        self.myprofileBtn.setObjectName(u"myprofileBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.myprofileBtn.setIcon(icon2)
        self.myprofileBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.myprofileBtn)

        self.yourorderBtn = QPushButton(self.frame_2)
        self.yourorderBtn.setObjectName(u"yourorderBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/shopping-cart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.yourorderBtn.setIcon(icon3)
        self.yourorderBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.yourorderBtn)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.slideMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.settingsBtn = QPushButton(self.frame_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon4)
        self.settingsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.settingsBtn)

        self.aboutusBtn = QPushButton(self.frame_3)
        self.aboutusBtn.setObjectName(u"aboutusBtn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aboutusBtn.setIcon(icon5)
        self.aboutusBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.aboutusBtn)

        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon6)
        self.helpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.helpBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.slideMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.slideMenu, 0, Qt.AlignLeft)

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
        self.search_2.setMaximumSize(QSize(500, 16777215))
        self.search_2.setFrameShape(QFrame.StyledPanel)
        self.search_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.search_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_4 = QFrame(self.search_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon7)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.pushButton)


        self.horizontalLayout_8.addWidget(self.frame_5)


        self.horizontalLayout_7.addWidget(self.frame_4)

        self.search = QLineEdit(self.search_2)
        self.search.setObjectName(u"search")
        self.search.setMinimumSize(QSize(300, 0))
        self.search.setMaximumSize(QSize(100, 20))
        self.search.setAutoFillBackground(False)
        self.search.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-bottom: 3px solid rgb(230,5,64);")
        self.search.setClearButtonEnabled(True)

        self.horizontalLayout_7.addWidget(self.search, 0, Qt.AlignTop)

        self.searchBtn = QPushButton(self.search_2)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setMinimumSize(QSize(0, 0))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.searchBtn.setIcon(icon8)

        self.horizontalLayout_7.addWidget(self.searchBtn, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_3.addWidget(self.search_2, 0, Qt.AlignTop)

        self.logo_2 = QFrame(self.headerFrame)
        self.logo_2.setObjectName(u"logo_2")
        self.logo_2.setFrameShape(QFrame.StyledPanel)
        self.logo_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.logo_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.logo = QPushButton(self.logo_2)
        self.logo.setObjectName(u"logo")

        self.horizontalLayout_6.addWidget(self.logo)


        self.horizontalLayout_3.addWidget(self.logo_2, 0, Qt.AlignTop)

        self.windowOption = QFrame(self.headerFrame)
        self.windowOption.setObjectName(u"windowOption")
        self.windowOption.setFrameShape(QFrame.StyledPanel)
        self.windowOption.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.windowOption)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.minimizeBtn = QPushButton(self.windowOption)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.minimizeBtn.sizePolicy().hasHeightForWidth())
        self.minimizeBtn.setSizePolicy(sizePolicy2)
        self.minimizeBtn.setMinimumSize(QSize(0, 0))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon9)

        self.horizontalLayout_5.addWidget(self.minimizeBtn, 0, Qt.AlignRight)

        self.maximizeBtn = QPushButton(self.windowOption)
        self.maximizeBtn.setObjectName(u"maximizeBtn")
        sizePolicy2.setHeightForWidth(self.maximizeBtn.sizePolicy().hasHeightForWidth())
        self.maximizeBtn.setSizePolicy(sizePolicy2)
        self.maximizeBtn.setMinimumSize(QSize(0, 0))
        self.maximizeBtn.setMaximumSize(QSize(16777215, 16777215))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeBtn.setIcon(icon10)

        self.horizontalLayout_5.addWidget(self.maximizeBtn, 0, Qt.AlignRight)

        self.closeBtn = QPushButton(self.windowOption)
        self.closeBtn.setObjectName(u"closeBtn")
        sizePolicy2.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy2)
        self.closeBtn.setMinimumSize(QSize(0, 0))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon11)

        self.horizontalLayout_5.addWidget(self.closeBtn, 0, Qt.AlignRight)


        self.horizontalLayout_3.addWidget(self.windowOption, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.headerFrame, 0, Qt.AlignTop)

        self.mainBodyFrame = QFrame(self.mainBodyContainer)
        self.mainBodyFrame.setObjectName(u"mainBodyFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainBodyFrame.sizePolicy().hasHeightForWidth())
        self.mainBodyFrame.setSizePolicy(sizePolicy3)
        self.mainBodyFrame.setFrameShape(QFrame.StyledPanel)
        self.mainBodyFrame.setFrameShadow(QFrame.Raised)

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
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/box.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon12)

        self.verticalLayout_6.addWidget(self.pushButton_4, 0, Qt.AlignBottom)


        self.horizontalLayout_4.addWidget(self.frame_8, 0, Qt.AlignBottom)

        self.sizeGrip = QFrame(self.footer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(10, 10))
        self.sizeGrip.setMaximumSize(QSize(10, 10))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.sizeGrip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_5.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
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
        self.aboutusBtn.setToolTip(QCoreApplication.translate("MainWindow", u"About Us", None))
#endif // QT_CONFIG(tooltip)
        self.aboutusBtn.setText(QCoreApplication.translate("MainWindow", u"ABOUT US", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"HELP", None))
        self.pushButton.setText("")
        self.search.setText("")
        self.search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search", None))
        self.searchBtn.setText("")
        self.logo.setText(QCoreApplication.translate("MainWindow", u"logo", None))
        self.minimizeBtn.setText("")
        self.maximizeBtn.setText("")
        self.closeBtn.setText("")
        self.appVersion.setText(QCoreApplication.translate("MainWindow", u"Gen Servives v1.0", None))
        self.pushButton_4.setText("")
    # retranslateUi

