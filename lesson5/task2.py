# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

try:
    with open('task1.txt', 'r', encoding='utf-8') as file:
        text = file.readlines()
        print(f'Количество строк в файле: {len(text)}')
        for index, string in enumerate(text):
            print(f'Количество слов в строке {index + 1}: {len(string.split())}')
except FileNotFoundError:
    print('Файл не найден!')
    