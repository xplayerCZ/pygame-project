from models import create_box
from models import create_rect
from models import create_slider_right
from models import create_slider_left
from models import file_interface
import pygame as pg
pg.init()


class Crossword:#trida crossword vytvori krizovku

    @staticmethod
    def create():
        clock = pg.time.Clock()
        #answers = [["A", "A", "w", "B", "C", "D", "E"], ["B", "C", "D", "E", "B", "C", "D", "E"], ["E", "b", "B", "C", "D", "E", "B", "C"]]
        questions = file_interface.load("crossword.xlt")
        input_boxes = []

        for i, question in enumerate(questions):
            for j, char in enumerate(question.answer):
                if char:
                    input_boxes.append(create_box.Box(100 + j * create_box.CUBE, 25 + i * create_box.CUBE, create_box.CUBE, create_box.CUBE))

        input_boxes.append(create_rect.Box(100, 400, create_rect.CUBE, 50))
        input_boxes.append(create_slider_right.Box(create_slider_right.POS_Y, create_slider_right.POS_X, create_rect.CUBE, 35))
        input_boxes.append(create_slider_left.Box(25, 425, create_rect.CUBE, 35))

        done = False

        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                for box in input_boxes:
                    box.on_click(event)
            for box in input_boxes:
                box.update()

            create_box.screen.fill((255, 255, 255))
            for box in input_boxes:
                box.draw(create_box.screen)

            pg.display.flip()
            clock.tick(30)

