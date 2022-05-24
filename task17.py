# todo: Создайте функцию compute_bill, считающаю итоговую сумму товаров в чеке.
# Функция должна принимать 1 параметр - словарь, в котором указано количество едениц товара.
# Цены хранятся в словаре:
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def compute_bill(prices):
    check = dict()
    total = 0
    for key in prices:
        print(key)
        check[key] = float(input("Введите колличество товара: ")) * prices[key]
        total += check[key]
    return total
print(compute_bill(prices))