from PyQt5.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QVBoxLayout, 
    QHBoxLayout,
    QLabel,
    QWidget, 
    QPushButton
)
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
import sys
from views.login import Login


class Contacts(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contacts Manager")

        self.setFixedSize(QSize(560, 400))
        # set app icon
        self.setWindowIcon(QIcon('images/icons/app-icon.png'))
        self.setStyleSheet("background: #ffffff; font-size: 16px; color: #20303f")

        layout = QVBoxLayout()
        btn = QPushButton("Click Me!")
        btn.clicked.connect(self.hide_login)

        layout.addWidget(btn)


        self.login = Login()
        layout.addWidget(self.login)

        widget = QWidget()
        widget.setStyleSheet(open("styles/default.css").read())

        widget.setLayout(layout)

        self.setCentralWidget(widget)
    
    def hide_login(self):
        self.login.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Contacts()
    window.show()
    app.exec_()