from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
import json
import random

# Carica sfide
with open("challenges.json", "r") as f:
    challenges = json.load(f)

# Schermate
class HomeScreen(Screen):
    def on_enter(self):
        self.ids.challenge_label.text = random.choice(challenges)['title']

class JivoryApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        return Builder.load_string("""
ScreenManager:
    HomeScreen:

<HomeScreen>:
    name: 'home'
    MDBoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 20
        MDLabel:
            id: challenge_label
            text: "Sfida di oggi"
            halign: "center"
            font_style: "H5"
        MDRaisedButton:
            text: "Genera nuova sfida"
            pos_hint: {"center_x":0.5}
            on_release: root.on_enter()
""")

JivoryApp().run()
