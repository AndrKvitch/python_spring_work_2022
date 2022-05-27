#todo: Числа в буквы
#Замените числа, написанные через пробел, на буквы. Не числа не изменять.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def num_text(alphabet, num_str):
    num_list = num_str.split(" ")
    out_text = " "
    for i in num_list:
        if i.isdigit() == True:
            if int(i) == 0:
                out_text += (" ")
            elif int(i) > 0:
                out_text += (alphabet[int(i) - 1])
            else:
                continue
        else:
            out_text += i
    return (out_text)
input_str = input("Введите цифры через пробел: ")
output_str = num_text(alphabet, input_str)
print(output_str)