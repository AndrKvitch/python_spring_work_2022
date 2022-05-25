#todo: Убрать повторяющиеся буквы и лишние символы
#Построить по ключевой фразе часть алфавита. Взять все буквы по одному разу. Не буквы убрать.
#Буквы должны идти в том порядке, в котором встретились во фразе в первый раз.

#Input             	            Output
#apple	                        aple
#25.04.2022 Good morning !!	    godmrni

text = input("Enter word: ")
x = ''.join(sorted(set(text), key = text.index))
print(x)
text2 = input("Введите ключевую фразу для построения части алфавита: ")
text2 = text2.lower()
new_text = ""
for letter in text2:
    if letter.isalpha():
        if letter not in new_text:
            new_text += letter
print(new_text)
