from textx.metamodel import metamodel_from_file
from quiz import Quiz
import Settings

class DragDropQuiz(Quiz):

    def __init__(self):
       super(DragDropQuiz, self).__init__()

    def load_metamodel(self):
        self._metamodel = metamodel_from_file(Settings.DnD_METAMODEL)
        return self._metamodel

