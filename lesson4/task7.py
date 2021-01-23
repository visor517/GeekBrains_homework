# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить только
# первые n чисел, начиная с 1! и до n!.

from functools import reduce

def fact(n):
    for el in [reduce(lambda x,y: x * y, range(1, x+1)) for x in range(1, n+1)]:
        yield el

while True:
    try:
        n = int(input('Введите n: '))
        break
    except ValueError:
        print('Введите целое число!') 

for el in fact(n):
    print(el)