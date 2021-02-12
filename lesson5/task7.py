# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также
# добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

try:
    with open('text_7.txt', 'r', encoding='utf-8') as file:
        
        vocabulary = {}
        total_profit = 0
        lucky_firms = 0
        for line in file:
            firm_data = line.split()
            profit = int(firm_data[2]) - int(firm_data[3])
            vocabulary[firm_data[0]] = profit
            if profit > 0:
                total_profit += profit
                lucky_firms += 1

        data = [vocabulary, {'average_profit': total_profit / lucky_firms}]

except FileNotFoundError:
    print('Файл не найден!')


with open('task_7_result.json', 'w', encoding='utf-8') as result:
    json.dump(data, result, ensure_ascii=False) #без ensure_ascii=False у меня Сказка записывалась как \u0421\u043a\u0430\u0437\u043a\u0430