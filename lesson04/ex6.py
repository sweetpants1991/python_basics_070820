# case6:
# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного.

from itertools import count
from itertools import cycle


def func_count(first_num, last_num):
    for items in count(first_num):
        if items > last_num:
            break
        else:
            print(items)


func_count(first_num=int(input("Please, input first number: ")), last_num=int(input("Please, input last number: ")))

# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.


def func_cycle(list_1, iteration):
    i = 0
    iter_1 = cycle(list_1)
    while i < iteration:
        print(next(iter_1))
        i += 1


func_cycle(list_1=[1, 2], iteration=int(input("Please, input iteration: ")))
