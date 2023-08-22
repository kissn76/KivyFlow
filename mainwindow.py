from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.lang import Builder
from widgetcontainer import *
from module import Module


Builder.load_file("mainwindow.kv")


class MainWindow(MDBoxLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        Window.set_system_cursor('arrow')
        self.module = Module()

        for module_name in self.module.list_modules():
            self.add_module(module_name)


    def add_new_widget(self, module_name):
        self.wc = WidgetContainer(pos=(0, 0))
        self.ids.mainlayout.add_widget(self.wc)
        self.wc.add_widget(self.module.new_object(module_name=module_name))


    def add_module(self, module_name):
        rb = MDRaisedButton(text=module_name)
        rb.bind(on_press=lambda x: self.add_new_widget(module_name))
        self.ids.modulelist.add_widget(rb)
