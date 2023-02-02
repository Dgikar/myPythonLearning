"""
Useful Links:
    Качина типізація - https://www.youtube.com/watch?v=MwsIOSZAkN8
    ABC (Абстрактный базовый класс) - https://habr.com/ru/post/72757
    Декомпозиція:
        https://python-course.readthedocs.io/projects/year2/en/latest/lessons/04-decomposition.html

    SOLID - https://habr.com/ru/company/otus/blog/651753
    Single Responsibility - https://www.pythontutorial.net/python-oop/python-single-responsibility-principle
    Write Better Python Code - https://github.com/ArjanCodes/betterpython
-------------------------------------------

1. Створіть декоратор, який зареєструє клас, що декорується, у списку класів.
"""
class_list = []


def class_registration(cls):
    class_list.append(cls)

    def wrapper(*args, **kwargs):
        new_instance = cls(*args, **kwargs)

        return new_instance

    return wrapper


@class_registration
class Person:
    def __init__(self, surname, name, patronymic, birthdate):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birthdate = birthdate

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}. Дата народження: {self.birthdate}"


@class_registration
class Group:
    def __init__(self, group_name):
        self.group_name = group_name

    def __str__(self):
        return self.group_name


person = Person("Петров", "Петро", "Петрович", "24.08.1975")
group = Group("Python")

print("-" * 77, "\n")
print("Завдання №1:")

print(f"\tЗареєстровано: {class_list}")
# -------------------------------------------

"""
2. Створіть клас декоратора з параметром.
    Параметром має бути рядок, який повинен дописуватись (ліворуч) до результату роботи методу __str__.
"""


def add_str_to_left(string):
    def concatenate(cls):
        def create_string(*args, **kwargs):
            return f"{string} {cls(*args, **kwargs)}"

        return create_string

    return concatenate


@add_str_to_left('Збережено:')
class Person:

    def __init__(self, surname, name, patronymic, birthdate):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birthdate = birthdate

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}. Дата народження: {self.birthdate}"


person = Person("Петров", "Петро", "Петрович", "24.08.1975")

print("-" * 77, "\n")
print("Завдання №2:")

print("\t", person)
# -------------------------------------------

"""
3. Для класу Box напишіть статичний метод, який підраховуватиме сумарний обсяг двох ящиків, які будуть його параметрами.
"""


class Box:

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def box_volume(self):
        return self.length * self.width * self.height

    @staticmethod
    def total_volume_of_boxes(box_1_volume, box_2_volume):
        return f"Загальний об'єм = {box_1_volume.box_volume() + box_2_volume.box_volume()}"

    def __str__(self):
        return f"Ящик:\n\t\t" \
               f"Довжина = {self.length}\n\t\t" \
               f"Ширина = {self.width}\n\t\t" \
               f"Висота = {self.height}\n\t\t\t" \
               f"Об'єм = {self.box_volume()}"


box_1 = Box(5, 7, 2)
box_2 = Box(2, 7, 5)

print("-" * 77, "\n")
print("Завдання №3:")

print("\t", box_1, "\n")
print("\t", box_2, "\n")
print("\t", Box.total_volume_of_boxes(box_1, box_2))
# -------------------------------------------

"""
4. Створіть дескриптор, який робитиме поля класу керовані ним доступними лише для читання.
"""


class PersonDescriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance_self, instance_class):
        return self.value

    def __set__(self, instance_self, value):
        raise AttributeError("Ви не можете змінити цей атрибут")

    def __delete__(self, instance_self):
        raise AttributeError("Ви не можете змінити цей атрибут")


class Person:
    def __init__(self, surname, name, patronymic, birthdate):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birthdate = birthdate

    def __str__(self):
        txt = "Громадянин:\n\t\t"

        for key in self.__dict__:
            txt = txt + key.title() + ": " + str(self.__dict__[key]) + "\n\t\t"

        return txt

    nationality = PersonDescriptor("\tУкраїнець")


person = Person("Петров", "Петро", "Петрович", "24.08.1975")

print("-" * 77, "\n")
print("Завдання №4:")

print("\t", person)
print("\t", person.nationality)
# -------------------------------------------

"""
5. Реалізуйте функціонал, який заборонятиме встановлення полів класу будь-якими значеннями, крім цілих чисел.
    Тобто, якщо тому чи іншому полю спробувати присвоїти, наприклад, рядок, то має бути збуджено виняток.
"""


class Person:
    def __init__(self, surname, name, patronymic, age):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.age = age

    def __str__(self):
        txt = "Громадянин:\n\t\t"

        for key in self.__dict__:
            txt = txt + key.title() + ": " + str(self.__dict__[key]) + "\n\t\t"
        return txt

    def __setattr__(self, atr_name, atr_value):
        if atr_name == "age":
            if isinstance(atr_value, int):
                self.__dict__[atr_name] = atr_value
            else:
                raise ValueError("Вік може бути лише цілим числом")
        self.__dict__[atr_name] = atr_value


person = Person("Петров", "Петро", "Петрович", 45)

print("-" * 77, "\n")
print("Завдання №5:")

print("\t", person)
person.age = 25
# person.age = "qwerty"
print("\t", person)
# -------------------------------------------

"""
6. Реалізуйте властивість класу, яка має наступний функціонал:
    - при встановленні значення цієї властивості у файл із заздалегідь певною назвою повинен зберігатися час
        (коли встановлювали значення властивості) та встановлене значення.
"""
import datetime
import locale

locale.setlocale(locale.LC_TIME, "uk-UA")


class Person:
    def __init__(self, surname, name, patronymic, birthdate, nickname_in_the_past):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birthdate = birthdate
        self.nickname_in_the_past = nickname_in_the_past

    def __str__(self):
        return f"Громадянин: {self.surname} {self.name} {self.patronymic}. " \
               f"Дата народження: {self.birthdate}. " \
               f"Прізвисько в минулому = {self.nickname_in_the_past}"

    def get_nickname(self):
        return self.nickname_in_the_past

    def set_nickname(self, nickname_value):
        set_time = datetime.datetime.now().strftime("%A, %d.%m.%Y о %H:%M:%S:")

        string_to_save = f"{set_time}\n\t" \
                         f"- Прізвисько в минулому: {self.nickname_in_the_past}\n\t" \
                         f"- Позивний тепер: {nickname_value}"

        with open("nickname.txt", encoding='utf-8', mode='w') as f:
            f.write(string_to_save)

        self.nickname_in_the_past = nickname_value

    nickname_now = property(get_nickname, set_nickname)


person = Person("Петров", "Петро", "Петрович", "24.08.1975", "Петька")
person.nickname_now = "Доцент"

print("-" * 77, "\n")
print("Завдання №6:")

print("\t", "Позивний збережено у файл!")
# -------------------------------------------

"""
7. Реалізуйте метаклас, який має наступний функціонал:
    - при його використанні у файл із заздалегідь визначеною назвою потрібно зберегти ім'я класу та список його полів.
"""


class SaveToFileMetaData(type):
    def __new__(typeclass, classname, super_classes, classdict):
        res = f"{classname}:\n\t"
        for i in classdict:
            res += f"{i} = {classdict[i]}\n\t"

        with open("ClassData.txt", encoding="utf-8", mode="w") as f:
            f.write(res)

        return type.__new__(typeclass, classname, super_classes, classdict)


class Person(metaclass=SaveToFileMetaData):

    def __init__(self, surname, name, patronymic, birthdate):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birthdate = birthdate

    def __str__(self):
        return f"Громадянин: {self.surname} {self.name} {self.patronymic}. Дата народження: {self.birthdate}"


person = Person("Петров", "Петро", "Петрович", "24.08.1975")

print("-" * 77, "\n")
print("Завдання №7:")

print("\t", person)
# -------------------------------------------

"""
8. Створіть ABC клас з абстрактним методом перевірки цілого числа на простоту. Тобто якщо параметром цього методу є
    ціле число і воно просте, то метод повинен повернути True, а в іншому випадку False.
        - Створіть його клас наслідуючий.
        - Створіть клас, який не успадковує ABC клас, але володіє потрібним методом.
            Зареєструйте його як віртуальний підклас.
        - Перевірте працездатність проекту.
"""
import abc


class NumberValidator(abc.ABC):

    @abc.abstractmethod
    def check_number(self, number):
        for i in range(2, number // 2):
            return number % i != 0


class SimpleNumber(NumberValidator):
    def __init__(self, number):
        self.number = number

    def check_number(self, number):
        return super().check_number(number)


class AnotherClass:

    def check_number(self, number):
        for i in range(2, number // 2):
            return number % i != 0


NumberValidator.register(AnotherClass)

print("-" * 77, "\n")
print("Завдання №8:")

number1 = SimpleNumber(3)
print("\t", number1.check_number(78))

number2 = AnotherClass()
print("\t", isinstance(number2, NumberValidator))
