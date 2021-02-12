# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.


def my_func(x, y):
    result = 1
    for z in range(1, abs(y)+1):
        result = result / x
    return result


while True:
    try:
        x = float(input('Введите действительное положительное число Х: '))
        if x > 0:
            break
        else:
            print('Число не положительное')
    except ValueError:
        print('Введено не число')


while True:
    try:
        y = int(input('Введите целое отрицательное число Y: '))
        if y < 0:
            break
        else:
            print('Число не отрицательное')
    except ValueError:
        print('Ошибка ввода')

print(my_func(x, y))
