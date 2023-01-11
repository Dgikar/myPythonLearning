"""
Useful Links:
    typing - Support for type hints - https://docs.python.org/3/library/typing.html
    argparse - налізатор параметрів командного рядка, аргументів і підкоманд - https://docs.python.org/uk/3/library/argparse.html
    Патерн проектирования "Декоратор" / "Decorator" - https://habr.com/ru/post/86255
    Фабричный метод на Python:
        https://webdevblog.ru/shablon-fabrichnogo-metoda-i-ego-realizaciya-v-python
        https://refactoring.guru/ru/design-patterns/factory-method

    Патерн проектирования программ "Абстрактная фабрика (Abstract Factory)":
        https://www.youtube.com/watch?v=WNuH2ZDdeu0
        https://evileg.com/ru/post/381
        https://proglib.io/p/py-patterns
-------------------------------------------

1. Реалізуйте генераторну функцію, яка повертатиме по одному члену числової послідовності, закон якої задається за
    допомогою функції користувача. Крім цього параметром генераторної функції повинні бути значення першого члена
    прогресії та кількість членів, що видаються послідовністю.

    Генератор повинен зупинити свою роботу або по досягненню n-го члена, або при передачі команди на завершення.
"""


def generation_func(first_member_of_progression, n_member):
    """ Генераторна функцію, яка повертає по одному члену числової послідовності """

    def count():
        nonlocal first_member_of_progression
        first_member_of_progression += first_member_of_progression
        return first_member_of_progression

    for i in range(n_member):
        yield first_member_of_progression
        first_member_of_progression = count()
    return


print("-" * 35)
print("Генераторна функцію. Повертає по одному члену числової послідовності:")
for i in generation_func(1, 5):
    print(f"    {i}")
# -------------------------------------------

"""
2. Використовуючи замикання, реалізуйте такий прийом програмування як Мемоізація:
    https://en.wikipedia.org/wiki/Memoization

    Використовуйте отриманий механізм для прискорення функції рекурсивного обчислення n - го члена ряду Фібоначчі.

    Порівняйте швидкість виконання із просто рекурсивним підходом.
"""

import time


def fibonacci():
    """ Мемоізація """

    serial_numbers = {}
    first_number = 0
    second_number = 1

    def next_number(number):
        nonlocal first_number
        nonlocal second_number

        if number in serial_numbers:
            return serial_numbers[number]

        elif number == 0:
            serial_numbers[number] = 0

        elif number == 1:
            serial_numbers[number] = 1

        else:
            next_number = first_number + second_number
            first_number = second_number
            second_number = next_number
            serial_numbers[number] = next_number

        return serial_numbers[number]

    return next_number


start = time.time()
fibo = fibonacci()

print("-" * 35)
print("Генераторна функцію. Повертає по одному члену числової послідовності:")
for i in range(20):
    print(f"    {fibo(i)}")

print("-" * 35)
print("Час: ", time.time() - start)
# -------------------------------------------

"""
3. Напишіть функцію, яка застосує до списку чисел довільну функцію користувача і поверне суми елементів отриманого списку.
"""


def sum_list(list, func):
    """ Функція, яка застосує до списку чисел довільну функцію користувача """

    return sum(func(number) for number in list)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temp = lambda x: x / 2

print("-" * 35)
print("Функція, яка застосує до списку чисел довільну функцію користувача:", sum_list(list, temp))
