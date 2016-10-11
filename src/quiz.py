from abc import ABCMeta, abstractmethod
from textx.metamodel import metamodel_from_file
from jinja2 import Environment, FileSystemLoader
import config

class Quiz(metaclass=ABCMeta):

    def __init__(self):
        self._env = Environment(loader=FileSystemLoader(config.TEMPLATE_FOLDER))
        self._model = None
        self._metamodel = None

    @abstractmethod
    def load_metamodel(self):
        pass

    @abstractmethod
    def load_template(self):
        pass

    def get_metamodel(self):
        ''' Initialize and return the metamodel '''
        if not self._metamodel:
            self.load_metamodel()
        return self._metamodel


    def load_model(self, quiz_data):
        '''
        Initialize the model
        :param quiz_data: raw qml data
        :return: the quiz model
        '''
        if self._model is None:
            meta_quiz = self.get_metamodel()
            # Create and return the model
            self._model = meta_quiz.model_from_file(quiz_data)
        return self._model


    def reload_model(self, quiz_data):
        '''
        Resets and reinitializes the model.
        :param quiz_data: raw qml data
        :return: the quiz model
        '''
        self._model = None
        return load_model(self, quiz_data)


    def print_model(self):
        ''' print the quiz model for debugging purposes '''
        print(self._model.title)
        print(self._model.description)
        for tag in self._model.tags:
            print('#'+tag)

        for q in self._model.questions:
            print(q.question)
            for option in q.options:
                print(option.otype, option.otext)


    def render_template(self):
        '''
        Renders the template with the provided quiz model
        '''
        template = self.load_template()

        output = template.render(quiz=self._model)
        print(output)

        return output


    def save_json(self, data):
        '''
        Save data in json format
        This function is going to be replaced with a proper DataSource
        '''
        with open("quiz.json", "wb") as fh:
            fh.write(data.encode())


class MultichoiceQuiz(Quiz):

    def __init__(self):
       super(MultichoiceQuiz, self).__init__()

    def load_metamodel(self):
        self._metamodel = metamodel_from_file(config.MC_METAMODEL)
        return self._metamodel

    def load_template(self):
        return self._env.get_template(config.Templates['MC_JSON'])


class DragDropQuiz(Quiz):

    def __init__(self):
       super(DragDropQuiz, self).__init__()

    def load_metamodel(self):
        self._metamodel = metamodel_from_file(Config.DD_METAMODEL)
        return self._metamodel

    def load_template(self):
        return self._env.get_template(config.Templates['DD_JSON'])
