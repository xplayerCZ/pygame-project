import pygame as pg

WIDTH = 640
HEIGHT = 480
CUBE = 200
VELIKOST_PISMA = 23
STYL_TEXT = "Arial"

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
COLOR_NONE = pg.Color('black')
COLOR_WRITE = pg.Color('red')
FONT = pg.font.SysFont(STYL_TEXT, VELIKOST_PISMA)


class Box:
    QUESTION_COUNT = 1
    QUESTION = "Toto je epicka otazka ?"

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_NONE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def on_click(self, event):
        if event.type == pg.MOUSEMOTION:
            if Box.QUESTION_COUNT == 1:
                Box.QUESTION = "Toto je epicka otazka 1 ?"
            elif Box.QUESTION_COUNT == 2:
                Box.QUESTION = "Toto je epicka otazka 2 ?"
            else:
                Box.QUESTION = "Toto je epicka otazka 3 ?"
                Box.QUESTION_COUNT = 0

            self.txt_surface = FONT.render(Box.QUESTION, True, self.color)


    def update(self):
        width = max(self.txt_surface.get_width(), self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(screen, self.color, self.rect, 2)

