#!/usr/bin/python3

import sys
import random
import os
from typing import List, Optional

from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtWidgets import QApplication

from main_window import MainWindow
from tray import Tray
from popup_window import PopupWindow

class App(QApplication):
    def __init__(self, argv: List[str]):
        super().__init__(argv)
        self.setQuitOnLastWindowClosed(False)
    
        self.main_win = MainWindow(5, self.__timeout_action, self.__activate_extended_mode)
        self.main_win.show()
        
        self.tray = Tray(window=self.main_win)
        self.tray.trigger_quit_visibility(False)
        self.tray.show()
        
        self.sound_dir = "resources/sounds/failure/"
        self.failure_sound = QSoundEffect()
        
        sys.exit(self.exec())

    def __activate_extended_mode(self):
        self.tray.trigger_quit_visibility(True)
    
    def __timeout_action(self):
        self.main_win.showNormal()
        self.popup = PopupWindow()
        self.popup.show()
        self.__play_failure_sound()
    
    def __play_failure_sound(self):
        self.failure_sound.setSource(QUrl.fromLocalFile(
            self.sound_dir + self.get_random_filename(self.sound_dir)
        ))
        self.failure_sound.play()
    
    @staticmethod
    def get_random_filename(directory: str) -> Optional[str]:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        if not files:
            return None
        return random.choice(files)



def main():
    app = App(sys.argv)


if __name__ == "__main__":
    main()
