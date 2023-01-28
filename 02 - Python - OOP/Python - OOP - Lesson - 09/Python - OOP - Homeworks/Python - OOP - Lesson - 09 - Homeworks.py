"""
1. Створіть декоратор, який підраховуватиме, скільки разів була викликана функція, що декорується.
"""


class counter_decorator:
    """ Кастомний декоратор """

    def __init__(self, function):
        self.count = 0
        self.function = function

    def __call__(self, x, y, operator="+"):
        self.count += 1
        return self.function(x, y, operator)


@counter_decorator
def some_function(x, y, operator):
    """ Вибір дії """

    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
        "//": lambda x, y: x // y,
        "**": lambda x, y: x ** y
    }

    action_operator = operators.get(operator)

    return f"{x} {operator} {y} = {action_operator(x, y)}"


print("-" * 77, "\n")

print(f"Результат роботи: {some_function(10, 2)}\n\t"
      f"Виклик {type(some_function)} №: {some_function.count}")

print("-" * 56)

print(f"Результат роботи: {some_function(-3, 5, '-')}\n\t"
      f"Виклик {type(some_function)} №: {some_function.count}")

print("-" * 56)

print(f"Результат роботи: {some_function(20, 4, '*')}\n\t"
      f"Виклик {type(some_function)} №: {some_function.count}")
# -------------------------------------------

"""
2. Створіть декоратор, який зареєструє функцію, що декорується, у списку функцій, для обробки послідовності.
"""
function_list = []


def func_list_decorator(some_func):
    """ Decorator """

    def wrapper():
        """ Wrapper """

        function_list.append(some_func)

        return function_list

    return wrapper


@func_list_decorator
def first_function():
    """ Це просто функція """

    return "Це перша функція"


@func_list_decorator
def second_function(lst, multiplier):
    """ Ця функція множить елементи списку some_list """

    return [i * multiplier for i in lst]


some_list = [1, 2, 3, 4, 5]

print()
print("*" * 77)
print(f"Функція зареєстрована як: {first_function()}")
print(f"Тепер зареєстровано такі функції: {second_function()}")

print()
print(f"Маємо список: [1, 2, 3, 4, 5]\n\t"
      f"Після множення,маємо такий список: {function_list[1](some_list, 3)}")
# -------------------------------------------

"""
3. Припустимо, у класі визначено метод __str__, який повертає рядок на підставі класу.
    Створіть такий декоратор для цього методу, щоб отриманий рядок зберігався у текстовий файл, ім'я якого збігається з
    ім'ям класу, метод якого ви декорували.
"""


def save_to_file_decorator(func):
    """ Decorator """

    def wrapper(class_name):
        """ Wrapper """

        class_name_str = class_name.__class__.__name__

        with open(f"{class_name_str}.txt", encoding='utf-8', mode='w') as f:
            f.write(func(class_name))

        return func(class_name)

    return wrapper


class Person:
    """ Просто клас """

    def __init__(self, surname, name, patronymic, birthdate):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birthdate = birthdate

    @save_to_file_decorator
    def __str__(self):
        return f"Збережено: {self.surname} {self.name} {self.patronymic}. Дата народження: {self.birthdate}"


person1 = Person("Петров", "Петро", "Петрович", "24.08.1975")

print()
print("*" * 77)
print(person1)
