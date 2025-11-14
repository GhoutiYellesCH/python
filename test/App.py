from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
from kivymd.uix.textfield import MDTextField
from kivy.properties import StringProperty

# Define the KV language string with improved formatting and error correction
screen_helper = """
ScreenManager:
    FirstPage:
    HomePage:
    MaladiePage:
    LangBluetoothPage:
    GuidePage:
    ImportantPage:

<FirstPage>:
    name: 'FirstPage'
    AsyncImage:
        source: "MediTalk3.png"
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        size_hint: (0.6, 0.4)
    MDRectangleFlatButton:
        text: 'Welcome'
        text_color: 'white'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_press: root.manager.current = 'HomePage'
        theme_text_color: 'Custom'
        md_bg_color: 54/255, 79/255, 107/255, 5
        line_color: 0,0,0,0

<HomePage>:
    name: 'HomePage'
    AsyncImage:
        source: "MediTalk4.png"
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        size_hint: (0.6, 0.4)
    MDRectangleFlatButton:
        text: 'Maladie'
        text_color: 'white'
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        on_press: root.manager.current = 'MaladiePage'
        theme_text_color: 'Custom'
        md_bg_color: 54/255, 79/255, 107/255, 5
        line_color: 0,0,0,0
    MDRectangleFlatButton:
        text: 'Connection & Bluetooth'
        text_color: 'white'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press: root.manager.current = 'LangBluetoothPage'
        theme_text_color: 'Custom'
        md_bg_color: 54/255, 79/255, 107/255, 5
        line_color: 0,0,0,0
    MDRectangleFlatButton:
        text: 'Guide'
        text_color: 'white'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_press: root.manager.current = 'GuidePage'
        theme_text_color: 'Custom'
        md_bg_color: 54/255, 79/255, 107/255, 5
        line_color: 0,0,0,0
    MDRectangleFlatButton:
        text: 'Important'
        text_color: 'white'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press: root.manager.current = 'ImportantPage'     
        theme_text_color: 'Custom'
        md_bg_color: 54/255, 79/255, 107/255, 5     
        line_color: 0,0,0,0

<MaladiePage>:
    name: 'MaladiePage'
    MDTextField:
        id: user_input_field  # Assign a unique ID to the text field
        hint_text: "Select le type de Maladie"
        helper_text: "Type N N:1->4"
        helper_text_mode: "on_focus"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width: 300
        max_chars: 6
    MDLabel:
        id: error_label
        text: ""  # Initially empty text
        pos_hint: {'center_x': 0.6, 'y': 0.3}  # Position below the text field
        
        color: (1, 0, 0, 1)  # Set color to red for error indication
        theme_text_color: 'Custom'    
    MDRectangleFlatButton:
        text: 'valider'  # Change the button text to trigger storage
        text_color: 'white'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press: root.store_input()  # Call the function to store input
        theme_text_color: 'Custom'
        md_bg_color: 54/255, 79/255, 107/255, 5     
        line_color: 0,0,0,0
        # ... (rest of button properties)
    MDRectangleFlatButton:
        text: 'Retour'
        text_color: 'white'
        pos_hint: {'center_x': 0.2, 'center_y': 0.2}
        on_press: root.manager.current = 'HomePage'
        theme_text_color: 'Custom'
        md_bg_color: 54/255, 79/255, 107/255, 5
        line_color: 0, 0, 0, 0   

<LangBluetoothPage>:
    name: 'LangBluetoothPage'
    MDRectangleFlatButton:
        text: 'Retour'
        text_color: 'white'
        pos_hint: {'center_x': 0.2, 'center_y': 0.2}
        on_press: root.manager.current = 'HomePage'    
        theme_text_color: 'Custom'
        md_bg_color: 54/255, 79/255, 107/255, 5    
        line_color: 0,0,0,0

<GuidePage>:
    name: 'GuidePage'
    MDRectangleFlatButton:
        text: 'Retour'
        text_color: 'white'
        pos_hint: {'center_x': 0.2, 'center_y': 0.2}
        on_press: root.manager.current = 'HomePage'  
        theme_text_color: 'Custom'
        md_bg_color: 54/255, 79/255, 107/255, 5    
        line_color: 0,0,0,0

<ImportantPage>:
    name: 'ImportantPage'
    MDRectangleFlatButton:
        text: 'Retour'
        text_color: 'white'
        pos_hint: {'center_x': 0.2, 'center_y': 0.2}
        on_press: root.manager.current = 'HomePage'    
        theme_text_color: 'Custom'
        md_bg_color: 54/255, 79/255, 107/255, 5  
        line_color: 0,0,0,0
"""


# Class definitions remain the same
class FirstPage(Screen):
    pass


class HomePage(Screen):
    pass


class MaladiePage(Screen):
    selected_maladie = StringProperty("")  # Property to store user input

    def store_input(self):
        user_input = self.ids.user_input_field.text
        if self.validate_input(user_input):
            self.selected_maladie = user_input
            print(f"Selected Maladie: {self.selected_maladie}")
            self.ids.error_label.text = ""  # Clear error message if input is valid
        else:
            self.ids.error_label.text = "Entrée invalide. Veuillez saisir « Type N », où N est un nombre compris entre 1 et 4."

    def validate_input(self, text):
        return len(text) == 6 and text.startswith("Type ") and text[-1] in "1234"


class LangBluetoothPage(Screen):
    pass


class GuidePage(Screen):
    pass


class ImportantPage(Screen):
    pass


def on_enter(self):
    maladie_page = self.manager.get_screen('MaladiePage')
    selected_maladie = maladie_page.selected_maladie
    print(f"Retrieved Maladie: {selected_maladie}")  # Accessing the stored value


sm = ScreenManager()
sm.add_widget(FirstPage(name='FirstPage'))
sm.add_widget(HomePage(name='HomePage'))
sm.add_widget(MaladiePage(name='MaladiePage'))
sm.add_widget(LangBluetoothPage(name='LangBluetoothPage'))
sm.add_widget(GuidePage(name='GuidePage'))
sm.add_widget(ImportantPage(name='ImportantPage'))


class MediTalk(MDApp):
    def build(self):
        self.icon = "doctor.png"
        screen = Builder.load_string(screen_helper)
        return screen


if __name__ == '__main__':
    MediTalk().run()
