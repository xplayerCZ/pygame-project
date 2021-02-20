from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from tkinter import filedialog


SOUBOR = "crossword.xlt"
NAZEV_SOUBORU = "Choose File"


class FloatLayout(FloatLayout):
    Window.clearcolor = (255, 255, 255, 255)
    pass

class ButtonApp2(App):

    def build(self):
        self.soubor = SOUBOR
        return FloatLayout()

    def turnOn(self, event):
        start.stop()
        print(SOUBOR)
        from models import kivy_filestart
        kivy_filestart.First.Second(self, self.soubor)
        start.stop()

    def chooseFile(self, event):
        self.soubor = filedialog.askopenfilename()
        print(SOUBOR)

start = ButtonApp2()
start.run()
