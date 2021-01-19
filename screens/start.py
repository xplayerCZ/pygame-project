import pygame as pg
from screens import start_btn
from screens import start_choose

pg.init()

class Start:

    @staticmethod
    def create():
        clock = pg.time.Clock()
        input_boxes = []
        input_boxes.append(start_btn.Button(105, 350, 200, 50))
        input_boxes.append(start_choose.Button(185, 275, 100, 50))

        done = False

        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                for box in input_boxes:
                    box.on_click(event)
            for box in input_boxes:
                box.update()

            start_btn.screen.fill((255, 255, 255))
            for box in input_boxes:
                box.draw(start_btn.screen)

            pg.display.flip()
            clock.tick(30)