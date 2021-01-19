import pygame as pg
from models import file_interface
from models import create_box

WIDTH = create_box.WIDTH
HEIGHT = create_box.HEIGHT
CUBE = 200
CUBEH = 40
VELIKOST_PISMA = 23
STYL_TEXT = "Arial"
SOUBOR = "crossword.xlt"

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
COLOR_NONE = pg.Color('black')
COLOR_WRITE = pg.Color('red')
COLOR_WIN = pg.Color('green')
FONT = pg.font.SysFont(STYL_TEXT, VELIKOST_PISMA)
questions = file_interface.load(SOUBOR)
answer = "test"

class Box:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_NONE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.QUESTION_COUNT = 1
        self.QUESTION = "This is a default question"
        self.questions = file_interface.load(SOUBOR)


    def on_click(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_WRITE if self.active else COLOR_NONE

        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
    def listtostring(s):
        str1 = " "
        for e in s:
            str1 += e
        return str1

    def update(self):
        width = max(CUBE, self.txt_surface.get_width() + 10)
        self.rect.w = width
        if self.text == str(Box.listtostring(self.questions[len(self.questions)-1].question))[1:]:
            self.color = COLOR_WIN
        self.txt_surface = FONT.render("Answer: " + self.text, True, self.color)

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(screen, self.color, self.rect, 2)

