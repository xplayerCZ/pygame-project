class First:
    def Second(self, soubor):
        from models import crossword_build as quest
        quest.SOUBOR = soubor
        quest.Crossword().create()
