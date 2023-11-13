# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pyclassdb_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QFormLayout,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QTableView,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(708, 692)
        MainWindow.setMaximumSize(QSize(708, 692))
        MainWindow.setStyleSheet(
            "*{\n"
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
            '	background-color: "#5A38DA";\n'
            "	border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:Hover{\n"
            "	color: rgb(0, 0, 0);\n"
            "	background-color: rgb(137, 145, 255);\n"
            "}\n"
            ""
        )
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.stackedWidget.sizePolicy().hasHeightForWidth()
        )
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.page_home = QWidget()
        self.page_home.setObjectName("page_home")
        self.gridLayout_2 = QGridLayout(self.page_home)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QLabel(self.page_home)
        self.label_3.setObjectName("label_3")
        self.label_3.setMaximumSize(QSize(16777215, 500))
        self.label_3.setPixmap(
            QPixmap(
                ":/image/resource/image/Transform Your MySQL Table to Python Class.png"
            )
        )

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1, Qt.AlignHCenter)

        self.getStartBtn = QPushButton(self.page_home)
        self.getStartBtn.setObjectName("getStartBtn")
        font = QFont()
        font.setPointSize(20)
        self.getStartBtn.setFont(font)

        self.gridLayout_2.addWidget(self.getStartBtn, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_home)
        self.page_host = QWidget()
        self.page_host.setObjectName("page_host")
        self.gridLayout_3 = QGridLayout(self.page_host)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QLabel(self.page_host)
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(font)

        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(
            20, 140, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_3.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(
            20, 319, QSizePolicy.Minimum, QSizePolicy.Preferred
        )

        self.gridLayout_3.addItem(self.verticalSpacer_3, 7, 0, 1, 1)

        self.lineEdit_host = QLineEdit(self.page_host)
        self.lineEdit_host.setObjectName("lineEdit_host")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.lineEdit_host.sizePolicy().hasHeightForWidth()
        )
        self.lineEdit_host.setSizePolicy(sizePolicy1)
        self.lineEdit_host.setMinimumSize(QSize(400, 50))
        font1 = QFont()
        font1.setPointSize(18)
        self.lineEdit_host.setFont(font1)
        self.lineEdit_host.setAutoFillBackground(False)
        self.lineEdit_host.setMaxLength(15)

        self.gridLayout_3.addWidget(self.lineEdit_host, 5, 0, 1, 1, Qt.AlignHCenter)

        self.hostNextBtn = QPushButton(self.page_host)
        self.hostNextBtn.setObjectName("hostNextBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.hostNextBtn.sizePolicy().hasHeightForWidth())
        self.hostNextBtn.setSizePolicy(sizePolicy2)
        self.hostNextBtn.setMinimumSize(QSize(140, 40))
        font2 = QFont()
        font2.setPointSize(15)
        self.hostNextBtn.setFont(font2)

        self.gridLayout_3.addWidget(self.hostNextBtn, 6, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(
            20, 100, QSizePolicy.Minimum, QSizePolicy.Preferred
        )

        self.gridLayout_3.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.hostBackBtn = QPushButton(self.page_host)
        self.hostBackBtn.setObjectName("hostBackBtn")
        icon = QIcon()
        icon.addFile(
            ":/icon/resource/icon/chevron-left.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        self.hostBackBtn.setIcon(icon)
        self.hostBackBtn.setIconSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.hostBackBtn, 0, 0, 1, 1, Qt.AlignLeft)

        self.stackedWidget.addWidget(self.page_host)
        self.page_credentials = QWidget()
        self.page_credentials.setObjectName("page_credentials")
        self.gridLayout_4 = QGridLayout(self.page_credentials)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_7 = QLabel(self.page_credentials)
        self.label_7.setObjectName("label_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setFont(font)

        self.gridLayout_4.addWidget(self.label_7, 2, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_6 = QSpacerItem(
            20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_4.addItem(self.verticalSpacer_6, 1, 0, 1, 1)

        self.credentialNextBtn = QPushButton(self.page_credentials)
        self.credentialNextBtn.setObjectName("credentialNextBtn")
        self.credentialNextBtn.setMinimumSize(QSize(140, 40))
        self.credentialNextBtn.setFont(font2)

        self.gridLayout_4.addWidget(self.credentialNextBtn, 6, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_5 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_4.addItem(self.verticalSpacer_5, 7, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred
        )

        self.gridLayout_4.addItem(self.verticalSpacer_8, 5, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QLabel(self.page_credentials)
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_userName = QLineEdit(self.page_credentials)
        self.lineEdit_userName.setObjectName("lineEdit_userName")
        self.lineEdit_userName.setMinimumSize(QSize(400, 50))
        self.lineEdit_userName.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_userName)

        self.verticalSpacer_7 = QSpacerItem(
            20, 16, QSizePolicy.Minimum, QSizePolicy.Preferred
        )

        self.formLayout.setItem(1, QFormLayout.SpanningRole, self.verticalSpacer_7)

        self.label_6 = QLabel(self.page_credentials)
        self.label_6.setObjectName("label_6")
        self.label_6.setFont(font2)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_password = QLineEdit(self.page_credentials)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setMinimumSize(QSize(400, 50))
        self.lineEdit_password.setFont(font1)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_password)

        self.gridLayout_4.addLayout(self.formLayout, 4, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(
            20, 100, QSizePolicy.Minimum, QSizePolicy.Preferred
        )

        self.gridLayout_4.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.credentialBackBtn = QPushButton(self.page_credentials)
        self.credentialBackBtn.setObjectName("credentialBackBtn")
        self.credentialBackBtn.setIcon(icon)
        self.credentialBackBtn.setIconSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.credentialBackBtn, 0, 0, 1, 1, Qt.AlignLeft)

        self.stackedWidget.addWidget(self.page_credentials)
        self.page_database = QWidget()
        self.page_database.setObjectName("page_database")
        self.gridLayout_5 = QGridLayout(self.page_database)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalSpacer_9 = QSpacerItem(
            20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_5.addItem(self.verticalSpacer_9, 1, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(
            20, 180, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_5.addItem(self.verticalSpacer_10, 7, 0, 1, 1)

        self.lineEdit_database = QLineEdit(self.page_database)
        self.lineEdit_database.setObjectName("lineEdit_database")
        sizePolicy1.setHeightForWidth(
            self.lineEdit_database.sizePolicy().hasHeightForWidth()
        )
        self.lineEdit_database.setSizePolicy(sizePolicy1)
        self.lineEdit_database.setMinimumSize(QSize(400, 50))
        self.lineEdit_database.setFont(font1)

        self.gridLayout_5.addWidget(self.lineEdit_database, 4, 0, 1, 1, Qt.AlignHCenter)

        self.label_8 = QLabel(self.page_database)
        self.label_8.setObjectName("label_8")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        self.label_8.setFont(font)

        self.gridLayout_5.addWidget(self.label_8, 2, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_12 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Preferred
        )

        self.gridLayout_5.addItem(self.verticalSpacer_12, 5, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(
            20, 100, QSizePolicy.Minimum, QSizePolicy.Preferred
        )

        self.gridLayout_5.addItem(self.verticalSpacer_11, 3, 0, 1, 1)

        self.databaseNextBtn = QPushButton(self.page_database)
        self.databaseNextBtn.setObjectName("databaseNextBtn")
        sizePolicy2.setHeightForWidth(
            self.databaseNextBtn.sizePolicy().hasHeightForWidth()
        )
        self.databaseNextBtn.setSizePolicy(sizePolicy2)
        self.databaseNextBtn.setMinimumSize(QSize(140, 40))
        self.databaseNextBtn.setFont(font2)

        self.gridLayout_5.addWidget(self.databaseNextBtn, 6, 0, 1, 1, Qt.AlignHCenter)

        self.databaseBackBtn = QPushButton(self.page_database)
        self.databaseBackBtn.setObjectName("databaseBackBtn")
        self.databaseBackBtn.setIcon(icon)
        self.databaseBackBtn.setIconSize(QSize(30, 30))

        self.gridLayout_5.addWidget(self.databaseBackBtn, 0, 0, 1, 1, Qt.AlignLeft)

        self.stackedWidget.addWidget(self.page_database)
        self.page_table = QWidget()
        self.page_table.setObjectName("page_table")
        self.gridLayout_6 = QGridLayout(self.page_table)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tableView = QTableView(self.page_table)
        self.tableView.setObjectName("tableView")
        self.tableView.setFont(font1)
        self.tableView.setStyleSheet(
            "QTableView{\n"
            "	border-radius:25px;\n"
            "}\n"
            "QHeaderView{\n"
            '	font: 700 15pt "Segoe UI";\n'
            "	border-radius: 10px;\n"
            "	background-color: rgb(45, 40, 93);\n"
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
            ""
        )

        self.gridLayout_6.addWidget(self.tableView, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_9 = QLabel(self.page_table)
        self.label_9.setObjectName("label_9")
        self.label_9.setFont(font2)

        self.horizontalLayout.addWidget(self.label_9, 0, Qt.AlignLeft)

        self.checkBox = QCheckBox(self.page_table)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setFont(font2)
        self.checkBox.setIconSize(QSize(30, 30))
        self.checkBox.setChecked(True)
        self.checkBox.setTristate(False)

        self.horizontalLayout.addWidget(self.checkBox, 0, Qt.AlignRight)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.gridLayout_6.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.tableBackBtn = QPushButton(self.page_table)
        self.tableBackBtn.setObjectName("tableBackBtn")
        self.tableBackBtn.setMaximumSize(QSize(34, 30))
        self.tableBackBtn.setIcon(icon)
        self.tableBackBtn.setIconSize(QSize(30, 30))

        self.gridLayout_6.addWidget(self.tableBackBtn, 0, 0, 1, 1)

        self.tableNextBtn = QPushButton(self.page_table)
        self.tableNextBtn.setObjectName("tableNextBtn")
        self.tableNextBtn.setMinimumSize(QSize(140, 40))
        self.tableNextBtn.setFont(font2)

        self.gridLayout_6.addWidget(self.tableNextBtn, 3, 0, 1, 1, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page_table)
        self.page_summery = QWidget()
        self.page_summery.setObjectName("page_summery")
        self.summeryBackBtn = QPushButton(self.page_summery)
        self.summeryBackBtn.setObjectName("summeryBackBtn")
        self.summeryBackBtn.setGeometry(QRect(10, 20, 41, 29))
        self.summeryBackBtn.setIcon(icon)
        self.summeryBackBtn.setIconSize(QSize(30, 30))
        self.pushButton_2 = QPushButton(self.page_summery)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QRect(290, 500, 140, 40))
        self.pushButton_2.setMinimumSize(QSize(140, 40))
        self.pushButton_2.setFont(font2)
        self.stackedWidget.addWidget(self.page_summery)

        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setPointSize(28)
        font3.setBold(True)
        self.label_2.setFont(font3)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1, Qt.AlignHCenter)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1, Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.lineEdit_host.returnPressed.connect(self.hostNextBtn.click)
        self.lineEdit_userName.returnPressed.connect(self.lineEdit_password.setFocus)
        self.lineEdit_password.returnPressed.connect(self.credentialNextBtn.click)
        self.lineEdit_database.returnPressed.connect(self.databaseNextBtn.click)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.label_3.setText("")
        self.getStartBtn.setText(
            QCoreApplication.translate("MainWindow", "Get Start", None)
        )
        self.label_4.setText(QCoreApplication.translate("MainWindow", "Host", None))
        self.lineEdit_host.setText(
            QCoreApplication.translate("MainWindow", "localhost", None)
        )
        self.lineEdit_host.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "127.0.0.1", None)
        )
        self.hostNextBtn.setText(QCoreApplication.translate("MainWindow", "Next", None))
        self.hostBackBtn.setText("")
        self.label_7.setText(
            QCoreApplication.translate("MainWindow", "Credentials", None)
        )
        self.credentialNextBtn.setText(
            QCoreApplication.translate("MainWindow", "Next", None)
        )
        self.label_5.setText(
            QCoreApplication.translate("MainWindow", "User Name", None)
        )
        self.lineEdit_userName.setText(
            QCoreApplication.translate("MainWindow", "root", None)
        )
        self.label_6.setText(QCoreApplication.translate("MainWindow", "Password", None))
        self.lineEdit_password.setText(
            QCoreApplication.translate("MainWindow", "master123@Umansha", None)
        )
        self.credentialBackBtn.setText("")
        self.lineEdit_database.setText(
            QCoreApplication.translate("MainWindow", "store", None)
        )
        self.label_8.setText(QCoreApplication.translate("MainWindow", "Database", None))
        self.databaseNextBtn.setText(
            QCoreApplication.translate("MainWindow", "Next", None)
        )
        self.databaseBackBtn.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", "ALL", None))
        self.checkBox.setText("")
        self.tableBackBtn.setText("")
        self.tableNextBtn.setText(
            QCoreApplication.translate("MainWindow", "Next", None)
        )
        self.summeryBackBtn.setText("")
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", "Finished", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", "PyClassDB", None)
        )
        self.label.setText(
            QCoreApplication.translate("MainWindow", "All Right Reserved @ 2023", None)
        )

    # retranslateUi
