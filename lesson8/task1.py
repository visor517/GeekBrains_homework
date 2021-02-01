# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен
# проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

import re

class Data:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_date(cls,param):
        if cls.validate(param):
            date_arr = param.split("-")
            return [int(item) for item in date_arr] #из задания непонятно куда извлекать число, поэтому метод возвращает список чисел или сообщение об ошибке
        return "Параметр не прошел валидацию"

    @staticmethod
    def validate(date):
        if re.match(r'^(\d{1,2}-){2}\d{4}$',date): #проверяем формат
            date_arr = date.split("-")
            day = int(date_arr[0])
            month = int(date_arr[1])
            year = int(date_arr[2])
            if (month <= 12) & (month > 0) & (year <= 2021) & (year > 1900): #проверяем числа
                upper_limit = [31,28,31,30,31,30,31,31,30,31,30,31]
                if (day <= upper_limit[month-1]) & (day > 0):
                    return True 
        return False

print(Data.validate("27-2-2007"))
print(Data.get_date("1-02-2005"))
