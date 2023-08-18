from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog


class SliderWidget(MDBoxLayout):
    dialog = None

    def show_config_dialog(self):

        def close_dialog(obj):
            self.dialog.dismiss()

        def use_input(obj):
            self.ids.slider.min = float(self.dialog.content_cls.ids.min_value.text)
            self.ids.slider.max = float(self.dialog.content_cls.ids.max_value.text)
            self.ids.slider.step = float(self.dialog.content_cls.ids.step_value.text)

        if not self.dialog:
            self.dialog = MDDialog(
                size_hint=[0.9, None],
                title="Settings",
                type="custom",
                content_cls=SliderWidgetConfig(min=self.ids.slider.min, max=self.ids.slider.max, step=self.ids.slider.step),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        on_press = close_dialog,
                    ),
                    MDFlatButton(
                        text="DISCARD",
                        on_press = use_input,
                    ),
                ],
            )
        self.dialog.open()


class SliderWidgetConfig(MDBoxLayout):
    def __init__(self, min, max, step, **kwargs):
        super(SliderWidgetConfig, self).__init__(**kwargs)
        self.ids.min_value.text = str(min)
        self.ids.max_value.text = str(max)
        self.ids.step_value.text = str(step)
