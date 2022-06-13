# todo: Реализовать две сопрограммы. Первая с заданной периодичность(раз в 2,3 сек) пишет в файл и выводит результат.
# другая делает запрос к БД на выборку  билета и отображает поочередно  название билета (раз в 2,3 сек)

import random
import asyncio
from aiofile import async_open
import asyncpg
import datetime

class Test:

    @classmethod
    async def get_list_tests(cls):
        print(f"Вход в БД {datetime.datetime.now()}")
        con = await asyncpg.connect(dbname="testsystem2", user="test", password="123", host="localhost", port="5432")
        print(f"Запрос данных из БД {datetime.datetime.now()}")
        async with con.transaction():
            cur = await con.fetch(f"""SELECT id_answer, answer_text FROM test_answer""")
            theme_lists = [dict(cur[i]) for i in range(len(cur))]
            val_list = [[v for v in theme_lists[i].values()] for i in range(len(theme_lists))]
            print(random.choice(val_list)[0])

async def logger():
    text_1 = "Hello\n"
    print(f"Открытие файла на запись {datetime.datetime.now()}")
    async with async_open('classwork1006.TXT', "a+", encoding="utf-8") as f:
        print(f"Запись 'Hello' {datetime.datetime.now()}")
        await f.write(text_1)

async def main():
    await asyncio.gather(logger(), Test.get_list_tests())

asyncio.run(main())

