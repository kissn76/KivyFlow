from kivy.uix.behaviors import DragBehavior
from kivy.core.window import Window
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.scrollview import MDScrollView
from kivy.lang import Builder


Builder.load_file("kv/mainwindow.kv")


class MainWindow(MDFloatLayout):
    Window.set_system_cursor('arrow')


class WidgetContainer(DragBehavior, MDBoxLayout):
    def __init__(self, **kwargs):
        super(WidgetContainer, self).__init__(**kwargs)
        self.titlebar_height = 24
        self.middlewidget_width = 6
        self.resize_border_width = 6


    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return super(WidgetContainer, self).on_touch_up(touch)

        delta_w = self.resize_border_width
        delta_h = self.titlebar_height

        if touch.button == 'left':
            edit_type = 'pos'
            xx, yy = self.to_widget(*touch.pos, relative=True)
            if self.width - xx < delta_w and self.height - yy < delta_h:
                edit_type = 'right'
            touch.ud['edit_type'] = edit_type

            if edit_type != 'pos':
                touch.ud['size_node'] = self
                return True

        return super(WidgetContainer, self).on_touch_down(touch)


    def on_touch_move(self, touch):
        if 'size_node' in touch.ud.keys():
            if touch.ud['size_node'] == self:
                xx, yy = self.to_widget(*touch.pos, relative=True)
                if touch.ud['edit_type'] == 'right':
                    self.do_right_size(xx, yy)
                return True

        return super(WidgetContainer, self).on_touch_move(touch)


    def on_touch_up(self, touch):
        return super(WidgetContainer, self).on_touch_up(touch)


    def do_right_size(self, xx, yy):
        if xx > 0:
            if self.size_hint_x is None:
                self.width = xx
            else:
                self.size_hint_x = xx / self.parent.width


class WidgetMover(HoverBehavior, MDLabel):
    def on_enter(self, *args):
        Window.set_system_cursor('crosshair')

    def on_leave(self, *args):
        Window.set_system_cursor('arrow')


class WidgetResizer(HoverBehavior, MDLabel):
    def on_enter(self, *args):
        Window.set_system_cursor('size_we')

    def on_leave(self, *args):
        Window.set_system_cursor('arrow')


class WidgetOutput(MDBoxLayout):
    pass


class SliderWidget(MDBoxLayout):
    dialog = None

    def show_alert_dialog(self):

        def close_dialog(obj):
            self.dialog.dismiss()

        def use_input(obj):
            self.ids.slider.min = float(self.dialog.content_cls.ids.min_value.text)
            self.ids.slider.max = float(self.dialog.content_cls.ids.max_value.text)
            self.ids.slider.step = float(self.dialog.content_cls.ids.step_value.text)

        if not self.dialog:
            self.dialog = MDDialog(
                type="custom",
                content_cls=SliderConfig(min=self.ids.slider.min, max=self.ids.slider.max, step=self.ids.slider.step),
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


class SliderConfig(MDBoxLayout):
    def __init__(self, min, max, step, **kwargs):
        super(SliderConfig, self).__init__(**kwargs)
        self.ids.min_value.text = str(min)
        self.ids.max_value.text = str(max)
        self.ids.step_value.text = str(step)
