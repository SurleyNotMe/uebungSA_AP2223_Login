from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QPushButton, QLineEdit, QTextBrowser, QVBoxLayout, QGridLayout, QLabel

# Definiere die Daten direkt als Klassenvariable
ERWARTETE_BENUTZERDATEN = {
    "benutzername": "MaxMustermann",
    "kennwort": "SicheresPasswort123",
    "token": "AFFE"
}


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.__login = QPushButton("Login")
        self.__login.clicked.connect(self.check_login)

        self.__logout = QPushButton("Logout")
        self.__logout.setEnabled(False)

        self.__benutzername = QLabel("Benutzername")
        self.__passwort = QLabel("Passwort")
        self.__token = QLabel("Token")



        self.__line_edit = QLineEdit()
        #Platzhalter um vor der ersten eingabe was zu haben
        self.__line_edit.setPlaceholderText("max_power")


        self.__line_edit_pw = QLineEdit()
        #Echomode Passwort zwischen speichern zu verbergen
        self.__line_edit_pw.setEchoMode(QLineEdit.EchoMode.Password)


        self.__line_edit_token = QLineEdit()
        #Erlaubt als Eingabe 4 Hexadezimalzahlen
        self.__line_edit_token.setInputMask("HHHH")


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


    @pyqtSlot()
    def check_login(self):
        """Simuliert den Login-Prozess und aktiviert/deaktiviert die Buttons."""

        # 1. Eingabewerte aus den QLineEdit-Feldern abrufen
        benutzername = self.__line_edit.text()
        kennwort = self.__line_edit_pw.text()
        token = self.__line_edit_token.text()

        # 2. Prüfen, ob ALLE DREI Werte korrekt sind (mit 'and')
        # Die Zeilenumbrüche (\) dienen nur der besseren Lesbarkeit.
        if benutzername == ERWARTETE_BENUTZERDATEN["benutzername"] and \
                kennwort == ERWARTETE_BENUTZERDATEN["kennwort"] and \
                token == ERWARTETE_BENUTZERDATEN["token"]:

            # Login erfolgreich
            self.__login.setEnabled(False)
            self.__logout.setEnabled(True)
            self.__text_browser.append("🟢 Login erfolgreich. Logout ist nun möglich.")
        else:
            # Login fehlgeschlagen
            self.__text_browser.append("🔴 Login fehlgeschlagen. Bitte Eingaben prüfen.")

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
