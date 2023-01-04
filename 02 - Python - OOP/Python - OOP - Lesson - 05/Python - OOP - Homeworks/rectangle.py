"""
1. Створіть клас «Прямокутник», у якого є два поля (ширина і висота).
    Реалізуйте метод порівняння прямокутників за площею. Також реалізуйте методи складання прямокутників
    (площа сумарного прямокутника повинна дорівнювати сумі площ прямокутників, які ви складаєте).

    Реалізуйте методи множення прямокутника на число n (це має збільшити площу базового прямокутника в n разів).
"""


class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.length = height

    def square(self):
        return self.length * self.width

    def __eq__(self, other):
        return self.square() == other.square()

    def __add__(self, other):
        return Rectangle(1, self.square() + other.square())

    def __mul__(self, number):
        return self.square() * number

    def __str__(self) -> str:
        return f"   ширина: {self.width}\n" \
               f"       висота: {self.length}\n" \
               f"       {'-' * 14}\n" \
               f"       його площа = {self.square()}"
