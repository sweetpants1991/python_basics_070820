# case4:
# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

numbers_v1 = [42, 42, 14, 88, 1991, 1991, 8, 8, 2020, 2020, 666, 666]
numbers_v2 = [items for items in numbers_v1 if numbers_v1.count(items) < 2]

print(f'Generated {numbers_v2}, :)')
