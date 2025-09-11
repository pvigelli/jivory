# main.py
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.utils import platform

import json
import random
import sys
import traceback
import threading
import os

KV = """
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
"""

def format_traceback(exc_type, exc_value, exc_tb):
    return ''.join(traceback.format_exception(exc_type, exc_value, exc_tb))

def safe_show_popup(text):
    """
    Show a scrollable popup with long text. Use Clock to be sure we are on the main thread.
    """
    def _open(dt):
        label = Label(text=text, size_hint_y=None, text_size=(Window.width * 0.9, None))
        # set label height after texture is computed
        label.bind(texture_size=lambda inst, val: setattr(inst, 'height', val[1]))
        sv = ScrollView(do_scroll_x=False, do_scroll_y=True)
        sv.add_widget(label)
        popup = Popup(title='Errore - vedi traccia', content=sv, size_hint=(0.95, 0.95))
        popup.open()
    Clock.schedule_once(_open, 0.1)

# global fallback variable for startup error
startup_error_trace = None

# Set global excepthook to display uncaught exceptions
def global_excepthook(exc_type, exc_value, exc_tb):
    trace = format_traceback(exc_type, exc_value, exc_tb)
    # try show popup (if app and event loop exist), otherwise print
    try:
        # write to file in app user_data_dir if possible
        app = MDApp.get_running_app()
        if app:
            # attempt to save a copy to user_data_dir
            try:
                path = os.path.join(app.user_data_dir, "last_crash.txt")
                os.makedirs(app.user_data_dir, exist_ok=True)
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(trace)
            except Exception:
                pass
            # show popup
            safe_show_popup(trace)
        else:
            # maybe before app created
            print("Unhandled exception (before app):")
            print(trace)
    except Exception:
        # Last resort: print
        print("Error while handling exception:")
        print(trace)

sys.excepthook = global_excepthook

# catch thread exceptions (py3.8+)
if hasattr(threading, "excepthook"):
    def thread_excepthook(args):
        global_excepthook(args.exc_type, args.exc_value, args.exc_traceback)
    threading.excepthook = thread_excepthook

class HomeScreen(Screen):
    def on_enter(self):
        app = MDApp.get_running_app()
        ch = getattr(app, "challenges", None)
        if ch and isinstance(ch, (list, tuple)) and len(ch) > 0:
            # choose safely
            try:
                item = random.choice(ch)
                title = item.get('title') if isinstance(item, dict) else str(item)
                self.ids.challenge_label.text = title or "(senza titolo)"
            except Exception:
                self.ids.challenge_label.text = "(errore durante scelta sfida)"
        else:
            self.ids.challenge_label.text = "(Nessuna sfida caricata)"

class JivoryApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        return Builder.load_string(KV)

    def on_start(self):
        # Load challenges here (on UI thread) and show error popup if something goes wrong.
        try:
            # try to open the packaged JSON file
            # using a few attempts for path resolution
            possible_paths = [
                "challenges.json",
                os.path.join(self.user_data_dir, "challenges.json"),
                os.path.join(os.getcwd(), "challenges.json")
            ]
            data = None
            for p in possible_paths:
                if p and os.path.exists(p):
                    with open(p, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    break
            if data is None:
                # last attempt: try open relative resource (may work in some packaging)
                try:
                    with open("challenges.json", "r", encoding="utf-8") as f:
                        data = json.load(f)
                except Exception:
                    data = None

            if not data:
                raise FileNotFoundError("challenges.json non trovato o vuoto. Controlla che sia incluso nel pacchetto.")

            if not isinstance(data, list):
                raise ValueError("Formato di challenges.json non valido: expected list at top level.")

            self.challenges = data

            # show one initial challenge
            self.root.get_screen('home').on_enter()

        except Exception as e:
            trace = format_traceback(type(e), e, e.__traceback__)
            # put a minimal placeholder so UI won't crash
            self.challenges = [{'title': '(errore caricamento sfide)'}]
            # show popup with the full traceback
            safe_show_popup(trace)

if __name__ == "__main__":
    JivoryApp().run()