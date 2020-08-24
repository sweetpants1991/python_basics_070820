# case1:
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

def calculation():
    try:
        per_hour = float(input('Please, input output per hour: '))
        wage = int(input('Please, input wage: '))
        award = int(input('Please, input award: '))
        salary = per_hour * wage + award
        print(f'Your salary is :  {salary}')
    except ValueError:
        return print('Not a number')


calculation()
