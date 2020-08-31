# case04:
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} started to final destination'

    def stop(self):
        return f'{self.name} just stopped'

    def turn_right(self):
        return f'{self.name} turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Your speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


priora = TownCar(30, 'White', 'Priora', False)
ferrari = SportCar(100, 'Red', 'Audi', False)
granta = WorkCar(70, 'Rose', 'Lada', True)
largus = PoliceCar(110, 'Blue',  'Ford', True)
print(granta.turn_right())
print(f'When {priora.turn_right()}, then {ferrari.stop()}')
print(f'{granta.go()} with speed exactly {granta.show_speed()}')
print(f'{granta.name} is {granta.color}')
print(f'Is {ferrari.name} a police car? {ferrari.is_police}')
print(f'Is {granta.name}  a police car? {granta.is_police}')
print(priora.show_speed())
print(ferrari.show_speed())
print(largus.show_speed())
print(largus.police())
