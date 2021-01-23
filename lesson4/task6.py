# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count, cycle
from random import randint

while True:
    try:
        smallest_number = int(input('Введите начально целое число меньше 30 для генирации: '))
        break
    except ValueError:
        print('Введите число!')

for el in count(smallest_number):
    if el > 30:
        break
    else:
        print(el)

# Б

your_list = input('Введите список элементо через пробел: ').split()

c = 0
for el in cycle(your_list):
    if c < 10:
        print(el)
        c += 1
