# case1:
# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

var1_int = int(7)
var2_float = float(42.88)
var3_str = str("Artem 1991")
print(var1_int, var2_float, var3_str)

var4 = input("Text here something - ")
print("You text", var4)

# case2:
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input("Enter your time in seconds here: "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = (time - (hours * 3600 + minutes * 60))
print(f"Time format hh:mm:ss {hours} : {minutes} : {seconds}")

# case3:
# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

num = input("Please, input number: ")
var1 = int(num + num)
var2 = int(num + num + num)
var3 = int(num) + var1 + var2
print(var3)

# case4:
# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num1 = input("Please, input number: ")
var_x = 0
for var_y in num1:
    while int(var_y) > var_x:
        var_x = int(var_y)
print(var_x)

# case5:
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки)
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceeds = int(input("Please, input your proceeds: "))
costs = int(input("Please, input your costs: "))
if proceeds > costs:
    profit = proceeds - costs
    profitability = float(profit / proceeds)
    print("You have profit: ", profit)
    worker = int(input("Please, input number of workers: "))
    profit_per_worker = float(profit / worker)
    print("Your profit per worker: ", profit_per_worker)
elif proceeds == costs:
    print("You try to make ends meet")
else:
    print("You have loss")
