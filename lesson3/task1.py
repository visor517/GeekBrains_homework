# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
# у пользователя, предусмотреть обработку ситуации деления на ноль.

def collector(message):
    while True:
        try:
            return float(input(f'Введите {message}: '))

        except ValueError:
            print('Вводите число!')


def division(dividend, divider):
    try:
        result = dividend / divider
    except ZeroDivisionError:
        return 'На 0 делить нельзя!'
    return result

print(division(collector('делимое'), collector('делитель')))