from kivymd.app import MDApp
from mainwindow import MainWindow


class MainApp(MDApp):
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    MainApp().run()
