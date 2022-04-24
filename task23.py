#todo: Взлом шифра
#Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
#Попробуйте все возможные сдвиги и расшифруйте фразу.
#zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin

text = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin"
alf = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
       "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
       "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# алфавит ввел списком, т.к. при введении его строкой у меня получилось расшивровать послание, но не полкчилось
# вставить при расшифровке пробелы
otvet = ""

for i in text:
    try:
        mesto = alf.index(i)
        new_mesto = mesto - 6
        if i in alf:
            otvet += alf[new_mesto]
    except ValueError:
        otvet += i
print(otvet)