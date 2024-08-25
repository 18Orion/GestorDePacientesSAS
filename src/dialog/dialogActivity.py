# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QDialog
from src.dialog.dialogUI import Ui_Dialog

class dialogActivity(QDialog):
    def __init__(self, message, onCloseFunc=None,parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.onCloseFunc=onCloseFunc
        self.ui.setupUi(self)
        self.ui.advise.setText(message)
        self.ui.okButton.clicked.connect(self.closeDialog)
        self.show()

    def closeDialog(self):
        if self.onCloseFunc:
            self.onCloseFunc()
        self.close()
