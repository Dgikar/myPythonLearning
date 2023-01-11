"""
Useful Links:
    HTML Tutorial - https://www.w3schools.com/html
    CSS Tutorial - https://www.w3schools.com/css/default.asp
    Bootstrap 5 Tutorial - https://www.w3schools.com/bootstrap5/index.php
-------------------------------------------

1. Реалізуйте генераторну функцію, яка повертатиме по одному члену геометричної прогресії із зазначеним множником.
    Генератор повинен зупинити свою роботу або після досягнення зазначеного елементу, або при передачі команди на
     завершення.
"""


def geometric_progression(denominator: int, stop: int):
    """ Генератор геометричної прогресії """

    start = 1

    while start * denominator <= stop:
        yield f"{start} * {denominator} = {start * denominator}"
        start += 1

    return


print("-" * 42)
print("Генератор геометричної прогресії:")
for i in geometric_progression(7, 70):
    print(f"    {i}")

print("-" * 35)
# -------------------------------------------

"""
2. Реалізуйте свій аналог генераторної функції range()
"""


def range_func(*args, **kwargs):
    """ Кастомна функція range() """

    if not args or len(args) > 3:
        raise TypeError

    start = args[0] if len(args) >= 2 else 0
    stop = args[1] if len(args) >= 2 else args[0]
    step = args[2] if len(args) == 3 else 1

    if not step:
        raise ValueError

    if start < 0 and stop > start:
        return

    if step > 0 and stop < start:
        return

    while start < stop:
        yield start
        start += step

    return


range1 = range_func(4, 20, 2)

print("Кастомна функція range():")
for i in range1:
    print(f"    {i}")

print("-" * 35)
# -------------------------------------------

"""
3. Напишіть функцію-генератор, яка повертатиме прості числа.
    Верхня межа діапазону повинна бути задана параметром цієї функції.
"""


def prime_numbers(multiplier_args):
    """ Функція-генератор простих чисел """

    start = 2

    while start <= multiplier_args:
        prime_numbers_list = [1 for i in range(2, start + 1) if start % i == 0]

        if len(prime_numbers_list) > 1:
            start += 1
            continue

        else:
            yield start

        start += 1

    return


print("Функція-генератор простих чисел:")
for i in prime_numbers(25):
    print(f"    {i}")

print("-" * 35)
# -------------------------------------------

"""
4. Напишіть генераторний вираз для заповнення списку.
    Список повинен бути заповнений кубами чисел від 2 до вказаної вами величини.
"""


def numbers_list(entry_args):
    """ Генератор від 2 до вказаної величини """

    return (i ** 3 for i in range(2, entry_args))


print('Генератор чисел в кубі:\n   ', *numbers_list(10))
