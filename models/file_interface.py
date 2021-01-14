import pandas
import math
from models.question import Question


def load(path):
    questions = []
    data = pandas.read_excel(io=path, header=None)

    for row in data.iterrows():
        question = Question()
        question.answer = []

        for column in row:
            if type(column) is int:
                continue
            for j, value in column.items():
                print("Value: ", value)
                if j == 0:
                    question.question = value
                else:
                    if type(value) == float:
                        question.answer.append("")
                    else:
                        question.answer.append(value)

        questions.append(question)
    return questions

