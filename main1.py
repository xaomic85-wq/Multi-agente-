from kivy.app import App
from kivy.uix.label import Label
import math

class MeuApp(App):
    def build(self):
        return Label(text='Oi mae! O valor de pi e: ' + str(math.pi))

MeuApp().run()
