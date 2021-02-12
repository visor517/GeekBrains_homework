# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

file = open('task1.txt', 'w', encoding='utf-8')

while True:
    string = input('Введите строку: ')
    if string == '':
        break
    file.write(f'{string}\n')

file.close