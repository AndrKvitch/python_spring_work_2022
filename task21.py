#todo: Задан словарь, его значения необходимо внести по соответвющим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}

lines = list()
f = open("index.html.TXT", "r+")
for i in f:
    lines.append(i)
    if not i:
        break
f.close()
print(lines)
new_lines = list()
for i in lines:
        for key in page:
                if key in i:
                        print(lines.index(i))
                        num = i.find("?")
                        print(i[:num] + page[key] + i[num  + 1:])
                        new_lines.append(str(i[:num]) + str(page[key]) + str(i[num  + 1:]))
                        break
        else:
                new_lines.append(lines[lines.index(i)])
f = open("index.html.TXT", "at+")
f.writelines(new_lines)
f.close()