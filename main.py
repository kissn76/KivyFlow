from kivymd.app import MDApp
from mainwindow import MainWindow
import sys


sys.path.append('./modules')


class MainApp(MDApp):
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    MainApp().run()
