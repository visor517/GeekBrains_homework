# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с
# прописной первой буквой. Например, print(int_func(‘text’)) -> Text.


def int_func(word):
    return word.title()


string = input('Введите строку из слов, разделенных пробелом: ')
arr = string.split(' ')
for index, item in enumerate(arr):
    arr[index] = int_func(item)

print(' '.join(arr))
