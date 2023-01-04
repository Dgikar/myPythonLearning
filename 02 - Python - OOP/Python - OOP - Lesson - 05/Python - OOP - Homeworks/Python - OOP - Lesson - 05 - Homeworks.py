"""
Useful Links:
    PEP 257 – Docstring Conventions - https://peps.python.org/pep-0257
    PEP 0 – Index of Python Enhancement Proposals (PEPs) - https://peps.python.org/pep-0000
    Действия с дробями - http://spacemath.xyz/deistviya_s_drobyami
-------------------------------------------
"""
import rectangle
import fractions

"""
1. Створіть клас «Прямокутник», у якого є два поля (ширина і висота).
    Реалізуйте метод порівняння прямокутників за площею. Також реалізуйте методи складання прямокутників
    (площа сумарного прямокутника повинна дорівнювати сумі площ прямокутників, які ви складаєте).

    Реалізуйте методи множення прямокутника на число n (це має збільшити площу базового прямокутника в n разів).
"""
if __name__ == "__main__":
    print(f'{"-" * 42}\nДомашне завдання №1 - клас "Прямокутник":')
    rectangle1 = rectangle.Rectangle(5.5, 7.5)
    rectangle2 = rectangle.Rectangle(12, 8)

    rectangle3 = rectangle1 + rectangle2

    print(f"{'-' * 42}\n    Прямокутник 1:\n    {rectangle1}")
    print(f"    {'-' * 21}\n    Прямокутник 2:\n    {rectangle2}")
    print(f"    {'-' * 21}\n    Порівняння прямокутника 1 та 2: {rectangle1 == rectangle2}")
    print(f"    {'-' * 21}\n    Прямокутник 3 (складання прямокутників 1 та 2). Його площа = {rectangle3.square()}")
    print(f"    {'-' * 21}\n    Множення площі прямокутника 3 на число n (зокрема на 2): {rectangle3 * 2}")
    # -------------------------------------------

    """
    2. Створіть клас "Правильна дроба" та реалізуйте методи:
        - порівняння,
        - додавання,
        - віднімання, 
        - множення 
        для екземплярів цього класу.
    """
    print(f"\n{'-' * 42}\nДомашне завдання №2 - Правильні дроби\n{'-' * 42}")
    fractions1 = fractions.ProperFractions(2, 2)
    fractions2 = fractions.ProperFractions(5, 5)

    print(f"    Перша введена дроба - {fractions1}")
    print(f"    Друга введена дроба - {fractions2}")
    print(f"    {'-' * 35}\n    Порівняння дробів 1 та 2: {fractions1 == fractions2}")
    print(f"    {'-' * 35}\n    Додавання дроби 2 до дроби 1: {fractions1 + fractions2}")
    print(f"    {'-' * 35}\n    Віднімання дроби 1 від дроби 2: {fractions1 - fractions2}")
    print(f"    {'-' * 35}\n    Множення дробів 1 та 2: {fractions1 * fractions2}")
