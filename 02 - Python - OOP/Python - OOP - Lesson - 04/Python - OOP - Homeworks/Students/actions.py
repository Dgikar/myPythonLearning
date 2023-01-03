import persons


def actions_with_students(on_course):
    """

    :param on_course:
    :type on_course:
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
            print("Список студентів:")
            persons.show_person(on_course, 1)
            print("-" * 42)

        elif choose_an_action == 2:
            print("Кого потрібно видалити?:")
            persons.show_person(on_course, 1)
            print("-" * 42)

            chose_student_to_del = int(input("Оберіть студента за його номером: "))

            on_course.remove_students(chose_student_to_del - 1)
            print("-" * 42)

            print("Студенти які продовжують навчання:")
            persons.show_person(on_course, 1)
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
            break
