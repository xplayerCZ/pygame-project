import pygame as pg
import tkinter as tk
from models import create_box as box
from tkinter import filedialog
from models import  crossword_build

WIDTH = box.WIDTH
HEIGHT = box.HEIGHT
CUBE = 200
POS_X = 475
POS_Y = 25
VELIKOST_PISMA = 23
STYL_TEXT = "Arial"
SOUBOR = "crossword.xlt"


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
COLOR_NONE = pg.Color('black')
COLOR_WRITE = pg.Color('blue')
COLOR_FILL = pg.Color('grey')
FONT = pg.font.SysFont(STYL_TEXT, VELIKOST_PISMA)
root = tk.Tk()
root.withdraw()


class Button:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_NONE
        self.text = text
        self.txt_surface = FONT.render(text.center(4), True, self.color)
        self.active = False
        self.file_path = "crossword.xlt"

    def on_click(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pg.mouse.get_pos()):
                self.file_path = filedialog.askopenfilename()


    def update(self):
        width = max(CUBE, self.txt_surface.get_width())
        self.rect.w = width
        self.txt_surface = FONT.render("Vyber soubor".center(5), True, self.color)
        SOUBOR = self.file_path
        crossword_build.SOUBOR = SOUBOR

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(screen, self.color, self.rect, 2)

