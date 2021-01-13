# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

# создаем файл с числами
file = open('task5.txt', 'w', encoding='utf-8')

for i in range(0, 10):
    file.write(f'{randint(0, 1000)} ')

file.close()

with open('task5.txt', 'r', encoding='utf-8') as file:
    result = 0
    for number in file.read().split():
        result += int(number)
    print(f'Сумма чисел в файле {file.name}: {result}')
