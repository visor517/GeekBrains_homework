# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
# у пользователя, предусмотреть обработку ситуации деления на ноль.
def collector(message):
    while True:
        try:
            return float(input(f'Введите {message}: '))
            break
        except ValueError:
            print('Вводите число!')


def division(dividend, divider):
    try:
        result = dividend / divider
    except ZeroDivisionError:
        return 'На 0 делить нельзя!'
    return result


print(division(collector('делимое'), collector('делитель')))

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год
# рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
def unifier(**kwargs):
    return kwargs


print(unifier(name="Иван", patronymic="Иванович", surname="Иванов", age=1945, city="Stockholm", email="none@mail.by", phone="0071236745"))

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.
def my_func(*args):
    result = sum(args) - min(args)
    return result


print(my_func(44, 17, 26))

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

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь
# введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.
result = 0


def adder(arr):
    global result
    for item in arr:
        try:
            if item != 'q':
                item = float(item)
                result = result + item
            else:
                return True
        except ValueError:
            pass
    return False


while True:
    string = input('Введите строку чисел, разделенных пробелом. Или q для выхода: ')
    arr = string.split(' ')
    if adder(arr):
        break
    print(f'Промежуточный результат: {result}')

print(f'Итоговая сумма {result}')

# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с
# прописной первой буквой. Например, print(int_func(‘text’)) -> Text.


def int_func(word):
    return word.title()


string = input('Введите строку из слов, разделенных пробелом: ')
arr = string.split(' ')
for index, item in enumerate(arr):
    arr[index] = int_func(item)

print(' '.join(arr))

