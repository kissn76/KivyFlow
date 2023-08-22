from kivy.uix.behaviors import DragBehavior
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.core.window import Window


Builder.load_file("widgetcontainer.kv")


class WidgetContainer(DragBehavior, MDBoxLayout):
    def __init__(self, **kwargs):
        self.titlebar_height = 24
        self.middlewidget_width = 6
        self.resize_border_width = 6
        super(WidgetContainer, self).__init__(**kwargs)


    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return super(WidgetContainer, self).on_touch_up(touch)

        if touch.button == 'left':
            edit_type = 'pos'
            xx, yy = self.to_widget(*touch.pos, relative=True)
            if self.width - xx < self.resize_border_width and self.height - yy < self.titlebar_height:
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
