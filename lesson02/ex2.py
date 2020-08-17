# case2:
# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

while True:
    elements = input("Please, put number here: ")
    if elements.isdigit():
        elements = int(elements)
        break

    print('This is not a number, try again: ')
list = []
qty = 0
item = 0
while qty < elements:
    list.append(input("Put next number is line: "))
    qty += 1

for item in range(int(len(list)/2)):
        list[item], list[item + 1] = list[item + 1], list[item]
        item += 2
print(list)





