from kivymd.app import MDApp
from mainwindow import MainWindow
import sys


sys.path.append('./modules')


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return MainWindow()


    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            "Orange" if self.theme_cls.primary_palette == "Red" else "Red"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )


if __name__ == '__main__':
    MainApp().run()
