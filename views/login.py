# the ui file and logic for the login page
from PyQt5.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel
)

class Login(QWidget):
    def __init__(self):
        super().__init__()

        top = QVBoxLayout()
        bottom = QHBoxLayout()

        layout = QVBoxLayout()

        icon = QLabel("Hey, Welcome! Please login")
        title = QLabel("LOGIN")

        top.addWidget(icon)
        top.addWidget(title)

        self.setLayout(top)