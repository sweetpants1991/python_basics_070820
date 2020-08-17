# case5:
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

user_list = [91, 42, 19, 19, 8]
while True:
    user_number = input('Please, put number here: ')
    if user_number.isdigit():
        user_number = int(user_number)
        break
    print('This is not a number, try again: ')
amt = user_list.count(user_number)
for item in user_list:
    if amt > 0:
        qty1 = user_list.index(user_number)
        user_list.insert(qty1+amt, user_number)
        break
    else:
        if user_number > item:
            qty2 = user_list.index(item)
            user_list.insert(qty2, user_number)
            break
        elif user_number < user_list[len(user_list) - 1]:
            user_list.append(user_number)
print(user_list)