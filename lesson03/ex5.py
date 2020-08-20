# case5:
# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def summary():
    summary_result = 0
    exception = False
    while exception == False:
        number = input('Input numbers or Q for quit - ').split()
        result = 0
        for item in range(len(number)):
            if number[item] == 'q' or number[item] == 'Q':
                exception = True
                break
            else:
                result = result + int(number[item])
        summary_result = summary_result + result
        print(f'Current sum is {summary_result}')
    print(f'Your final sum is {summary_result}')


summary()

