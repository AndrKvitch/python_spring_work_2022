import psycopg2
import bcrypt
class db:
    def __init__(self, name, user, password):
        self.dbname = name
        self.user = user
        self.password = password
    def getConnection(self):
        connect = psycopg2.connect(dbname="testsystem2", user="test", password = "123", host = "localhost", port = "5432")
        return connect
object = db(name='testsystem', user='test', password='123')
conn = object.getConnection()


class profile:
    def __init__(self, login, password, name, group):
        self.login = login,
        self.password = password
        self.name = name
        self.group = group

    def getprofile(self):
        with psycopg2.connect(dbname="testsystem2", user="test", password = "123", host = "localhost", port = "5432") as conn:
            with conn.cursor as cur:
                cur.execute(f"""SELECT login, password FROM testsystem2 WHERE login = '{self.login}'""")
            res_log = cur.fetchone()
            if res_log is None:
                return "Пользователь не найден. Зарегестрируйтесь"
            else:
                val = bcrypt.checkpw(self.password.encode(), res_log[1].encode())
                if val:
                    return "добро пожаловать ", {self.login}
                else:
                    "Неверный логин или пароль"
    def setprofile(self):
        with psycopg2.connect(dbname="testsystem2", user="test", password = "123", host = "localhost", port = "5432") as cnct:
            with cnct.cursor() as cur:
                try:
                    cur.execute("""SELECT name FROM testing2 ORDER BY name desc limit 1""")
                    res_user_count = cur.fetchone()
                    new_res_user = int(res_user_count[0]) + 1
                except:
                    new_res_user = 1
                    cnct.rollback()
                cur.execute(f"INSERT INTO testing2 (id_user, name, login, password) VALUES "
                            f"({new_res_user}, {self.name}, {self.login}, {self.password});")
                print("Пользователь добавлен")
                cnct.commit()

