from textx.metamodel import metamodel_from_file
from jinja2 import Environment, FileSystemLoader

def get_quiz_metamodel():
    try:
        return get_quiz_metamodel.metamodel
    except AttributeError:
        # initialize the quiz metamodel
        get_quiz_metamodel.metamodel = metamodel_from_file('meta/quiz.tx')
        return get_quiz_metamodel.metamodel

def load_quiz_model(quiz_data):
    quiz_mm = get_quiz_metamodel()
    # Create the model
    quiz_model = quiz_mm.model_from_file(quiz_data)

    return quiz_model


def print_model(model):
    print(model.title)
    print(model.description)
    for tag in model.tags:
        print('#'+tag)

    for q in model.questions:
        print(q.question)
        for option in q.options:
            print(option.otype, option.otext)


def render_template(quiz_model):
    env = Environment(loader=FileSystemLoader('templates'))

    template = env.get_template('json.j2')

    output = template.render(quiz=quiz_model)
    print(output)

    # to save the results
    with open("quiz.json", "wb") as fh:
        fh.write(output.encode())


if __name__ == "__main__":
    model = load_quiz_model('data/quiz.qml')
    print_model(model)
    render_template(model)


