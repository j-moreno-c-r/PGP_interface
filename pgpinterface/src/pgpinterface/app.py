"""
a simple pgp interface in python for messages 
"""
from .resources.tk_main_files.tk_main_menu import create_main_menu
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class pgpinterface(toga.App):
    def startup(self):
        create_main_menu()
        main_box = toga.Box()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return pgpinterface()
