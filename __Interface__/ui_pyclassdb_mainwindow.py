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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QWidget)
# import rc_resource

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(708, 692)
        MainWindow.setMaximumSize(QSize(708, 692))
        MainWindow.setStyleSheet(u"*{\n"
"background-color: rgb(0, 89, 146);\n"
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignTop)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
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
        self.getStartBtn.setFont(font1)

        self.gridLayout_2.addWidget(self.getStartBtn, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_home)
        self.page_host = QWidget()
        self.page_host.setObjectName(u"page_host")
        self.gridLayout_3 = QGridLayout(self.page_host)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_4 = QSpacerItem(20, 140, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 0, 0, 1, 1)

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

        self.gridLayout_3.addWidget(self.hostNextBtn, 5, 0, 1, 1, Qt.AlignHCenter)

        self.label_4 = QLabel(self.page_host)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 319, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 6, 0, 1, 1)

        self.lineEdit_host = QLineEdit(self.page_host)
        self.lineEdit_host.setObjectName(u"lineEdit_host")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_host.sizePolicy().hasHeightForWidth())
        self.lineEdit_host.setSizePolicy(sizePolicy3)
        self.lineEdit_host.setMinimumSize(QSize(400, 50))

        self.gridLayout_3.addWidget(self.lineEdit_host, 4, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_host)
        self.page_credentials = QWidget()
        self.page_credentials.setObjectName(u"page_credentials")
        self.gridLayout_4 = QGridLayout(self.page_credentials)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 6, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_5 = QLabel(self.page_credentials)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_userName = QLineEdit(self.page_credentials)
        self.lineEdit_userName.setObjectName(u"lineEdit_userName")
        self.lineEdit_userName.setMinimumSize(QSize(400, 50))

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

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_password)


        self.gridLayout_4.addLayout(self.formLayout, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.credentialNextBtn = QPushButton(self.page_credentials)
        self.credentialNextBtn.setObjectName(u"credentialNextBtn")
        self.credentialNextBtn.setMinimumSize(QSize(140, 40))
        self.credentialNextBtn.setFont(font2)

        self.gridLayout_4.addWidget(self.credentialNextBtn, 5, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_6 = QSpacerItem(20, 140, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_6, 0, 0, 1, 1)

        self.label_7 = QLabel(self.page_credentials)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setFont(font1)

        self.gridLayout_4.addWidget(self.label_7, 1, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_4.addItem(self.verticalSpacer_8, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_credentials)
        self.page_database = QWidget()
        self.page_database.setObjectName(u"page_database")
        self.gridLayout_5 = QGridLayout(self.page_database)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_9 = QSpacerItem(20, 140, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_9, 0, 0, 1, 1)

        self.databaseNextBtn = QPushButton(self.page_database)
        self.databaseNextBtn.setObjectName(u"databaseNextBtn")
        sizePolicy2.setHeightForWidth(self.databaseNextBtn.sizePolicy().hasHeightForWidth())
        self.databaseNextBtn.setSizePolicy(sizePolicy2)
        self.databaseNextBtn.setMinimumSize(QSize(140, 40))
        self.databaseNextBtn.setFont(font2)

        self.gridLayout_5.addWidget(self.databaseNextBtn, 5, 0, 1, 1, Qt.AlignHCenter)

        self.label_8 = QLabel(self.page_database)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        self.label_8.setFont(font1)

        self.gridLayout_5.addWidget(self.label_8, 1, 0, 1, 1, Qt.AlignHCenter)

        self.lineEdit_database = QLineEdit(self.page_database)
        self.lineEdit_database.setObjectName(u"lineEdit_database")
        sizePolicy3.setHeightForWidth(self.lineEdit_database.sizePolicy().hasHeightForWidth())
        self.lineEdit_database.setSizePolicy(sizePolicy3)
        self.lineEdit_database.setMinimumSize(QSize(400, 50))

        self.gridLayout_5.addWidget(self.lineEdit_database, 3, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_10, 6, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_5.addItem(self.verticalSpacer_11, 2, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_5.addItem(self.verticalSpacer_12, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_database)
        self.page_table = QWidget()
        self.page_table.setObjectName(u"page_table")
        self.layoutWidget = QWidget(self.page_table)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 50, 126, 45))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.horizontalLayout.addWidget(self.label_9)

        self.checkBox = QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font2)
        self.checkBox.setIconSize(QSize(30, 30))
        self.checkBox.setChecked(True)
        self.checkBox.setTristate(False)

        self.horizontalLayout.addWidget(self.checkBox)

        self.stackedWidget.addWidget(self.page_table)
        self.page_summery = QWidget()
        self.page_summery.setObjectName(u"page_summery")
        self.stackedWidget.addWidget(self.page_summery)

        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"All Right Reserved @ 2023", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PyClassDB", None))
        self.label_3.setText("")
        self.getStartBtn.setText(QCoreApplication.translate("MainWindow", u"Get Start", None))
        self.hostNextBtn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Host", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.credentialNextBtn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Credentials", None))
        self.databaseNextBtn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Database", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"ALL", None))
        self.checkBox.setText("")
    # retranslateUi

