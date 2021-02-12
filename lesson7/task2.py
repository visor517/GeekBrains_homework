# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь
# определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост
# (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих
# методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов
# проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Сlothes(ABC):
    name = "name"

    @abstractmethod
    def consumption(self):
        pass

class Coat(Сlothes):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @property
    def consumption(self):
        return self.size / 6.5 + 0.5

class Suit(Сlothes):
    def __init__(self, name, height):
        self.name = name
        self.height = height

    @property
    def consumption(self):
        return 2 * self.height + 0.3

coat_1 = Coat("Пальто", 54)
suit_1 = Suit("Костюм", 6)

print(suit_1.consumption + coat_1.consumption)
