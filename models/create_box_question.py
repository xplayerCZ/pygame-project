import pygame as pg
from models import file_interface

WIDTH = 600
HEIGHT = 600
CUBE = 200
VELIKOST_PISMA = 23
STYL_TEXT = "Arial"

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
COLOR_NONE = pg.Color('black')
COLOR_WRITE = pg.Color('red')
FONT = pg.font.SysFont(STYL_TEXT, VELIKOST_PISMA)


class Box:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_NONE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.QUESTION_COUNT = 0
        self.QUESTION = "bruh"
        self.questions = file_interface.load("crossword.xlt")

    def on_click(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            self.QUESTION_COUNT = self.QUESTION_COUNT + 1

    def listtostring(s):
        str1 = " "
        for e in s:
            str1 += e
        return str1

    def update(self):
        width = max(self.txt_surface.get_width(), self.txt_surface.get_width() + 10)
        self.rect.w = width
        for i, self.question in enumerate(self.questions):
                if self.QUESTION_COUNT == self.QUESTION_COUNT and self.QUESTION_COUNT < i:
                    self.QUESTION = str(Box.listtostring(self.questions[self.QUESTION_COUNT].question)) #+ " ?"
                elif self.QUESTION_COUNT > len(self.questions)-2:
                    self.QUESTION_COUNT = 0
                #print(self.QUESTION_COUNT)
        self.txt_surface = FONT.render("Question " + str(self.QUESTION_COUNT) + ": " + self.QUESTION, True, self.color)


    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(screen, self.color, self.rect, 2)

