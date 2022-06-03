#todo: Сделать рефакторинг кода задачи 35.
#  1. Реализовать из класса DB синглтон. Экземляр класса должен быть единственным.
#  2. Сделать класс View абстрактным, а также метод render() абстрактным
#  3. Реализовать  фабрику FabConsoleView в которой пораждаются экзепляры
#     классов TestView, QuestionView и AuthView

#  1. Реализовать из класса DB синглтон. Экземляр класса должен быть единственным.
class db:
    __instanse__ = None
    def __init__(self):
        if db.__instanse__ is None:
            db.__instanse__ = self
        else:
            raise Exception("Невозможно создать класс")
    @staticmethod
    def getinstance():
        if not db.__instanse__:
            db()
        return db.__instanse__

#  2. Сделать класс View абстрактным, а также метод render() абстрактным
from abc import ABC
from abc import abstractmethod
class View(ABC):
    @abstractmetod
    def render(self):
        raise NotImplementedError("Метод не импортирован")


class View:
    def __init__(self, QuestionView, RegistrationView):
        self.QuestionView = "Метод реализует отрисовку вопроса с вариантами ответа и строкой выбора варианта"
        self.RegistrationView = "Метод реализует отрисовку регистрации пользователя"
    def __repr__(self):
        return f'Question = {self.QuestionView}% Registration = {self.RegistrationView}%'
    def render(cls):
        return cls('отрисовка регистрации и вопроса')
Realisation.render = classmethod(Realisation.render)

#  3. Реализовать  фабрику FabConsoleView в которой пораждаются экзепляры
#     классов TestView, QuestionView и AuthView

class FabConsoleView():
    def __init__(self, testview, questionview, loginview):
        self.testview = testview
        self.questionview = questionview
        self.loginwiew = loginview

class testview(FabConsoleView):
    def __init__(self):
        pass

    def render(self):
        for t in Test().getlisttest():
            print(str(t).strip("(), ' ").replace(", ", ". "))
        questionview().time_render(input("Выберите номер теста: "))

class questionview(FabConsoleView):
    lock = Lock()
    stop_thrd = False

    def render(self, data = None):
        stedent_res = 0
        q = list()
        q1 = list()
        q2 = list()
        list_question = Test().getquestion(data)
        for qs, qs1, qs2 in list_question:
            q.append(qs)
            q1.append(qs1)
            q2.append(qs2)
        question = sorted(set(q))
        k_ = len(q1) / len(question)
        k = 0
        for element in question:
            c = 1
            test1 = testsystem().getlistquestion(element)
            for t in test1:
                print("Вопрос: ", str(t).strip("(), '"))
            for i in range(k, int(k + k_)):
                 student_res = 0
                 answer1 = testsystem().getlistanswer(q1[i])
                 print(f"{c}. ", str(answer1[0]).strip("(), '"))
                 c += 1
            student_answer = int(input("Выберите ответ: "))
            student_res += 1 if q2[student_answer - 1 + k] is True else None
            k += int(k_)
        return stedent_res

class loginview(FabConsoleView):
    def render(self, data):
        pass

class FabConsoleViewFactory():
    def getFabConsoleView(self, FabConsoleViewFunction):
        if FabConsoleViewFunction == 'questionview':
            return questionview()
        elif FabConsoleViewFunction == 'testview':
            return testview()
        elif FabConsoleViewFunction == 'lodinview':
            return loginview()
        else:
            pass

