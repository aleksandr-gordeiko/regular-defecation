#!/usr/bin/python3

from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QSystemTrayIcon, QMenu, QApplication, QMainWindow

from main_window import MainWindow

class Tray(QSystemTrayIcon):
    def __init__(self, window: MainWindow):
        super().__init__()
        self.window = window
        self.__ui_setup()
        self.__menu_setup()
        
        self.activated.connect(self.window.restore)
    
    def trigger_quit_visibility(self, state: bool):
        self.quit_action.setEnabled(state)
        
    def __menu_setup(self):
        self.menu = QMenu()
        
        self.quit_action = QAction("Выйти", self)
        self.quit_action.triggered.connect(QApplication.quit)
        self.menu.addAction(self.quit_action)
        
        self.setContextMenu(self.menu)
    
    def __ui_setup(self):
        self.setIcon(QIcon("resources/images/poop.png"))
        self.setVisible(True)
