from abc import ABCMeta, abstractmethod
from textx.metamodel import metamodel_from_file
from jinja2 import Environment, FileSystemLoader
import Settings

class Quiz(metaclass=ABCMeta):
    
    def __init__(self):
        self._model = None
        self._metamodel = None

    # Out: Quiz metamodel
    def get_metamodel(self):
        if not self._metamodel:
            self.load_metamodel()
        return self._metamodel

    @abstractmethod
    def load_metamodel(self):
        pass

    # In: Quiz data in QuizML format 
    # Out: Model of the given quiz data
    def load_model(self, quiz_data):
        if self._model is None:
            # initialize the model
            quiz_mm = self.get_metamodel()
            # Create and return the model
            self._model = quiz_mm.model_from_file(quiz_data)
        return self._model

    # In: Quiz data in QuizML format 
    # Out: Model of the given quiz data
    def reload_model(self, quiz_data):
        self._model = None
        return load_model(self, quiz_data)

    def print_model(self):
        print(self._model.title)
        print(self._model.description)
        for tag in self._model.tags:
            print('#'+tag)

        for q in self._model.questions:
            print(q.question)
            for option in q.options:
                print(option.otype, option.otext)

    def render_template(self):
        env = Environment(loader=FileSystemLoader(Settings.TEMPLATE_FOLDER))

        template = env.get_template('multichoice.json.j2')

        output = template.render(quiz=self._model)
        print(output)

        # Save the results
        with open("quiz.json", "wb") as fh:
            fh.write(output.encode())




