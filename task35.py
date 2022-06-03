import datetime
import time
from threading import Thread
from threading import Lock
import psycopg2
import bcrypt

class db:
    __instance__ = None
    def __init__(self):
        self.__connect = psycopg2.connect(dbname="testsystem2", user="test", password = "123", host = "localhost", port = "5432")
        if db.__instance__ is None:
            db.__instance__ = self.__connect
        else:
            raise Exception("Невозможно создать класс")
    @staticmethod
    def getinstance():
        if not db.__instance__:
            db()
        return db.__instance__
class Profile:
    def __init__(self, name = None, surname = None, age = None, password = None):
        self.connect = db.__instance__
        self.name = name
        self.surname = surname
        self.age = age
        self.password = password
        self.login = None

    def getprofile(self, login):
        cur = self.connect.cursor()
        cur.execute(f"""SELECT "login", "password" FROM "profile" WHERE "login" LIKE '{login}' """)
        login_password = cur.fetchall()
        return login_password

    def setprofile(self, name, surname, patronymic, group, login, password):
        cur = self.connect.cursor(f"""INSERT INTO "student" ("name", "surname", "patronymic", "group")
        VALUES ('{name}', '{surname}', '{patronymic}', '{group}')""")
        self.connect.commit()

class authorisation:
    Login = None
    def __init__(self):
        self.connect = db.__instance__
        self.login = None
        self.password = None
        self.name = None
        self.surname = None
        self.patronymic = None
        self.group = None
        self.age = None
        self.phone_number = None
        self.email = None
    is_authorisation = bool()

    def regisrtration(self):
        self.login = input("enter login: ")
        self.password = input("enter password: ")
        self.name = input("enter name: ")
        self.surname = input("enter surname: ")
        self.patronymic = input("enter patronymic: ")
        self.group = input("enter group: ")
        self.age = input("enter age: ")
        self.phone_number = input("enter phone number: ")
        self.email = input("enter email: ")
        Profile().setprofile(self.name, self.surname, self.patronymic, self.group, self.login, self.password)
        authorisation.Login = self.login
        self.connect.close()
        authorisation.is_authorisation = True
        return authorisation.is_authorisation

    def log(self):
        self.login = input("enter login: ")
        self.password = input("enter password: ")
        prof = Profile().getprofile(self.login)
        if len(prof):
            if self.password == str(prof[0][1]):
                authorisation.is_authorisation = True
            else:
                print("wrong password"), authorisation().log()
        else:
            print("Profile not found, enter registration")
            authorisation().regisrtration()

    def logout(self):
        authorisation.is_authorisation = False

class saveresult:
    def __init__(self):
        self.connect = db.getinstance()
        self.login = authorisation.Login
        self.cur = self.connect.cursor()

    def save_res(self, test, data_time, result, timer):
        self.cur.execute(f"""INSERT INTO "test_result" ("login", "test", "data_time", "result", "timer")
            VALUES ('{self.login}', '{data_time}','{test}', {result}, {timer}')""")
        self.connect.commit()

class Test:
    def __init__(self):
        self.connect = db.getinstance()

    def getlisttest(self):
        cur = self.connect.cursor()
        cur.execute("""SELECT "id_test", "theme" FROM "test" """)
        tests = cur.fetchall()
        return tests

    def getquestion(self, id_test):
        cur = self.connect.cursor()
        cur.execute(f""" SELECT "id_question", "id_answer", "status" FROM "test_question" 
                                WHERE "id_test" = {id_test} """)
        test = cur.fetchall
        return test

class testsystem:
    def __init__(self):
        self.connect = db.getinstance()
        self.cur = self.connect.cursor()
    test_out = False
    
    def run(self):
        while not authorisation.is_authorisation:
            authorisation().log()
        else:
            print("You enter in test system", "\n",
                  "choose a test topic", "\n")
        testview().render()

    def showlist(self):
        pass

    def showquestion(self, id_question):
        pass

    def getlistquestion(self, element):
        self.cur.execute(f""" SELECT "text_question" FROM "question" WHERE "id_question" = {element} """)
        test = self.cur.fetchall()
        return test
    def getlistanswer(self, element):
        self.cur.execute(f""" SELECT "answer" FROM "answer" WHERE "id_answer" = {element}""")
        answers = self.cur.fetchall()
        return answers

class View:
    def render(self):
        pass

class questionview(View):
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
    def time_render(self, data):
        st = list()
        d_time = datetime.datetime.now()
        f_time = time.time()
        thr = Thread(target=(st.append(questionview().render(data))))
        thr.start()
        questionview.lock.acquire()
        questionview.stop_thrd = True
        questionview.lock.release()

        test_time = time.time() - f_time
        saveresult().save_res(data, d_time, st, test_time)
        print("Тест завершен", "\n", "Оценка: ", st)
        time.sleep(10)
        authorisation.logout()

class testview(View):
    def __init__(self):
        pass

    def render(self):
        for t in Test().getlisttest():
            print(str(t).strip("(), ' ").replace(", ", ". "))
        questionview().time_render(input("Выберите номер теста: "))

testsystem().run()

class registrationview(View):
    def render(self, data):
        pass
class loginview(View):
    def render(self, data):
        pass



        
