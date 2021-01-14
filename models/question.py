class Question:
    def __init__(self, question="", answer=[]):
        self.question = question
        self.answer = answer

    @property
    def question(self):
        return self.__question

    @question.setter
    def question(self, value):
        self.__question = value

    @property
    def answer(self):
        return self.__answer

    @answer.setter
    def answer(self, value):
        self.__answer = value
