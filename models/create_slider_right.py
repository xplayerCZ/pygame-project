import pygame as pg
from models import  create_box_question

WIDTH = 600
HEIGHT = 600
CUBE = 25
VELIKOST_PISMA = 23
STYL_TEXT = "Arial"
POS_X = 375
POS_Y = 25


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
        self.txt_surface = FONT.render(">".center(3), True, self.color)

    def on_click(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            return

    def update(self):
        width = max(self.txt_surface.get_width(), self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(screen, self.color, self.rect, 2)

