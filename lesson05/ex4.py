# case04:
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1; Two — 2; Three — 3; Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

russian = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
file = []
with open('file.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        file.append(russian[i[0]] + '  ' + i[1])
    print(file)

with open('file_russian.txt', 'w') as file_obj_2:
    file_obj_2.writelines(file)
