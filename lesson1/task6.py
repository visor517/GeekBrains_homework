# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен
# увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена
# составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = int(input('Введите а: '))
b = int(input('Введите b: '))

day = 1
distance = a

while distance < b:
    a = 1.1 * a
    distance += a
    day += 1

print(f'Спортсмен пробежит {b} километров в {day} день')