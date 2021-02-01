# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
# нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

dividend = int(input("Введите делимое: "))

divider = int(input("Введите делитель: "))

try:
    if divider == 0:
        raise OwnError("На ноль делить нельзя")
except OwnError as err:
    print(err)
else:
    print(f'Результат деления: {dividend / divider}')
    