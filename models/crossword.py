from models import create
from models import create_rect
from models import create_slider1
from models import create_slider2
import pygame as pg

class Crossword: #trida crossword vytvori krizovku
    @staticmethod
    def create():
        clock = pg.time.Clock()
        answers = [["A", "A", "w", "B", "C", "D", "E"], ["B", "C", "D", "E", "B", "C", "D", "E"], ["E", "b", "B", "C", "D", "E", "B", "C"]]
        input_boxes = []
        for i in range(len(answers)):
            for j in range(len(answers[i])):
                if answers[i][j]:
                    input_boxes.append(create.Box(100 + j * create.CUBE, 25 + i * create.CUBE, create.CUBE, create.CUBE))
        input_boxes.append(create_rect.Box(100, 400, create_rect.CUBE, 50))
        input_boxes.append(create_slider1.Box(create_slider1.POS_Y, create_slider1.POS_X, create_rect.CUBE, 35))
        input_boxes.append(create_slider2.Box(25, 425, create_rect.CUBE, 35))

        done = False

        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                for box in input_boxes:
                    box.on_click(event)
            for box in input_boxes:
                box.update()

            create.screen.fill((255, 255, 255))
            for box in input_boxes:
                box.draw(create.screen)

            pg.display.flip()
            clock.tick(30)

