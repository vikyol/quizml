import unittest
from quiz_model import *

class GrammarTest(unittest.TestCase):

    model_mc_base = "@quiz this is a sample quiz\n"\
                    "@desc multi-choice quiz to to demonstrate qml\n"\
                    "@tags test, sample tag\n"

    """    model_mc_1q = model_mc_base + "
    ? This is the first question
    + True
    - False"

    model_mc_2q = model_mc_1q + "
    ? This is the second question
     + True
    - False"
    """
    def test_metamodel(self):
        self.assertIsNotNone(get_quiz_metamodel())

    def test_multichoice_noquestion(self):
        metamodel = get_quiz_metamodel()
        metamodel.model_from_str(self.model_mc_base)
