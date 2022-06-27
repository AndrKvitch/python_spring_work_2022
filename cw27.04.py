#todo: Создайте объект сериализации любым методом для соседа, запишите его в файл,
# педайте его ему для считывания. Соседу необходимо десириализовать полученый объект.

import json
#list = ['Ну шо ты?', "Голова", {"Возвраст": 13}]
#f = open("file_for_frend.pkl", "wb")
#pickle.dump(list, f, pickle.HIGHEST_PROTOCOL)
with open("data.json", "rb") as f:
    obj = json.load(f)
    print(obj)
#todo: Заданы два списка. Необходимо их сериализовать в один файл.
#import pickle
#list_one = [True, 'If the implementation is hard to explain, it\'s a bad idea.', {'age': 27}]
#list_two = [False, 'Sparse is better than dense.', {'age': 90}]
#f = open("serrial.pkl", "wb")
#pickle.dump(list_one, f, pickle.HIGHEST_PROTOCOL)
#pickle.dump(list_two, f, pickle.HIGHEST_PROTOCOL)