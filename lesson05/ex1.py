# case01:
# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

file = open('test.txt', 'w')
line = input('Enter text \n')
while line:
    file.writelines(line)
    line = input('Enter text \n')
    if not line:
        break

file.close()
file = open('test.txt', 'r')
content = file.readlines()
print(content)
file.close()
