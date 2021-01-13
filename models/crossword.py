from models import create
import pygame as pg

class Crossword: #trida crossword vytvori krizovku
    clock = pg.time.Clock()
    answers = [["P", "A", "w"], ["B", "C", "D", "E"], ["E", "b"]]
    input_boxes = []
    for i in range(len(answers)):
        for j in range(len(answers[i])):
            if answers[i][j]:
                input_boxes.append(game.Box(100 + j * game.CUBE, 25 + i * game.CUBE, game.CUBE, game.CUBE))
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                box.on_click(event)

        for box in input_boxes:
            box.update()

        game.screen.fill((255, 255, 255))
        for box in input_boxes:
            box.draw(game.screen)

        pg.display.flip()
        clock.tick(30)

