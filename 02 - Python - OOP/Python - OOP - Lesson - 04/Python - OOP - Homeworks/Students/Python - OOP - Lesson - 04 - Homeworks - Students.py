"""
    Рознесіть класи, які використовували під час вирішення завдання про замовлення та групу студентів по модулям.
        Переконайтеся у працездатності проєктів.

    2) Студенти
"""

import persons
import group_module
import actions

if __name__ == "__main__":
    print("-" * 42)
    candidates = persons.person_registration()
    course_groups = group_module.open_groups()
    students_on_course = group_module.add_candidate_to_grope(candidates, course_groups)
    actions.actions_with_students(students_on_course)
