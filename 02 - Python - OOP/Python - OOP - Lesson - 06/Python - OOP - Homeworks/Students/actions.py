""" Модуль додаткових дій зі студентами"""

import persons


def actions_with_students(on_course):
    """ Додаткові дії зі студентами

        :param on_course: List[Objects]
    """

    while True:
        print("Що бажаєте зробити? ")
        choose_an_action = int(
            input("     1) Подивитись список студентів\n"
                  "     2) Видалити студента\n"
                  "     3) Знайти студента за прізвищем\n"
                  "     4) Вихід\n"
                  "Введіть номер обраного дії: "))

        print("-" * 42)

        if choose_an_action == 1:
            label("Список студентів:", on_course)
        elif choose_an_action == 2:
            label("Кого потрібно видалити?:", on_course)
            chose_student_to_del = int(input("Оберіть студента за його номером: "))

            on_course.remove_students(chose_student_to_del - 1)
            print("-" * 42)

            label("Студенти які продовжують навчання:", on_course)

        elif choose_an_action == 3:
            find_student = "Петров"
            # find_student = "Сідоров"
            # find_student = "Марініна"
            # find_student = "Петрова" # немає в жодному із списків

            print("Кого потрібно знайти?", find_student)
            print("-" * 42)

            if students_find_list := on_course.search_students(find_student):
                print("Знайдено!")
                persons.show_person(students_find_list)
            else:
                print("Такого студента немає на жодному курсі...")
            print("-" * 42)
        else:
            break


def label(text, on_course):
    """ Відображення пояснювального тексту в залежності від умови

        :param text: Пояснювальний текст
        :type text: str
        :param on_course: Список студентів
        :type on_course: List[Objects]
    """

    print(text)
    persons.show_person(on_course)
    print("-" * 42)
