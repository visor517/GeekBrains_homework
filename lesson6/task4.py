# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в
# базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    speed = 0
    color = 'red'
    name = 'SimpleCar'
    is_police = False

    def go(self, speed):
        self.speed = speed
        print(f'Машина {self.name} разогналась до {self.speed} км/ч')

    def stop(self):
        self.speed = 0
        print(f'Машина {self.name} остановилась до {self.speed}')

    def turn(self, direction):
        print(f'Поворот {direction}')

    def show_speed(self):
        print(f'Скорость: {self.speed} км/ч')

class TownCar(Car):
    def show_speed(self,):
        super().show_speed()
        if self.speed > 60:
            print(f'Скорость превышена на {self.speed - 60} км/ч!')

class WorkCar(Car):
    name = 'Work Car'
    color = 'Yellow'
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Скорость превышена на {self.speed - 40} км/ч!')

class PoliceCar(Car):
    name = 'Police'
    color = 'White'
    is_police = True

class SportCar(Car):
    name = 'Sport Car'

car_1 = TownCar()
car_2 = WorkCar()
car_3 = SportCar()
car_4 = PoliceCar()

car_1.go(70)
car_1.show_speed()
car_1.stop()

print('\n')

car_2.go(40)
car_2.turn('вправо')
car_2.show_speed()

print('\n')

car_3.go(80)
car_3.show_speed()
print(f'Скорость {car_3.name} - {car_3.speed} км/ч')

print('\n')

car_4.go(80)
car_4.stop()
print(f'Цвет {car_4.name} - {car_4.color}')