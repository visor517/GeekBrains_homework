# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь
# введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.
result = 0


def adder(arr):
    global result
    for item in arr:
        try:
            if item != 'q':
                item = float(item)
                result = result + item
            else:
                return True
        except ValueError:
            pass
    return False


while True:
    string = input('Введите строку чисел, разделенных пробелом. Или q для выхода: ')
    arr = string.split(' ')
    if adder(arr):
        break
    print(f'Промежуточный результат: {result}')

print(f'Итоговая сумма {result}')
