# case02:
# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Cloth:
    def __init__(self, v_size, h_size):
        self.v_size = v_size
        self.h_size = h_size

    def coat_area(self):
        return self.v_size / 6.5 + 0.5

    def jacket_area(self):
        return self.h_size * 2 + 0.3

    @property
    def full_area(self):
        return str(f'Total S {(self.v_size / 6.5 + 0.5) + (self.h_size * 2 + 0.3)}')


class Coat(Cloth):
    def __init__(self, v_size, h_size):
        super().__init__(v_size, h_size)
        self.square_c = round(self.v_size / 6.5 + 0.5)

    def __str__(self):
        return f'S for coat {self.square_c}'


class Jacket(Cloth):
    def __init__(self, v_size, h_size):
        super().__init__(v_size, h_size)
        self.square_j = round(self.h_size * 2 + 0.3)

    def __str__(self):
        return f'S for jacket {self.square_j}'


coat = Coat(14, 18)
jacket = Jacket(10, 18)
print(coat)
print(jacket)
print(coat.full_area)
print(jacket.full_area)
