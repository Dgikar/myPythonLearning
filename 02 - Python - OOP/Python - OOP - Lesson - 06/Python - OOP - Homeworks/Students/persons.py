""" Модуль роботи з обєктом Human """


class Human:
    """ Клас Human """

    def __init__(self,
                 person_surname: str,
                 person_name: str,
                 person_patronymic: str,
                 person_gender: str,
                 person_phone: str
                 ):
        """ Цей метод відповідає за ініціалізацію екземплярів класу після його створення """

        self.person_surname = person_surname
        self.person_name = person_name
        self.person_patronymic = person_patronymic
        self.person_gender = person_gender
        self.person_phone = person_phone

    def __str__(self):
        """ Відображення інформації про об'єкт класу для користувачів (наприклад, для функцій print, str)

            :return: f стрічка
            :rtype: str
        """
        return f"{self.person_surname} " \
               f"{self.person_name} " \
               f"{self.person_patronymic}. " \
               f"Стать: {self.person_gender}. " \
               f"Телефон: {self.person_phone}"


class Student(Human):
    """ Клас Student успадковується від Human """

    def __init__(self, person_surname, person_name, person_patronymic, person_gender, person_phone, person_age):
        """ Цей метод відповідає за ініціалізацію екземплярів класу після його створення """

        super().__init__(person_surname, person_name, person_patronymic, person_gender, person_phone)
        self.person_age = person_age

    def __str__(self):
        """ Відображення інформації про об'єкт класу для користувачів (наприклад, для функцій print, str)

            :return: f стрічка
            :rtype: str
        """

        return f"{super().__str__()}. {self.person_age} років"


def person_registration():
    """ Тут створюється список кандидатів

        :return: Повертає List[Objects] зі списком кандидатів
    """

    student_list = []
    how_many_student_register = 6

    student_1 = Student("Петров", "Петро", "Петрович", "чоловіча", "111-1111111", 25)
    student_2 = Student("Сідоров", "Сідор", "Сідорович", "чоловіча", "222-2222222", 19)
    student_3 = Student("Марініна", "Марія", "Петрівна", "жіноча", "333-3333333", 36)
    student_4 = Student("Іванова", "Іванна", "Іванівна", "жіноча", "444-4444444", 27)
    student_5 = Student("Петров", "Петро", "Петрович", "чоловіча", "555-5555555", 37)
    student_6 = Student("Мусієнко", "Василь", "Андрійович", "чоловіча", "777-7777777", 20)

    for student_number in range(1, how_many_student_register + 1):
        student_list.append(locals().get(f"student_{student_number}"))

    return student_list


def show_person(persons):
    """ Виведення списка кандидатів або списка (пошуку) студентів на екран (в консоль)

        :param persons: List[Objects]
        :type persons: List[Objects]
    """
    for number_in_list, person in enumerate(persons, start=1):
        print(f"    {number_in_list}) {person}")
