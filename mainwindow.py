from kivy.uix.behaviors import DragBehavior
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.slider import MDSlider
from kivy.lang import Builder


Builder.load_file("kv/mainwindow.kv")


class MainWindow(MDFloatLayout):
    pass


class WidgetContainer(DragBehavior, MDBoxLayout):
    pass


class ButtonWidget(MDBoxLayout):
    pass


class WidgetSlider(MDBoxLayout):
    pass
