import kivy
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock

from helper import slave_helper
from helper import register_helper
from helper import datatype_helper
from helper import readtype_helper
    

screen_helper ="""
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Application'

        MDBottomNavigation:
                
                    
"""
class DemoApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.datatype = Builder.load_string(datatype_helper)
        x = ("float","uint")
        menu_items = [{"text": f"{x[i]}"} for i in range(len(x))]
        self.menu = MDDropdownMenu(
            caller=self.datatype.ids.field,
            items=menu_items,
            position="bottom",
            callback= self.set_datatype,
            width_mult=4,
        )
    

        
    def set_datatype(self, instance):
        def set_datatype(terval):
            self.datatype.ids.field.text = instance.text
            self.menu.dismiss()
        Clock.schedule_once(set_datatype, 0.5)
        
    def set_readtype(self, texttype):
        def set_readtype(interval):
            self.datatype.ids.field.text = texttype.text
            self.menu.dismiss()
        Clock.schedule_once(set_readtype, 0.5)

    def build(self):
        self.theme_cls.primary_palette = 'Green'
        screen = Builder.load_string(screen_helper)
        button = MDRectangleFlatButton(text = 'show',pos_hint = {'center_x': 0.5, 'center_y':0.3},
                                        on_release = self.show_data )
        
        self.slave = Builder.load_string(slave_helper)
        self.register = Builder.load_string(register_helper)
        
        screen.add_widget(self.slave)
        screen.add_widget(self.register)
        screen.add_widget(self.datatype)
##        screen.add_widget(self.readtype)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        print(self.slave.text)
        print(self.register.text)
        print(self.datatype.ids.field.text)
##        print(self.readtype.ids.field.text)
        
    


DemoApp().run()
