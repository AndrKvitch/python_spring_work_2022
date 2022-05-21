import psycopg2

connect = psycopg2.connect(dbname="postgres", user="test", password="123", host="localhost", port="5432")
with connect.cursor() as cur:
    cur.execute("""
        CREATE TABLE "group" (
            "id_group" serial PRIMARY KEY, 
            "name" varchar(50)
        """)
    cur.execute("""
            CREATE TABLE "student" (
                "id_student" serial PRIMARY KEY, 
                "name" varchar(50),
                "id_group" integer not null
            """)
    cur.execute("""
            CREATE TABLE "test" (
                "id_test" serial PRIMARY KEY,
                "id_student_test" integer not null,
                "tm_test" timestamp
                "theme" varchar(100)
                "true_answer" boolean)
            """)
    cur.execute("""
        CREATE INDEX "idx_student_id_group" ON "student" ("id_group");
        """)
    cur.execute("""
            CREATE INDEX "idx_student_test_id_student" ON "student_test" ("id_student");
            """)
    cur.execute("""
            CREATE INDEX "idx_student_test_id_test" ON "student_test" ("id_test");
            """)
cur.close()
connect.commit()

###при запуске программы мне выдает ошибку:
### line 122, in connect
###    conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
###psycopg2.OperationalError
#я не могу разобраться, из-за чего он не подключается к БД и не создает таблицу. Все данные для подклчения
#введены верно
