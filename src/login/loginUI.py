# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginUI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(578, 147)
        self.formLayoutWidget = QWidget(login)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(2, 2, 2, 2)
        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_3)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.user = QLineEdit(self.formLayoutWidget)
        self.user.setObjectName(u"user")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.user)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.password = QLineEdit(self.formLayoutWidget)
        self.password.setObjectName(u"password")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.password)

        self.logIn = QPushButton(self.formLayoutWidget)
        self.logIn.setObjectName(u"logIn")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.logIn)

        login.setCentralWidget(self.formLayoutWidget)

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Inicio de sesi\u00f3n", None))
        self.label_3.setText(QCoreApplication.translate("login", u"Inicio de sesi\u00f3n en el sistema", None))
        self.label.setText(QCoreApplication.translate("login", u"Usuario", None))
        self.label_2.setText(QCoreApplication.translate("login", u"Contrase\u00f1a: ", None))
        self.logIn.setText(QCoreApplication.translate("login", u"Iniciar sesi\u00f3n", None))
    # retranslateUi

