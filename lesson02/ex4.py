# case4:
# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_string = str(input("Please, input something else here: "))
user_wd = []
user_string_number = 1
for item in range(user_string.count(' ') + 1):
    user_wd = user_string.split()
    if len(str(user_wd)) <= 10:
        print(f"{user_string_number} {user_wd [item]}")
        user_string_number += 1
    else:
        print(f"{user_string_number} {user_wd [item] [0:10]}")
        user_string_number += 1
