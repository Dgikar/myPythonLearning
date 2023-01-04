"""
2. Створіть клас "Правильна дроба" та реалізуйте методи:
    - порівняння,
    - додавання,
    - віднімання,
    - множення
    для екземплярів цього класу.
"""


class ProperFractions:
    def __init__(self, denominator: int, devider: int):
        self.denominator = denominator
        self.devider = devider

    def __eq__(self, fraction):

        fractions1 = (self.denominator * fraction.devider,
                      self.devider * fraction.devider)

        fractions2 = (fraction.denominator * self.devider,
                      fraction.devider * self.devider)

        return fractions1 == fractions2

    def __add__(self, fraction):
        if self.devider == fraction.devider:
            self.denominator += fraction.denominator
            return self

        else:
            a = self.denominator
            b = self.devider
            c = fraction.denominator
            d = fraction.devider

            new_fractions_1 = a * d + c * b
            new_fractions_2 = b * d
            new_fractions = ProperFractions(new_fractions_1, new_fractions_2)

            return new_fractions

    def __sub__(self, fraction):
        if self.devider == fraction.devider:
            self.denominator -= fraction.denominator
            return self

        else:
            a = self.denominator
            b = self.devider
            c = fraction.denominator
            d = fraction.devider

            new_fractions_1 = a * d - c * b
            new_fractions_2 = b * d
            new_fractions = ProperFractions(new_fractions_1, new_fractions_2)

            return new_fractions

    def __mul__(self, fraction):
        denominator = self.denominator * fraction.denominator
        devider = self.devider * fraction.devider
        new = ProperFractions(denominator, devider)

        return new

    def __str__(self):
        return f"{str(self.denominator)}/{str(self.devider)}"
