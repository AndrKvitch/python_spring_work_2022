#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
#– id - номер по порядку (от 1 до 10);
#– текст из списка algoritm
#Каждое значение из списка должно находится на отдельной строке.

f = open("algoritm.csv", mode="at")
algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]
count = 0
for i in algoritm:
    if i in algoritm:
        count += 1
    f.write(str(count))
    f.write(i)
    f.write("\n")
f.close()