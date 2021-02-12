# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из сотрудников
# имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

try:
    with open('text_3.txt', 'r', encoding='utf-8') as file:
        text = file.readlines()
        poor_persons = []
        total_income = 0.0

        for string in text:
            person = string.split()

            if float(person[1]) < 20000:
                poor_persons.append(person[0])
            
            total_income += float(person[1])

        print(f'Сотрудники получающие меньще 20000: {", ".join(poor_persons)}')
        print(f'Средняя виличина дохода сотрудников: {total_income / len(text)}')

except FileNotFoundError:
    print('Файл не найден!')