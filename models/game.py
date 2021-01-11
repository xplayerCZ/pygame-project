from models import question
import random

class Crossword:
    def __init__(self):
        rows = []

    @staticmethod
    def generate(question_file):
        with open(question_file) as f:
            lines = [question.Question(i.split(";")[0], i.split(";")[1]) for i in f.readlines()]
            word_puzzle = random.choice(lines)
        splited_puzzle = list(word_puzzle.answer)
        splited_puzzle = splited_puzzle[:-1]

        for x in splited_puzzle:
            random_fill = random.choice(lines)
            split_fill = list(random_fill.answer)
            print(x, split_fill)

