# case2:
# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.

numbers_v1 = [42, 14, 88, 1991, 19, 8, 2020, 666]
numbers_v2 = [items for items in numbers_v1 if items > numbers_v1[numbers_v1.index(items)-1]]

print(f'Generated {numbers_v2}')
