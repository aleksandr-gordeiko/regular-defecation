#!/usr/bin/python3

from typing import Callable

import PyQt6.Qt6 as Qt
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QColorConstants
from PyQt6.QtWidgets import QTextEdit, QVBoxLayout, QWidget


class CountdownTimer(QWidget):
    def __init__(self, timeout_sec: int, timeout_cb: Callable[[None], None], parent: QWidget):
        super().__init__(parent)
        
        self.timeout_sec = timeout_sec
        self.timeout_cb = timeout_cb

        self.__widgets_setup()
        self.__timer_setup()

        self.__update_time()

    def reset(self):
        self.timer.stop()
        self.left_sec = self.timeout_sec
        self.timer.start(1000)
        self.__update_time()
    
    def set_time(self, time_sec: int):
        self.left_sec = time_sec

    def __update_time(self):
        total_seconds = min(self.left_sec, 359940)  # Max time: 99:59:00
        hours = total_seconds // 3600
        total_seconds = total_seconds - (hours * 3600)
        minutes = total_seconds // 60
        seconds = total_seconds - (minutes * 60)
        self.displayArea.setText("{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds)))
        self.displayArea.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
    def __countdown_step(self):
        if self.left_sec > 0:
            self.left_sec -= 1
        if self.left_sec == 0:
            self.timer.stop()
            self.timeout_cb()
        self.__update_time()
        
    def __timer_setup(self):
        self.left_sec = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.__countdown_step)

    def __widgets_setup(self):
        self.displayArea = QTextEdit()
        self.displayArea.setTextColor(QColorConstants.DarkBlue)
        self.displayArea.setStyleSheet("border: none")
        self.displayArea.setFontFamily("Arial")
        self.displayArea.setFontPointSize(55)
        self.displayArea.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.displayArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.displayArea)
        self.setLayout(vbox)
