''' Quiz runner '''
import sys
from quiz import MultichoiceQuiz
from quiz import DragDropQuiz

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: {} <quiz type>'.format(sys.argv[0]))
        print('Quiz type: [mc|dnd]')
        sys.exit(1)

    if sys.argv[1] == 'mc':
        mc_quiz = MultichoiceQuiz()
        mc_quiz.load_model('../data/mc_01.qml')
        mc_quiz.print_model()
        data = mc_quiz.render_template()
        MultichoiceQuiz.save('mc.json', data)
    elif sys.argv[1] == 'dnd':
        dnd_quiz = DragDropQuiz()
        dnd_quiz.load_model('../data/dnd_01.qml')
        dnd_quiz.print_model()
        data = dnd_quiz.render_template()
        DragDropQuiz.save('dnd.json', data)
    else:
        print('Incorrect quiz type', sys.argv[1])
