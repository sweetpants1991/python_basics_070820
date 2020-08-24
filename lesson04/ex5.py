# case5:
# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce


def my_func(e_items, items):
    return e_items * items


print(f'Even numbers {[items for items in range(99, 1001) if items % 2 == 0]}')
print(f'Multiply {reduce(my_func, [items for items in range(99, 1001) if items % 2 == 0])}')
