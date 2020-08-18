# case1:
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

while True:
    pos_arg1 = input("Please, input dividend here: ")
    if pos_arg1.isdigit():
        pos_arg1 = int(pos_arg1)
        break
    print("This is not a number, try again")
while True:
    pos_arg2 = input("Please input divider here: ")
    if pos_arg2.isdigit():
        pos_arg2 = int(pos_arg2)
        break
        print("This is not a number, try again")

def division(*args):
    try:
        result = pos_arg1 / pos_arg2
    except ValueError:
        return "You have a value error!"
    except ZeroDivisionError:
        return "wrong, Please check divider!"
    return result

print(f'Your result is {division()}')


