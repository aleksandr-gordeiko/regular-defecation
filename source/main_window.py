#!/usr/bin/python3

from typing import Callable

from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QSize, Qt, QUrl
from PyQt6.QtGui import QGuiApplication, QShortcut, QKeySequence
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QSystemTrayIcon

from timer import CountdownTimer

class MainWindow(QMainWindow):
    def __init__(self, timeout_sec: int, timeout_cb: Callable[[None], None], magic_sequence_cb: Callable[[None], None]):
        super().__init__()
        self.magic_sequence_cb = magic_sequence_cb
        self.timeout_cb = timeout_cb
        self.__window_setup()
        self.__widgets_setup(timeout_sec)
        
        self.magic_sequence = QShortcut(QKeySequence("Ctrl+Shift+Alt+N"), self)
        self.magic_sequence.activated.connect(self.__magic_sequence_cb)
        
        self.fart_sound = QSoundEffect()
        self.fart_sound.setSource(QUrl.fromLocalFile("./resources/sounds/fart/fart-with-reverb-39675.wav"))
    
    def __magic_sequence_cb(self):
        self.timer.set_time(15)
        self.magic_sequence_cb()
    
    def closeEvent(self, event):
        event.ignore()
        self.hide()
    
    def restore(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.showNormal()
    
    def __play_sound(self):
        self.fart_sound.play()
        
    def __timer_cb(self):
        self.timeout_cb()
        self.timer.reset()
    
    def __timer_reset_action(self):
        self.timer.reset()
        self.__play_sound()
    
    def __window_setup(self):
        self.setWindowTitle("РЕГУЛЯРНАЯ ДЕФЕКАЦИЯ")
        self.setFixedSize(QSize(600, 400))
        self.__center()
        self.setStyleSheet("background-color: white;")
        
    def __center(self):
        qr=self.frameGeometry()           
        cp=QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def __widgets_setup(self, timeout_sec: int):
        root_widget = QWidget()
        self.setCentralWidget(root_widget)
        vbox = QVBoxLayout()
        root_widget.setLayout(vbox)
        
        self.timer_label = QLabel()
        self.timer_label.setText("КАЛОВЫЙ ВЗРЫВ ЧЕРЕЗ")
        self.timer_label.setStyleSheet("color: red;\
                                  font-family: arial;\
                                  font-size: 40px")
        vbox.addWidget(self.timer_label)
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
        self.timer = CountdownTimer(timeout_sec, self.__timer_cb, parent=self)
        self.timer.reset()
        vbox.addWidget(self.timer)
        
        self.defecate_btn = QPushButton("ПОСРАТЬ С КАЙФОМ")
        self.defecate_btn.setStyleSheet("background-color: green;\
                                         color: yellow;\
                                         font-size: 30px")
        self.defecate_btn.clicked.connect(self.__timer_reset_action)
        vbox.addWidget(self.defecate_btn)
