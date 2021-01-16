# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
# “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = "Название"

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    title = "Ручка"
    def draw(self):
        print('Отрисовываем ручку!')

class Pencil(Stationery):
    title = "Карандаш"
    def draw(self):
        print('Отрисовываем карандаш!')

class Handle(Stationery):
    title = "Маркер"
    def draw(self):
        print('Отрисовываем маркер!')

pen_1 = Pen()
pencil_1 = Pencil()
handle_1 = Handle()

pen_1.draw()
pencil_1.draw()
handle_1.draw()