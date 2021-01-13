import pygame as pg

WIDTH = 640
HEIGHT = 480
CUBE = 50
VELIKOST_PISMA = 27

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
COLOR_NONE = pg.Color('black')
COLOR_WRITE = pg.Color('red')
FONT = pg.font.SysFont("Arial", VELIKOST_PISMA)


class Box:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_NONE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

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
                    while len(self.text) != 1:
                        self.text += event.unicode
                self.txt_surface = FONT.render(self.text.upper(), True, self.color)

    def update(self):
        width = max(CUBE, self.txt_surface.get_width())
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(screen, self.color, self.rect, 2)

