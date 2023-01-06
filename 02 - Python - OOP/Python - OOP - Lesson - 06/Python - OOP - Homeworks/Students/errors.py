""" Цей модуль відповідає за Exception """


class OverMaxStudentError(Exception):
    """ Exception виникає тоді, коли до групи намагаються додати більше студентів ніж зарезервовано місць """

    def __init__(self, group_name, max_student):
        """ Метод відповідає за ініціалізацію екземплярів класу після його створення """

        self.group_name = group_name
        self.max_student = max_student

    def __str__(self):
        """ Відображення інформації про об'єкт класу для користувачів (наприклад, для функцій print, str) """

        return f'Не має можливості додати до групи. В групі "{self.group_name}" всього {self.max_student} місць'


class CannotBeLessThanOrEqualZeroError(Exception):
    """ Exception виникає тоді, коли користувач ввів номер кандидата або групи який менше або дорівнює нулю """

    def __init__(self, chose_candidates_or_group: int, what_is_chosen: str):
        """ Метод відповідає за ініціалізацію екземплярів класу після його створення """

        self.chose_candidates_or_group = chose_candidates_or_group
        self.what_is_chosen = what_is_chosen
        self.candidate = "кандидата"
        self.group = "групу"

    def __str__(self):
        """ Відображення інформації про об'єкт класу для користувачів (наприклад, для функцій print, str) """

        return f'Обрано {self.candidate if self.what_is_chosen != "Group" else self.group} ' \
               f'під номером: {self.chose_candidates_or_group}. Номер не може бути менше або дорівнювати нулю!'


class SelectedNotInListError(Exception):
    """ Exception виникає тоді, коли користувач ввів номер кандидата або групи якого немає в списку """

    def __init__(self, chose_candidates_or_group: int, length_candidates_or_group_list: int, what_is_chosen: str):
        """ Метод відповідає за ініціалізацію екземплярів класу після його створення """

        self.chose_candidates_or_group = chose_candidates_or_group
        self.length_candidates_or_group_list = length_candidates_or_group_list
        self.what_is_chosen = what_is_chosen
        self.candidate1 = "кандидата"
        self.candidate2 = "кандидатів"
        self.group1 = "групу"
        self.group2 = "груп"

    def __str__(self):
        """ Відображення інформації про об'єкт класу для користувачів (наприклад, для функцій print, str) """

        return f'Обрано {self.candidate1 if self.what_is_chosen != "Group" else self.group1} ' \
               f'під номером: {self.chose_candidates_or_group}. Такого номеру не має в списку! ' \
               f'Всього {self.candidate2 if self.what_is_chosen != "Group" else self.group2}: ' \
               f'{self.length_candidates_or_group_list}'


class GroupFullError(Exception):
    """ Exception виникає тоді, коли користувач додає студента в групу яка вже набрана """

    def __init__(self, course_groups_full):
        """ Метод відповідає за ініціалізацію екземплярів класу після його створення """

        self.course_groups_full = course_groups_full

    def __str__(self):
        """ Відображення інформації про об'єкт класу для користувачів (наприклад, для функцій print, str) """

        return f'Група: "{self.course_groups_full}" вже заповнена'


class WrongChoiceAdditionalActionError(Exception):
    """ Exception виникає тоді, коли користувач ввів не вірний номер додаткової дії """

    def __init__(self, additional_chose):
        """ Метод відповідає за ініціалізацію екземплярів класу після його створення """

        self.additional_chose = additional_chose

    def __str__(self):
        """ Відображення інформації про об'єкт класу для користувачів (наприклад, для функцій print, str) """

        return f'Введено: "{self.additional_chose}". Потрібно або "1" або "0"'
