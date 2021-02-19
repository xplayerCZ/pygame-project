from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from tkinter import filedialog

SOUBOR = "crossword.xlt"
NAZEV_SOUBORU = "Choose File"



class ButtonApp(App):


    def build(self):
        self.soubor = SOUBOR
        Window.clearcolor = (255, 255, 255, 255)

        layoutLabel = GridLayout(cols=1,row_force_default = True, row_default_height = 100)
        layoutText = GridLayout(cols=1 ,row_force_default = True, row_default_height = 950)
        layoutCenter = AnchorLayout(anchor_x='center', anchor_y='center')
        layoutCenter2 = AnchorLayout(anchor_x='center', anchor_y='bottom')
        layout = FloatLayout()

        lab = Label(text="Welcome to the game! CROSSWORD",
                    font_size = '45sp',
                    color=(0,0,0)
                    )
        labInfo = Label(text="(Optional) Choose file to make crossword from:",
                    font_size = '20sp',
                    color=(0,0,0)
                    )


        btn = Button(text="Start",
                     font_size='20',
                     color=(0, 0, 0),
                     size_hint = (.4, .1),
                     width = 200,
                     height=100
                     )

        btnChoose = Button(text=NAZEV_SOUBORU,
                     font_size='20',
                     color=(0, 0, 0),
                        size_hint_y= None,
                     width = 200,
                     height=100

                     )

        btn.bind(on_press=self.turnOn)
        btnChoose.bind(on_press=self.chooseFile)

#//////////////////////////////////////////////////////////
        layoutLabel.add_widget(lab)
        layoutCenter2.add_widget(btnChoose)
        layoutCenter.add_widget(btn)
        layoutText.add_widget(labInfo)
        layout.add_widget(layoutCenter)
        layout.add_widget(layoutLabel)
        layout.add_widget(layoutCenter2)
        layout.add_widget(layoutText)
#//////////////////////////////////////////////////////////

        return layout

    def turnOn(self, event):
        print(SOUBOR)
        from models import crossword_build as quest
        quest.SOUBOR = self.soubor
        quest.Crossword().create()
        root.stop()

    def chooseFile(self, event):
        self.soubor = filedialog.askopenfilename()
        print(SOUBOR)


root = ButtonApp()
root.run()