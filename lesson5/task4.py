# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

vocabulary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

try:
    with open('text_4.txt', 'r', encoding='utf-8') as file:
        result = open('task_4_result.txt', 'w', encoding='utf-8')

        while True:
            string = file.readline()
            for word, value in vocabulary.items():
                string = string.replace(word, value)   
            result.write(string)
            if not string:
                break
            
        result.close()

except FileNotFoundError:
    print('Файл не найден!')