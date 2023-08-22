from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField, MDTextFieldRect


class Plugin(MDBoxLayout):
    def __init__(self, **kwargs):
        super(Plugin, self).__init__(**kwargs)
        self.orientation = "horizontal"
        self.add_widget(MDTextField())
