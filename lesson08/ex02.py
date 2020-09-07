# case02:
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class DivisionByZero:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def divide_by_zero(numerator, denominator):
        try:
            return (numerator / denominator)
        except: ZeroDivisionError


div = DivisionByZero(4, 8)
print(DivisionByZero.divide_by_zero(2020, 0))
print(div.divide_by_zero(100, 0))
