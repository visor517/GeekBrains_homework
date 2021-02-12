# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Imaginary_numbers:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f'{self.real}+{self.imaginary}i'

    def __add__(self,other):
        return Imaginary_numbers(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self,other):
        return Imaginary_numbers(self.real * other.real - self.imaginary * other.imaginary, self.real * other. imaginary + self.imaginary * other.real)


imaginary_1 = Imaginary_numbers(7,2)
imaginary_2 = Imaginary_numbers(5,1)

print(imaginary_1 + imaginary_2)
print(imaginary_1 * imaginary_2)