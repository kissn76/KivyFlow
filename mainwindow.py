from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from widgetcontainer import *
from module import Module


Builder.load_file("mainwindow.kv")


class MainWindow(MDBoxLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        Window.set_system_cursor('arrow')
        self.module = Module()


    def add_new_widget(self, module_name):
        self.wc = WidgetContainer(pos=(200, 200))
        self.ids.mainlayout.add_widget(self.wc)
        self.wc.add_widget(self.module.new_object(module_name=module_name))

