

####
#### На гит добавлены еще 17, 24, 25 задачи
####

import psycopg2
import bcrypt
#Создаем тестовую таблицу в БД и вносим туда 1 пользователья
connect = psycopg2.connect(dbname="testsystem2", user="test", password = "123", host = "localhost", port = "5432")
connect.autocommit = True
#with connect.cursor() as cur:
#    cur.execute(""" CREATE TABLE "testing2"
#        ("id_user" serial PRIMARY KEY,
#        "login" varchar(50),
#        "password" varchar(50),
#        "name" varchar(50),
#        "surname" varchar(50),
#        "patronymic" varchar(50),
#        "phone_number" integer,
#        "grp" varchar(50))
#         """)
#with connect.cursor() as cur:
#    cur.execute(
#        "INSERT INTO testing2(login, password, name, surname, patronymic, phone_number, grp) VALUES,
#        ('VasPup', '12345', 'Vasya', 'Pupkin', 'Ivanovich', 899941, 'bb11')")
print("1 Вход")
print("2 Регистрация")
parameter_selection = int(input("Выберите параметр: "))
if parameter_selection == 1:
    login = str(input("введите логин: "))
    password = str(input("Введите пароль: "))
    with connect.cursor() as cur:
        cur.execute("SELECT * FROM testing12 WHERE name = %s AND password = %s", [login, password])
        if cur.rowcount:
            cur.execute("SELECT name, surname FROM testing2")
            name_usr = cur.fetchone()
            print("Привет, ", " ".join(name_usr), " Выберите номер теста: ")
        else:
            print("Логин и пароль не найден, пройдите регистрацию1")

elif parameter_selection == 2:
    new_login = str(input("Придумайте логин: "))
    new_password = str(input("Придумайте пароль: "))
    new_name = str(input("Укажите ваше имя: "))
    new_surname = str(input("Укажите вашу фамилию: "))
    new_patronymic = str(input("Укажеите ваше отчество: "))
    new_phone_number = int(input("Укажите ваш номер телефона: "))
    new_group = str(input("Укажите вашу группу: "))
    hashandsalt = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
    hashandsalt = hashandsalt.decode('utf-8')
    with connect.cursor() as cur:
        cur.execute("SELECT * FROM testing12 WHERE login = %s AND password = %s", [new_login, new_password])
        if cur.rowcount:
            print("пользователь с таким именем существует")
        else:
            cur.execute(
        "INSERT INTO testing2(login, password, name, surname, patronymic, phone_number, grp) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            [new_login, hashandsalt, new_name, new_surname, new_patronymic, new_phone_number, new_group])
        print("Добро пожаловать, ", new_name, new_surname, ".Выберите номер теста", sep=" ")