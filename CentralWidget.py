from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QPushButton, QLineEdit, QTextBrowser, QVBoxLayout, QGridLayout, QLabel


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.__login = QPushButton("Login")
        self.__logout = QPushButton("Logout")

        self.__benutzername = QLabel("Benutzername")
        self.__passwort = QLabel("Passwort")
        self.__token = QLabel("Token")



        self.__line_edit = QLineEdit()
        #Platzhalter um vor der ersten eingabe
        self.__line_edit.setPlaceholderText("max_power")


        self.__line_edit_pw = QLineEdit()

        self.__line_edit_token = QLineEdit()

        self.__text_browser = QTextBrowser()



        layout = QGridLayout()
        layout.addWidget(self.__benutzername, 0, 0)
        layout.addWidget(self.__line_edit, 0, 1, 1, 10)
        layout.addWidget(self.__passwort, 1, 0)
        layout.addWidget(self.__line_edit_pw, 1, 1, 1, 10)
        layout.addWidget(self.__token, 2, 0)
        layout.addWidget(self.__line_edit_token, 2, 1, 1, 10)
        layout.addWidget(self.__login, 3, 0)
        layout.addWidget(self.__logout, 3, 1, 1, 10)

        # Ergebnisfeld
        layout.addWidget(self.__text_browser, 4, 0, 6, 11)


        self.setLayout(layout)










    '''
    
    @pyqtSlot()
    def append(self):
        text = self.__line_edit.text()

        self.__text_browser.append(text)

    @pyqtSlot()
    def set_text(self):
        text = self.__line_edit.text()

        self.__text_browser.setText(text)

    @pyqtSlot()
    def clear(self):
        self.__text_browser.clear()

    @pyqtSlot()
    def backward(self):
        self.__text_browser.undo()

    
    '''
