from textx.metamodel import metamodel_from_file
from jinja2 import Environment, FileSystemLoader

def load_quiz_model():
    # Load the quiz metamodel first
    quiz_mm = metamodel_from_file('../meta/quiz.tx')
    # Create the model
    quiz_model = quiz_mm.model_from_file('../data/quiz.qml')

    return quiz_model


def print_model(model):
    print(model.description)

    for q in model.questions:
        print(q.question)
        for option in q.options:
            print(option.otype, option.otext)


def render_template(quiz_model):
    env = Environment(loader=FileSystemLoader('../templates'))

    template = env.get_template('json.j2')

    output = template.render(quiz=quiz_model)
    print(output)

    # to save the results
    with open("quiz.json", "wb") as fh:
        fh.write(output.encode())


if __name__ == "__main__":
    model = load_quiz_model()
    print_model(model)
    render_template(model)


