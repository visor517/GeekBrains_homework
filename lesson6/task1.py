# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера,
# создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep
import colorama     # без этого colorama.init() не срабатывает - NameError: name 'colorama' is not defined
from colorama import Fore, Style    # чтобы везде colorama. не писать
colorama.init()

class TrafficLight: # тут возможно можно цикл сделать, но по постановке задачи это не понятно
    __color = 'Красный'

    def running(self):
        print(Fore.RED + self.__color)
        sleep(7)
        self.__color = "Желтый"
        print(Fore.YELLOW + self.__color)
        sleep(2)
        self.__color = "Зеленый"
        print(Fore.GREEN + self.__color)
        sleep(7)
        self.__color = "Красный"
        print(Fore.RED + self.__color + Style.RESET_ALL)
      
a = TrafficLight()

a.running()
