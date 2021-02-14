from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import QSize, Qt
import sys

class Contacts(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contacts Manager")

        self.setFixedSize(QSize(640, 400))

        layout = QVBoxLayout()

        layout.addWidget(QPushButton("Click Me!"))

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Contacts()
    window.show()
    app.exec_()