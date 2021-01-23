# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.
def my_func(*args):
    result = sum(args) - min(args)
    return result

print(my_func(44, 17, 26))
