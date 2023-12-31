# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pyclassdb_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableView, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(708, 692)
        MainWindow.setMaximumSize(QSize(708, 692))
        icon = QIcon()
        icon.addFile(u":/icon/resource/icon/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 89, 146);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border-radius: 8px;\n"
"	background-color: rgb(0, 51, 83);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: \"#5A38DA\";\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:Hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(137, 145, 255);\n"
"}\n"
"")
        MainWindow.setIconSize(QSize(50, 50))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.gridLayout_2 = QGridLayout(self.page_home)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.page_home)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 500))
        self.label_3.setPixmap(QPixmap(u":/image/resource/image/Transform Your MySQL Table to Python Class.png"))

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1, Qt.AlignHCenter)

        self.getStartBtn = QPushButton(self.page_home)
        self.getStartBtn.setObjectName(u"getStartBtn")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.getStartBtn.setFont(font1)

        self.gridLayout_2.addWidget(self.getStartBtn, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_home)
        self.page_host = QWidget()
        self.page_host.setObjectName(u"page_host")
        self.gridLayout_3 = QGridLayout(self.page_host)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.hostNextBtn = QPushButton(self.page_host)
        self.hostNextBtn.setObjectName(u"hostNextBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.hostNextBtn.sizePolicy().hasHeightForWidth())
        self.hostNextBtn.setSizePolicy(sizePolicy2)
        self.hostNextBtn.setMinimumSize(QSize(140, 40))
        font2 = QFont()
        font2.setPointSize(15)
        self.hostNextBtn.setFont(font2)

        self.gridLayout_3.addWidget(self.hostNextBtn, 7, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 270, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 8, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 170, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_3.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.hostBackBtn = QPushButton(self.page_host)
        self.hostBackBtn.setObjectName(u"hostBackBtn")
        icon1 = QIcon()
        icon1.addFile(u":/icon/resource/icon/chevron-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.hostBackBtn.setIcon(icon1)
        self.hostBackBtn.setIconSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.hostBackBtn, 0, 0, 1, 1, Qt.AlignLeft)

        self.label_4 = QLabel(self.page_host)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setPointSize(20)
        self.label_4.setFont(font3)

        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1, Qt.AlignHCenter)

        self.lineEdit_host = QLineEdit(self.page_host)
        self.lineEdit_host.setObjectName(u"lineEdit_host")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_host.sizePolicy().hasHeightForWidth())
        self.lineEdit_host.setSizePolicy(sizePolicy3)
        self.lineEdit_host.setMinimumSize(QSize(400, 50))
        font4 = QFont()
        font4.setPointSize(18)
        self.lineEdit_host.setFont(font4)
        self.lineEdit_host.setAutoFillBackground(False)
        self.lineEdit_host.setMaxLength(15)

        self.gridLayout_3.addWidget(self.lineEdit_host, 5, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_13 = QSpacerItem(20, 92, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_13, 6, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_host)
        self.page_credentials = QWidget()
        self.page_credentials.setObjectName(u"page_credentials")
        self.gridLayout_4 = QGridLayout(self.page_credentials)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_7 = QLabel(self.page_credentials)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setFont(font3)

        self.gridLayout_4.addWidget(self.label_7, 2, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_6 = QSpacerItem(20, 78, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_6, 1, 0, 1, 1)

        self.credentialNextBtn = QPushButton(self.page_credentials)
        self.credentialNextBtn.setObjectName(u"credentialNextBtn")
        self.credentialNextBtn.setMinimumSize(QSize(140, 40))
        self.credentialNextBtn.setFont(font2)

        self.gridLayout_4.addWidget(self.credentialNextBtn, 6, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_5 = QSpacerItem(20, 116, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 7, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_4.addItem(self.verticalSpacer_8, 5, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(35)
        self.label_5 = QLabel(self.page_credentials)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_userName = QLineEdit(self.page_credentials)
        self.lineEdit_userName.setObjectName(u"lineEdit_userName")
        self.lineEdit_userName.setMinimumSize(QSize(400, 50))
        self.lineEdit_userName.setFont(font4)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_userName)

        self.verticalSpacer_7 = QSpacerItem(20, 16, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.formLayout.setItem(1, QFormLayout.SpanningRole, self.verticalSpacer_7)

        self.label_6 = QLabel(self.page_credentials)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_password = QLineEdit(self.page_credentials)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setMinimumSize(QSize(400, 50))
        self.lineEdit_password.setFont(font4)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_password)


        self.gridLayout_4.addLayout(self.formLayout, 4, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.credentialBackBtn = QPushButton(self.page_credentials)
        self.credentialBackBtn.setObjectName(u"credentialBackBtn")
        self.credentialBackBtn.setIcon(icon1)
        self.credentialBackBtn.setIconSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.credentialBackBtn, 0, 0, 1, 1, Qt.AlignLeft)

        self.stackedWidget.addWidget(self.page_credentials)
        self.page_database = QWidget()
        self.page_database.setObjectName(u"page_database")
        self.gridLayout_5 = QGridLayout(self.page_database)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_9 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_9, 1, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 180, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_10, 7, 0, 1, 1)

        self.lineEdit_database = QLineEdit(self.page_database)
        self.lineEdit_database.setObjectName(u"lineEdit_database")
        sizePolicy3.setHeightForWidth(self.lineEdit_database.sizePolicy().hasHeightForWidth())
        self.lineEdit_database.setSizePolicy(sizePolicy3)
        self.lineEdit_database.setMinimumSize(QSize(400, 50))
        self.lineEdit_database.setFont(font4)

        self.gridLayout_5.addWidget(self.lineEdit_database, 4, 0, 1, 1, Qt.AlignHCenter)

        self.label_8 = QLabel(self.page_database)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        self.label_8.setFont(font3)

        self.gridLayout_5.addWidget(self.label_8, 2, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_5.addItem(self.verticalSpacer_12, 5, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_5.addItem(self.verticalSpacer_11, 3, 0, 1, 1)

        self.databaseNextBtn = QPushButton(self.page_database)
        self.databaseNextBtn.setObjectName(u"databaseNextBtn")
        sizePolicy2.setHeightForWidth(self.databaseNextBtn.sizePolicy().hasHeightForWidth())
        self.databaseNextBtn.setSizePolicy(sizePolicy2)
        self.databaseNextBtn.setMinimumSize(QSize(140, 40))
        self.databaseNextBtn.setFont(font2)

        self.gridLayout_5.addWidget(self.databaseNextBtn, 6, 0, 1, 1, Qt.AlignHCenter)

        self.databaseBackBtn = QPushButton(self.page_database)
        self.databaseBackBtn.setObjectName(u"databaseBackBtn")
        self.databaseBackBtn.setIcon(icon1)
        self.databaseBackBtn.setIconSize(QSize(30, 30))

        self.gridLayout_5.addWidget(self.databaseBackBtn, 0, 0, 1, 1, Qt.AlignLeft)

        self.stackedWidget.addWidget(self.page_database)
        self.page_table = QWidget()
        self.page_table.setObjectName(u"page_table")
        self.gridLayout_6 = QGridLayout(self.page_table)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tableBackBtn = QPushButton(self.page_table)
        self.tableBackBtn.setObjectName(u"tableBackBtn")
        self.tableBackBtn.setMaximumSize(QSize(34, 30))
        self.tableBackBtn.setIcon(icon1)
        self.tableBackBtn.setIconSize(QSize(30, 30))

        self.gridLayout_6.addWidget(self.tableBackBtn, 0, 0, 1, 1)

        self.tableView = QTableView(self.page_table)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setFont(font4)
        self.tableView.setStyleSheet(u"QTableView{\n"
"	border-radius:25px;\n"
"}\n"
"QHeaderView{\n"
"	font: 700 15pt \"Segoe UI\";\n"
"	border-radius: 10px;\n"
"	background-color: rgb(90, 56, 218);\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    text-align:center;\n"
"    padding:3px;\n"
"    margin:0px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255,0);\n"
"}\n"
"\n"
"QHeaderView::section:selected\n"
"{\n"
"    color:#FFFFFF;\n"
"    border:1px solid #242424;\n"
"}\n"
"QScrollBar:vertical{\n"
"    width:8px; \n"
"    border-style:flat;\n"
"    border-radius: 4px;\n"
"    border:0px;\n"
"     background: #19191A;\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"    background: rgba(255,255,255,0.50);\n"
"    border-radius: 4px;\n"
"    width:8px;\n"
"    min-height:91px;\n"
"    border-style:flat;\n"
"}\n"
"QScrollBar::handle:vertical::hover{\n"
"    background: rgba(255,255,255,0.90);\n"
"    border-radius: 4px;\n"
"    width:8px;\n"
"}\n"
"QScrollBar::handle:vertical::pressed{\n"
"    background: rgba(255,255,255,0.90);\n"
""
                        "    border-radius:4px;\n"
"    width:8px;\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
"    background: #19191A;\n"
"border-style:flat;\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
"   background: #19191A;\n"
"border-style:flat;\n"
"}\n"
"QScrollBar::add-line:vertical{\n"
"   background: #19191A;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"   background: #19191A;\n"
"}\n"
"QScrollBar:horizontal{\n"
"    height:8px; \n"
"    border-style:flat;\n"
"    border-radius: 4px;\n"
"    border:0px;\n"
"background: #19191A;\n"
"}\n"
"QScrollBar::handle:horizontal{\n"
"    background: rgba(255,255,255,0.50);\n"
"    border-radius: 4px;\n"
"    height:8px;\n"
"    min-width:91px;\n"
"    border-style:flat;\n"
"}\n"
"QScrollBar::handle:horizontal::hover{\n"
"    background: rgba(255,255,255,0.90);\n"
"    border-radius: 4px;\n"
"    height:8px;\n"
"}\n"
"QScrollBar::handle:horizontal::pressed{\n"
"    background: rgba(255,255,255,0.90);\n"
"    border-radius:4px;\n"
"    height:8px;\n"
"}\n"
"QScrollBar::sub-page:horizon"
                        "tal {\n"
"    background: #19191A;\n"
"    border-style:flat;\n"
"}\n"
"QScrollBar::add-page:horizontal {\n"
"   background: #19191A;\n"
"    border-style:flat;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   background: #19191A;\n"
"}\n"
"QScrollBar::add-line:horizontal{\n"
"   background: #19191A;\n"
"}\n"
"\n"
"")

        self.gridLayout_6.addWidget(self.tableView, 1, 0, 1, 1)

        self.tableNextBtn = QPushButton(self.page_table)
        self.tableNextBtn.setObjectName(u"tableNextBtn")
        self.tableNextBtn.setMinimumSize(QSize(140, 40))
        self.tableNextBtn.setFont(font2)

        self.gridLayout_6.addWidget(self.tableNextBtn, 2, 0, 1, 1, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page_table)
        self.page_summery = QWidget()
        self.page_summery.setObjectName(u"page_summery")
        self.summeryBackBtn = QPushButton(self.page_summery)
        self.summeryBackBtn.setObjectName(u"summeryBackBtn")
        self.summeryBackBtn.setGeometry(QRect(10, 10, 41, 29))
        self.summeryBackBtn.setIcon(icon1)
        self.summeryBackBtn.setIconSize(QSize(30, 30))
        self.pushButton_2 = QPushButton(self.page_summery)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(290, 500, 140, 40))
        self.pushButton_2.setMinimumSize(QSize(140, 40))
        self.pushButton_2.setFont(font2)
        self.label_10 = QLabel(self.page_summery)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(32, 79, 621, 401))
        self.label_10.setPixmap(QPixmap(u":/image/resource/image/taskFinished.png"))
        self.stackedWidget.addWidget(self.page_summery)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.lineEdit_host.returnPressed.connect(self.hostNextBtn.click)
        self.lineEdit_userName.returnPressed.connect(self.lineEdit_password.setFocus)
        self.lineEdit_password.returnPressed.connect(self.credentialNextBtn.click)
        self.lineEdit_database.returnPressed.connect(self.databaseNextBtn.click)
        self.pushButton_2.clicked.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyClassDB", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PyClassDB", None))
        self.label_3.setText("")
        self.getStartBtn.setText(QCoreApplication.translate("MainWindow", u"Get Start", None))
        self.hostNextBtn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.hostBackBtn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Host", None))
        self.lineEdit_host.setText(QCoreApplication.translate("MainWindow", u"localhost", None))
        self.lineEdit_host.setPlaceholderText(QCoreApplication.translate("MainWindow", u"127.0.0.1", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Credentials", None))
        self.credentialNextBtn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.lineEdit_userName.setText(QCoreApplication.translate("MainWindow", u"root", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_password.setText("")
        self.credentialBackBtn.setText("")
        self.lineEdit_database.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Database", None))
        self.databaseNextBtn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.databaseBackBtn.setText("")
        self.tableBackBtn.setText("")
        self.tableNextBtn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.summeryBackBtn.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Finished", None))
        self.label_10.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"All Right Reserved @ 2023", None))
    # retranslateUi

