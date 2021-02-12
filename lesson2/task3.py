# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
# месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
month = int(input('3: Введите месяц в виде целого числа от 1 до 12: '))

if month in range(3, 6):
    result = 'Весна'
elif month in range(6, 9):
    result = 'Лето'
elif month in range(9, 12):
    result = 'Осень'
elif month in range(1, 3) or 12:
    result = 'Зима'
else:
    result = 'Введено неподходящее значение!'

print(result)
