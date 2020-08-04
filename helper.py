slave_helper = """
MDTextField:
    hint_text: "Enter register"
    helper_text: "or click on forgot register"
    helper_text_mode: "on_focus"
    
    pos_hint: {'center_x': 0.5, 'center_y':0.8}
    size_hint_x: None
    width: 300
"""

register_helper = """
MDTextField:
    hint_text: "Enter TypeInput"
    helper_text: "or click on forgot TypeInput"
    helper_text_mode: "on_focus"
    
    pos_hint: {'center_x': 0.5, 'center_y':0.7}
    size_hint_x: None
    width: 300
"""

datatype_helper = '''
Screen:
    MDTextField:
        id: field
        pos_hint: {'center_x': .5, 'center_y': .6}
        size_hint_x: None
        width: 300
        hint_text: "Choose Datatype"
        on_focus: if self.focus: app.menu.open()
'''

readtype_helper = '''
Screen:
    MDTextField:
        id: field
        pos_hint: {'center_x': .5, 'center_y': .5}
        size_hint_x: None
        width: 300
        hint_text: "Choose readtype"
        on_focus: if self.focus: app.menu.open()
'''