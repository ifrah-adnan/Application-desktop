import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QBoxLayout
from PyQt5.uic import loadUi
from menu import Ui_Menu

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login3.ui",self)
        self.pushButton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        

    def loginfunction(self):
         email=self.user.text()
         password=self.password.text()
         if email =='admin' and password=='admin123':
         
            self.MainWindow1 = QtWidgets.QMainWindow()

            self.ui = Ui_Menu()
            self.ui.setupUi(self.MainWindow1)
            self.MainWindow1.show()

         else :

            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Critical)
            message_box.setText("User or password invalid")
            message_box.setWindowTitle("Erreur")
            message_box.exec_()













    



app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(740)
widget.setFixedHeight(740)
widget.show()
app.exec_()