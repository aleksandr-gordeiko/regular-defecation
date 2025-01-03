#!/usr/bin/python3



from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout

class PopupWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)
        
        self.image_label = QLabel()
        image = QPixmap("resources/images/poop_realistic.png")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setPixmap(image)
        self.vbox.addWidget(self.image_label)
        
        self.status_label = QLabel("ВЫ ОБОСРАЛИСЬ")
        self.status_label.setStyleSheet("color: black;\
                                         font-family: \"Comic Sans MS\";\
                                         font-size: 70px")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vbox.addWidget(self.status_label)
        
        self.showFullScreen()
    