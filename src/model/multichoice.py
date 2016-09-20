from textx.metamodel import metamodel_from_file
from quiz import Quiz
import Settings

class MultichoiceQuiz(Quiz):

    def __init__(self):
       super(MultichoiceQuiz, self).__init__()

    def load_metamodel(self):
        self._metamodel = metamodel_from_file(Settings.MC_METAMODEL)
        return self._metamodel

