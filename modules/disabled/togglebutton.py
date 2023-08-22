from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.togglebutton import ToggleButton


class Plugin(MDBoxLayout):
    def __init__(self, **kwargs):
        super(Plugin, self).__init__(**kwargs)
        self.orientation = "horizontal"
        self.add_widget(ToggleButton(text="Male", group="sex"))
        self.add_widget(ToggleButton(text="Female", group="sex"))
        self.add_widget(ToggleButton(text="Mixed", group="sex"))
