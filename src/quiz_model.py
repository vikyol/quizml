from textx.metamodel import metamodel_from_file

quiz_mm = metamodel_from_file('../meta/quiz.tx')

# Create model
quiz_model = quiz_mm.model_from_file('../data/quiz.qml')


def print_model(model):
    print(model.description)

    for q in model.questions:
        print(q.question)
        for answer in q.answers:
            print(answer.atype, answer.atext)


if __name__ == "__main__":
    print_model(quiz_model)

