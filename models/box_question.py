import pygame as pg
from models import file_interface
from models import create_box
from models import crossword_build

WIDTH = create_box.WIDTH
HEIGHT = create_box.HEIGHT
CUBE = 200
VELIKOST_PISMA = 20
STYL_TEXT = "Arial"


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
COLOR_NONE = pg.Color('black')
COLOR_WRITE = pg.Color('red')
FONT = pg.font.SysFont(STYL_TEXT, VELIKOST_PISMA)


class Box:
    QUESTION_COUNT = 0

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_NONE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.QUESTION = "This is a default question"
        self.questions = file_interface.load(crossword_build.SOUBOR)

    def on_click(self, event):
        if event.type == pg.MOUSEMOTION:
            self.color = COLOR_NONE

    def listtostring(s):
        str1 = " "
        for e in s:
            str1 += e
        return str1

    def update(self):
        width = max(self.txt_surface.get_width(), self.txt_surface.get_width() + 10)
        self.rect.w = width
        for i, self.question in enumerate(self.questions):
            if Box.QUESTION_COUNT == Box.QUESTION_COUNT and Box.QUESTION_COUNT < i:
                self.QUESTION = str(Box.listtostring(self.questions[Box.QUESTION_COUNT].question))
            elif Box.QUESTION_COUNT > len(self.questions)-2:
                Box.QUESTION_COUNT = 0
        self.txt_surface = FONT.render("Question " + str(Box.QUESTION_COUNT + 1) + ": " + self.QUESTION, True, self.color)
        if __name__ == '__main__':
            self.SOUBOR = crossword_build.SOUBOR

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(screen, self.color, self.rect, 2)

