import kivy
from kivy.app import App
from kivy.uix.button import Button
#import main

class ButtonApp(App):

    def build(self):
        btn = Button(text="Push Me !",
                     font_size='20',
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.2, .2),
                     pos=(300, 250))

        btn.bind(on_press=self.turnOn)
        return btn

    def turnOn(self, event):
        #main.First()
        root.stop()

root = ButtonApp()
root.run()