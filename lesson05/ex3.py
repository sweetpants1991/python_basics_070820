# case03:
# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('salary.txt', 'r') as file:
    salary = []
    poor = []
    coworkers = file.read().split('\n')
    for i in coworkers:
        i = i.split()
        if int(i[1]) < 20000:
            poor.append(i[0])
        salary.append(i[1])
print(f'Salary less then 20.000 {poor}, average: {sum(map(int, salary)) / len(salary)}')
