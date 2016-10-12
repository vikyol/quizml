'''
Quiz abstract class defines the basic model loading and validation operations.
Concrete quiz classes only override data related methods.
'''
from abc import ABCMeta, abstractmethod
from textx.metamodel import metamodel_from_file
from jinja2 import Environment, FileSystemLoader
import config

class Quiz(metaclass=ABCMeta):
    '''
     Quiz abstract base class implements model and metamodel management methods.
    '''

    def __init__(self):
        '''
        var: env: Environment variable pointing to the template folder
        var: model: validated quiz model
        var: metamodel: syntax definition of the quiz
        '''
        self._env = Environment(loader=FileSystemLoader(config.TEMPLATE_FOLDER))
        self._model = None
        self._metamodel = None


    @abstractmethod
    def load_metamodel(self):
        ''' validate and return the metamodel for the concrete class '''
        pass


    @abstractmethod
    def load_template(self):
        ''' return: default template of the concrete quiz class '''
        pass


    def get_metamodel(self):
        ''' Initializes and returns the metamodel '''
        if not self._metamodel:
            self.load_metamodel()
        return self._metamodel


    def load_model(self, quiz_data):
        '''
        Initialize the model
        :param quiz_data: raw qml data
        :return the quiz model
        '''
        if self._model is None:
            meta_quiz = self.get_metamodel()
            # Create and return the model
            self._model = meta_quiz.model_from_file(quiz_data)
        return self._model


    def get_model(self):
        ''' return the validated model '''
        return self._model


    def reload_model(self, quiz_data):
        '''
        Resets and reinitializes the model.
        :param quiz_data: raw qml data
        :return: the quiz model
        '''
        self._model = None
        return self.load_model(quiz_data)

    @abstractmethod
    def print_model(self):
        '''
        print the quiz model for debugging purposes
        '''
        print(self._model.title)
        print(self._model.description)
        for tag in self._model.tags:
            print('#'+tag)


    def render_template(self):
        '''
        Renders the template with the provided quiz model
        :return template data rendered with the model
        '''
        template = self.load_template()

        output = template.render(quiz=self._model)

        return output

    @staticmethod
    def save(file_name, data):
        '''
        Save rendered templated data
        This function is going to be replaced with a proper DataSource
        :param file_name: output file_name
        :param data rendered quiz data
        '''
        with open(file_name, "wb") as output_file:
            output_file.write(data.encode())


class MultichoiceQuiz(Quiz):
    ''' Overrides metamodel and template loading methods '''

    def __init__(self):
        ''' Invokes parent's init method '''
        super(MultichoiceQuiz, self).__init__()

    def load_metamodel(self):
        ''' Loads the configured metamodel '''
        self._metamodel = metamodel_from_file(config.MC_METAMODEL)
        return self._metamodel

    def load_template(self):
        '''
        Default template is JSON. More templates to be added later.
        :return the template for Multichoice quiz.
        '''
        return self._env.get_template(config.Templates['MC_JSON'])

    def print_model(self):
        ''' print multi-choice quiz model '''
        super(MultichoiceQuiz, self).print_model()

        for questions in self._model.questions:
            print(questions.question)
            for option in questions.options:
                print(option.otype, option.otext)


class DragDropQuiz(Quiz):
    ''' Overrides metamodel and template loading methods '''

    def __init__(self):
        ''' Invokes parent's init method '''
        super(DragDropQuiz, self).__init__()

    def load_metamodel(self):
        ''' Loads the configured metamodel for DragandDrop quiz '''
        self._metamodel = metamodel_from_file(config.DD_METAMODEL)
        return self._metamodel

    def load_template(self):
        '''
        Default template is JSON. More templates to be added later.
        :return the template for Multichoice quiz.
        '''
        return self._env.get_template(config.Templates['DD_JSON'])

    def print_model(self):
        ''' print drag and drop quiz model '''
        super(DragDropQuiz, self).print_model()

        for question in self._model.questions:
            print(question.target)
            print(question.draggable.otext)
