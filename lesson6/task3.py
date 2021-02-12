# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). Последний атрибут
# должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position
# (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:
    name = "Имя"
    surname = "Фамилия"
    position = "Должность"
    _income = {"wage": 0, "bonus": 0}

class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income["wage"] = wage
        self._income["bonus"] = bonus

    def get_full_name(self):
        print(f'Работник: { self.name } { self.surname }')

    def get_total_income(self):
        print(f'Итоговый доход: { self._income["wage"] + self._income["bonus"] }')

person = Position('Иван', 'Иванов', 'Слесарь', 15000, 5000)

person.get_full_name()
person.get_total_income()