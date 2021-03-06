# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У
# пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться после них.

rate = [7, 5, 3, 3, 2]
print(f'5: {rate}')
mark = int(input('Введите новый элемент рейтинга: '))

if rate[-1] < mark:
    for index, item in enumerate(rate):
        if mark > item:     # индекс первого числа меньше введенного
            break

    result = rate[:index] + [mark] + rate[index:]
else:
    result = rate + [mark]

print(result)
