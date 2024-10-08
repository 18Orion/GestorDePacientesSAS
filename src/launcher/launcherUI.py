# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'launcherUI.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_launcher(object):
    def setupUi(self, launcher):
        if not launcher.objectName():
            launcher.setObjectName(u"launcher")
        launcher.resize(672, 692)
        self.formLayoutWidget = QWidget(launcher)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.juntaAnd = QLabel(self.formLayoutWidget)
        self.juntaAnd.setObjectName(u"juntaAnd")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.juntaAnd.sizePolicy().hasHeightForWidth())
        self.juntaAnd.setSizePolicy(sizePolicy)
        self.juntaAnd.setMaximumSize(QSize(150, 150))
        self.juntaAnd.setFrameShape(QFrame.Box)
        self.juntaAnd.setText(u"")
        self.juntaAnd.setPixmap(QPixmap(u"../assets/logo.jpg"))
        self.juntaAnd.setScaledContents(True)
        self.juntaAnd.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.juntaAnd)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.greeting = QLabel(self.formLayoutWidget)
        self.greeting.setObjectName(u"greeting")

        self.verticalLayout.addWidget(self.greeting)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label_5)

        self.version = QLabel(self.formLayoutWidget)
        self.version.setObjectName(u"version")

        self.horizontalLayout.addWidget(self.version)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.formLayout.setItem(3, QFormLayout.SpanningRole, self.verticalSpacer_2)

        self.patientLabel = QLabel(self.formLayoutWidget)
        self.patientLabel.setObjectName(u"patientLabel")

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.patientLabel)

        self.patientUILaunch = QPushButton(self.formLayoutWidget)
        self.patientUILaunch.setObjectName(u"patientUILaunch")

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.patientUILaunch)

        self.exportUILaunch = QPushButton(self.formLayoutWidget)
        self.exportUILaunch.setObjectName(u"exportUILaunch")

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.exportUILaunch)

        self.equipmentLaunch = QPushButton(self.formLayoutWidget)
        self.equipmentLaunch.setObjectName(u"equipmentLaunch")
        self.equipmentLaunch.setEnabled(True)

        self.formLayout.setWidget(9, QFormLayout.SpanningRole, self.equipmentLaunch)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.formLayout.setItem(11, QFormLayout.SpanningRole, self.verticalSpacer)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(12, QFormLayout.SpanningRole, self.label_4)

        self.changeCredentialsUILaunch = QPushButton(self.formLayoutWidget)
        self.changeCredentialsUILaunch.setObjectName(u"changeCredentialsUILaunch")
        self.changeCredentialsUILaunch.setEnabled(True)

        self.formLayout.setWidget(13, QFormLayout.SpanningRole, self.changeCredentialsUILaunch)

        self.userCreatorLaunch = QPushButton(self.formLayoutWidget)
        self.userCreatorLaunch.setObjectName(u"userCreatorLaunch")

        self.formLayout.setWidget(14, QFormLayout.SpanningRole, self.userCreatorLaunch)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.formLayout.setItem(15, QFormLayout.SpanningRole, self.verticalSpacer_3)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(16, QFormLayout.SpanningRole, self.label_7)

        self.update = QPushButton(self.formLayoutWidget)
        self.update.setObjectName(u"update")
        self.update.setEnabled(True)

        self.formLayout.setWidget(17, QFormLayout.SpanningRole, self.update)

        self.about = QPushButton(self.formLayoutWidget)
        self.about.setObjectName(u"about")
        self.about.setEnabled(True)

        self.formLayout.setWidget(18, QFormLayout.SpanningRole, self.about)

        self.useInfo = QHBoxLayout()
        self.useInfo.setObjectName(u"useInfo")
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.useInfo.addWidget(self.label)

        self.name = QLabel(self.formLayoutWidget)
        self.name.setObjectName(u"name")
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)

        self.useInfo.addWidget(self.name)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.useInfo.addItem(self.horizontalSpacer)

        self.logOut = QPushButton(self.formLayoutWidget)
        self.logOut.setObjectName(u"logOut")

        self.useInfo.addWidget(self.logOut)


        self.formLayout.setLayout(1, QFormLayout.SpanningRole, self.useInfo)

        self.equipmentLabel = QLabel(self.formLayoutWidget)
        self.equipmentLabel.setObjectName(u"equipmentLabel")

        self.formLayout.setWidget(8, QFormLayout.SpanningRole, self.equipmentLabel)

        self.launchEquipmentRegistration = QPushButton(self.formLayoutWidget)
        self.launchEquipmentRegistration.setObjectName(u"launchEquipmentRegistration")

        self.formLayout.setWidget(10, QFormLayout.SpanningRole, self.launchEquipmentRegistration)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.formLayout.setItem(7, QFormLayout.SpanningRole, self.verticalSpacer_4)

        launcher.setCentralWidget(self.formLayoutWidget)
        self.statusbar = QStatusBar(launcher)
        self.statusbar.setObjectName(u"statusbar")
        launcher.setStatusBar(self.statusbar)

        self.retranslateUi(launcher)

        QMetaObject.connectSlotsByName(launcher)
    # setupUi

    def retranslateUi(self, launcher):
        launcher.setWindowTitle(QCoreApplication.translate("launcher", u"Men\u00fa", None))
        self.greeting.setText("")
        self.label_5.setText(QCoreApplication.translate("launcher", u"Versi\u00f3n:", None))
        self.version.setText("")
        self.patientLabel.setText(QCoreApplication.translate("launcher", u"Herramientas del paciente", None))
        self.patientUILaunch.setText(QCoreApplication.translate("launcher", u"Ficha de paciente", None))
        self.exportUILaunch.setText(QCoreApplication.translate("launcher", u"Exportar datos", None))
        self.equipmentLaunch.setText(QCoreApplication.translate("launcher", u"Seguimiento de equipos", None))
        self.label_4.setText(QCoreApplication.translate("launcher", u"Herramientas de administraci\u00f3n", None))
        self.changeCredentialsUILaunch.setText(QCoreApplication.translate("launcher", u"Cambiar credenciales", None))
        self.userCreatorLaunch.setText(QCoreApplication.translate("launcher", u"Creador de usuario", None))
        self.label_7.setText(QCoreApplication.translate("launcher", u"Herramientas del programa", None))
        self.update.setText(QCoreApplication.translate("launcher", u"Buscar \u00faltima versi\u00f3n", None))
        self.about.setText(QCoreApplication.translate("launcher", u"Sobre el programa", None))
        self.label.setText(QCoreApplication.translate("launcher", u"Has iniciado sesi\u00f3n como:", None))
        self.name.setText(QCoreApplication.translate("launcher", u"user", None))
        self.logOut.setText(QCoreApplication.translate("launcher", u"Cerrar sesi\u00f3n", None))
        self.equipmentLabel.setText(QCoreApplication.translate("launcher", u"Administraci\u00f3n de equipos", None))
        self.launchEquipmentRegistration.setText(QCoreApplication.translate("launcher", u"Registrar equipo", None))
    # retranslateUi

