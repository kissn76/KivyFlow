from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from modules.default import *


Builder.load_file("mainwindow.kv")


class MainWindow(MDBoxLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        Window.set_system_cursor('arrow')

        # self.wc = WidgetContainer()
        # self.ids.mainlayout.add_widget(self.wc)
