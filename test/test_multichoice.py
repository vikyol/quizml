import unittest
import testdata
import sys
import tempfile
from textx.exceptions import TextXSyntaxError
from quiz import MultichoiceQuiz


class GrammarTest(unittest.TestCase):

    def setUp(self):
        self.mc_quiz = MultichoiceQuiz()
        self.quiz_file = tempfile.NamedTemporaryFile(delete=True)

    def tearDown(self):
        self.quiz_file.close()

    def test_metamodel(self):
        self.assertIsNotNone(self.mc_quiz.get_metamodel())

    def test_multichoice_noquestion(self):
        self.quiz_file.write(testdata.model_mc_invalid_no_question.encode())
        self.quiz_file.flush()
        self.assertRaises(TextXSyntaxError, self.mc_quiz.load_model, self.quiz_file.name)


if __name__ == '__main__':
    unittest.main()
