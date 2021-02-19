from models import create_box
from models import box_question
from models import create_slider_plus
from models import create_slider_minus
from models import file_interface
from models import create_box_answer
import pygame as pg
pg.init()
SOUBOR = ""

class Crossword:

    @staticmethod
    def create():
        clock = pg.time.Clock()
        #answers = [["A", "A", "w", "B", "C", "D", "E"], ["B", "C", "D", "E", "B", "C", "D", "E"], ["E", "b", "B", "C", "D", "E", "B", "C"]]
        print(SOUBOR)
        questions = file_interface.load(SOUBOR)
        input_boxes = []
        box_question.SOUBOR = SOUBOR
        create_box_answer.SOUBOR = SOUBOR

        for i, question in enumerate(questions):
            for j, char in enumerate(question.answer):
                if char:
                    input_boxes.append(create_box.Box(100 + j * create_box.CUBE, 40 + i * create_box.CUBE, create_box.CUBE , create_box.CUBE))

        input_boxes.append(box_question.Box(100, create_box.WIDTH * 0.8, box_question.CUBE, 40))
        input_boxes.append(create_slider_plus.Box(create_slider_plus.POS_Y, create_box.WIDTH * 0.81, create_slider_plus.CUBE, create_slider_plus.CUBE))
        input_boxes.append(create_slider_minus.Box(create_slider_minus.POS_Y, create_box.WIDTH*0.87, create_slider_minus.CUBE, create_slider_minus.CUBE))
        input_boxes.append(create_box_answer.Box(100, create_box.WIDTH*0.87, create_box_answer.CUBE, create_box_answer.CUBEH))

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
