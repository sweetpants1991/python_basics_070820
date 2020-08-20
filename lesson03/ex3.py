# case3:
# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 <= arg2:
        return arg1 + arg2
    elif arg2 < arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3


print(f'Result - {my_func(int(input("1st argument ")),int(input("2nd argument ")), int(input("3rd argument ")))}')
