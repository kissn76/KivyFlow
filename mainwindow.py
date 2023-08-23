from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivy.app import App
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


    def add_new_widget(self, module_name, pos=(100, 200)):
        wc = None
        wc = WidgetContainer(pos=pos)
        self.ids.mainlayout.add_widget(wc)
        self.insert_widget(wc, module_name)


    def insert_widget(self, widget_container, module_name):
        widget_container.add_widget(self.module.new_object(module_name=module_name))


    def add_module(self, module_name):
        self.ids.modulelist.add_widget(ModuleLine(module_name))


class ModuleLine(MDBoxLayout):
    def __init__(self, module_name, **kwargs):
        super(ModuleLine, self).__init__(**kwargs)
        self.text = module_name


    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return super(ModuleLine, self).on_touch_up(touch)
        else:
            if touch.button == 'left':
                touch.ud['add_node'] = self

        return super(ModuleLine, self).on_touch_down(touch)


    def on_touch_move(self, touch):
        # xx, yy = touch.pos
        # if 'add_node' in touch.ud.keys():
        #     if touch.ud['add_node'] == self:
        #         xx, yy = self.to_widget(*touch.pos, relative=True)
        #         if touch.ud['edit_type'] == 'right':
        #             self.do_right_size(xx, yy)
        #         return True

        return super(ModuleLine, self).on_touch_move(touch)


    def on_touch_up(self, touch):
        if 'add_node' in touch.ud.keys():
            if touch.ud['add_node'] == self:
                app = App.get_running_app()
                for widget_container in app.root.ids.mainlayout.children:
                    if widget_container.collide_point(*touch.pos):
                        app.root.insert_widget(widget_container, self.text)
                        return super(ModuleLine, self).on_touch_up(touch)

                if app.root.ids.mainlayout.collide_point(*touch.pos):
                    app.root.add_new_widget(self.text, pos=touch.pos)

        return super(ModuleLine, self).on_touch_up(touch)