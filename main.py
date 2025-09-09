from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
import json
import random

from kivy.resources import resource_find

# Carica sfide in modo sicuro
try:
    path = resource_find("challenges.json")
    with open(path, "r", encoding="utf-8") as f:
        challenges = json.load(f)
except Exception as e:
    print("Errore caricando challenges.json:", e)
    challenges = [{"title": "Nessuna sfida trovata"}]

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
