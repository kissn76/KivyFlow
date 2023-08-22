from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.slider import MDSlider


class Plugin(MDBoxLayout):
    def __init__(self, **kwargs):
        super(Plugin, self).__init__(**kwargs)
        self.orientation = "horizontal"
        self.add_widget(MDSlider(min=0, max=100, step=0.1, hint=False))
