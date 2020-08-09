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
