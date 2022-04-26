#todo: Изучаем пакет pandas
#
# После установки библиотеки pandas выполните следующие действия:
#
# Изучите справку по модулю (для чего нужен модуль , какие возможности предоставляет)
# Найдите расположение директории модуля pandas и изучите его содержимое
# Получите список доступных атрибутов модуля pandas
# Импортируйте модуль pandas в исполняемый скрипт
# С помощью модуля pandas ознакомьтесь со структурой  DataFrame, фильтрации данных,
# загрузки данных из формата сsv (рассмотрите примеры статьи)
# Установите библиотеку matplotlib, создайте график на своем наборе данных.

#Опорная статья:  https://egorovegor.ru/pandas-obrabotka-i-analiz-dannyh-v-python/
#import pandas as pd

#df = pd.DataFrame({
 #   "Страна" : ["Россия", "Казахстан", "Украина", "Белоруссия", "Узбекистан"],
  #  "2017 год" : [1665, 179, 131, 60, 50],
   # "2018 год" : [1702, 182, 154, 63, 58],

#})
#df["Рост"] = df["2018 год"] - df["2017 год"]
#df.rename(columns={"2018 год": "2018", "2017 год": "2017"})
#df[df["2018 год"] &gt; 100]['Страна'] НЕ РАБОТАЕТ
#print(df)


import pandas as pd
file = pd.read_csv("annual-enterprise-survey-2020-financial-year-provisional-size-bands-csv.csv")
%matplotlib
import matplotlib.pyplot as plt

plt.plot(x = "year", y =["value", "year"])
plt.show()
