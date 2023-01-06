"""
Useful Links:
    HTML Tutorial - https://www.w3schools.com/html
    CSS Tutorial - https://www.w3schools.com/css/default.asp
    Bootstrap 5 Tutorial - https://www.w3schools.com/bootstrap5/index.php
-------------------------------------------

1. Доповніть клас Група (завдання Лекції 2) можливістю підтримки ітераційного протоколу.
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
