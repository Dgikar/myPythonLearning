"""
1. Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
"""


class Human:
    def __init__(self,
                 person_surname: str,
                 person_name: str,
                 person_patronymic: str,
                 person_gender: str,
                 person_phone: str
                 ):
        self.person_surname = person_surname
        self.person_name = person_name
        self.person_patronymic = person_patronymic
        self.person_gender = person_gender
        self.person_phone = person_phone

    def __str__(self):
        return f"{self.person_surname} " \
               f"{self.person_name} " \
               f"{self.person_patronymic}. " \
               f"Стать: {self.person_gender}. " \
               f"Телефон: {self.person_phone}"


# -------------------------------------------

"""
2. На його основі створіть клас Студент (перевизначте метод виведення інформації).
"""


class Student(Human):

    def __init__(self, person_surname, person_name, person_patronymic, person_gender, person_phone, person_age):
        super().__init__(person_surname, person_name, person_patronymic, person_gender, person_phone)
        self.person_age = person_age

    def __str__(self):
        return f"{super().__str__()}. {self.person_age} років"


# -------------------------------------------

"""
3. Створіть клас Група, який містить масив із 10 об'єктів класу Студент.
    Реалізуйте методи додавання, видалення студента та метод пошуку студента за прізвищем.
    Визначте для Групи метод str() для повернення списку студентів у вигляді рядка.
"""


class Groupe:
    def __init__(self, groupe_name: str):
        self.groupe_name = groupe_name
        self.__students_list = []

    def add_students(self, candidates, groupe_name):
        self.__students_list.append(f"{candidates.person_surname} "
                                    f"{candidates.person_name} "
                                    f"{candidates.person_patronymic} - "
                                    f"{candidates.person_age} років. "
                                    f"Телефон: {candidates.person_phone}. "
                                    f"Група \"{groupe_name}\"")

    def search_students(self, person_surname):
        return [student for student in self.__students_list if person_surname in student]

    def remove_students(self, candidates):
        self.__students_list.pop(candidates)

    def __str__(self):
        return "\n".join(f"{students}" for students in self.__students_list) or self.groupe_name


def open_groups():
    groups_list = []
    how_many_groups_create = 5

    group_1 = Groupe("Python")
    group_2 = Groupe("Java")
    group_3 = Groupe("FrontEnd")
    group_4 = Groupe("English")
    group_5 = Groupe("DevOps")

    for groups_number in range(1, how_many_groups_create + 1):
        groups_list.append(locals().get(f"group_{groups_number}"))

    return groups_list


def show_groups(grops):
    print("Наявні групи:")
    for number_in_list, groupe_name in enumerate(grops):
        print(f"    {number_in_list + 1}) {groupe_name}")
    print("-" * 42)


def person_registration():
    student_list = []
    how_many_student_register = 6

    student_1 = Student("Петров", "Петро", "Петрович", "чоловіча", "111-1111111", 25)
    student_2 = Student("Сідоров", "Сідор", "Сідорович", "чоловіча", "222-2222222", 19)
    student_3 = Student("Марініна", "Марія", "Петрівна", "жіноча", "333-3333333", 36)
    student_4 = Student("Іванова", "Іванна", "Іванівна", "жіноча", "444-4444444", 27)
    student_5 = Student("Петров", "Петро", "Петрович", "чоловіча", "555-5555555", 37)
    student_6 = Student("Мусієнко", "Василь", "Андрійович", "чоловіча", "555-5555555", 20)

    for student_number in range(1, how_many_student_register + 1):
        student_list.append(locals().get(f"student_{student_number}"))

    return student_list


def show_person(candidates, action_choice):
    if action_choice == 1:
        students_list = str(candidates).split("\n")

        for index, students in enumerate(students_list):
            print(f"    {index + 1}) {students}")

    else:
        for position_in_list, candidate in enumerate(candidates):
            print(f"    {position_in_list + 1}) {candidate}")


def add_candidate_to_grope(candidates, course_groups):
    groups = Groupe(course_groups)
    done = False

    while not done:
        print("Список кандидатів:")
        show_person(candidates, 0)
        print("-" * 42)
        chose_candidates = int(input("Оберіть кандидата за його номером: "))

        print("-" * 42)
        print(f"Ви обрали: {candidates[chose_candidates - 1].person_name} "
              f"{candidates[chose_candidates - 1].person_surname}. "
              f"{candidates[chose_candidates - 1].person_age} років. "
              f"Телефон: {candidates[chose_candidates - 1].person_phone}")
        print("-" * 42)

        show_groups(course_groups)

        chose_course_groups = int(input("Додайте кандидата до групи за її номером: "))

        print("-" * 42)
        print(f"Тепер, {candidates[chose_candidates - 1].person_name} "
              f"{candidates[chose_candidates - 1].person_surname}. "
              f"Телефон: {candidates[chose_candidates - 1].person_phone}, "
              f"зарахований(а) до групи \"{course_groups[chose_course_groups - 1].groupe_name}\"")
        print("-" * 42)

        groups.add_students(candidates[chose_candidates - 1], course_groups[chose_course_groups - 1])

        additional_choice = int(input('Бажаєте ще когось дадати до групи ("Так" - 1, "Ні" - 0)? '))
        print("-" * 42)

        if not additional_choice:
            done = True

    return groups


def actions_with_students(on_course):
    done = False

    while not done:
        print("Що бажаєте зробити? ")
        choose_an_action = int(
            input("     1) Подивитись список студентів\n"
                  "     2) Видалити студента. Натисніть\n"
                  "     3) Знайти студента за прізвищем\n"
                  "     4) Вихід\n"
                  "Введіть номер обраного дії: "))

        print("-" * 42)

        if choose_an_action == 1:
            print("Список студентів:")
            show_person(on_course, 1)
            print("-" * 42)

        elif choose_an_action == 2:
            print("Кого потрібно видалити?:")
            show_person(on_course, 1)
            print("-" * 42)

            chose_student_to_del = int(input("Оберіть студента за його номером: "))

            on_course.remove_students(chose_student_to_del - 1)
            print("-" * 42)

            print("Студенти які продовжують навчання:")
            show_person(on_course, 1)
            print("-" * 42)

        elif choose_an_action == 3:
            finde_student = "Петров"
            # finde_student = "Сідоров"
            # finde_student = "Марініна"
            # finde_student = "Петрова" # немає в жодному із списків

            print("Кого потрібно знайти?", finde_student)
            print("-" * 42)

            students_finde_list = on_course.search_students(finde_student)

            if not students_finde_list:
                print("Такого студента немає на жодному курсі...")
                print("-" * 42)
            else:
                print("Знайдено!")
                for index, students in enumerate(students_finde_list):
                    print(f"    {index + 1}) {''.join(students)}")
                print("-" * 42)

        else:
            done = True


print("-" * 42)
candidates = person_registration()
course_groups = open_groups()
students_on_course = add_candidate_to_grope(candidates, course_groups)
actions_with_students(students_on_course)
