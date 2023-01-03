class Human:
    def __init__(self,
                 person_surname: str,
                 person_name: str,
                 person_patronymic: str,
                 person_gender: str,
                 person_phone: str
                 ):
        """

        :param person_surname:
        :type person_surname:
        :param person_name:
        :type person_name:
        :param person_patronymic:
        :type person_patronymic:
        :param person_gender:
        :type person_gender:
        :param person_phone:
        :type person_phone:
        """
        self.person_surname = person_surname
        self.person_name = person_name
        self.person_patronymic = person_patronymic
        self.person_gender = person_gender
        self.person_phone = person_phone

    def __str__(self):
        """

        :return:
        :rtype:
        """
        return f"{self.person_surname} " \
               f"{self.person_name} " \
               f"{self.person_patronymic}. " \
               f"Стать: {self.person_gender}. " \
               f"Телефон: {self.person_phone}"


class Student(Human):

    def __init__(self, person_surname, person_name, person_patronymic, person_gender, person_phone, person_age):
        """

        :param person_surname:
        :type person_surname:
        :param person_name:
        :type person_name:
        :param person_patronymic:
        :type person_patronymic:
        :param person_gender:
        :type person_gender:
        :param person_phone:
        :type person_phone:
        :param person_age:
        :type person_age:
        """
        super().__init__(person_surname, person_name, person_patronymic, person_gender, person_phone)
        self.person_age = person_age

    def __str__(self):
        """

        :return:
        :rtype:
        """
        return f"{super().__str__()}. {self.person_age} років"


def person_registration():
    """

    :return:
    :rtype:
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


def show_person(candidates, action_choice):
    """

    :param candidates:
    :type candidates:
    :param action_choice:
    :type action_choice:
    """
    if action_choice == 1:
        if candidates:
            students_list = str(candidates).split("\n")
        else:
            print("Список студентів порожній")

        for index, students in enumerate(students_list):
            print(f"    {index + 1}) {students}")

    else:
        for position_in_list, candidate in enumerate(candidates):
            print(f"    {position_in_list + 1}) {candidate}")
