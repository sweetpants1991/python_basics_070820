# case02:
# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.

class Road:
    def __init__(self, __length, __width, __weigth, __tickness):
        self.__length = __length
        self.__width = __width
        self.__weigth = __weigth
        self.__tickness = __tickness
        print('Create new object')

    def intake(self):
        self.__weigth = 25
        self.__tickness = 0.05
        intake = self.__length * self.__width * self.__weigth * self.__tickness / 1000
        print(f'Need {intake} ton for the building')


obj_road = Road(20000, 6, 25, 0.05)
obj_road.intake()

