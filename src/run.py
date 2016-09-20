from quiz import Quiz
from multichoice import MultichoiceQuiz

if __name__ == "__main__":
    quiz = MultichoiceQuiz()
    quiz.load_model('../data/quiz_mc_01.qml')
    quiz.print_model()
    quiz.render_template()
