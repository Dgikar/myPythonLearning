class OverMaxStudentError(Exception):
    """ Exception виникає тоді, коли до групи намагаються додати більше студентів ніж зарезервовано місць """

    def __init__(self, groupe_name, max_student):
        self.groupe_name = groupe_name
        self.max_student = max_student

    def __str__(self):
        return f'Не має можливості додати до групи. В групі "{self.groupe_name}" всього {self.max_student} місць'


class CannotBeLessThanOrEqualZeroError(Exception):
    """ Exception виникає тоді, коли користувач ввів номер кандидата або групи який менше або дорівнює нулю """

    def __init__(self, chose_candidates_or_groupe: int, what_is_chosen: str):
        self.chose_candidates_or_groupe = chose_candidates_or_groupe
        self.what_is_chosen = what_is_chosen
        self.candidate = "кандидата"
        self.groupe = "групу"

    def __str__(self):
        return f'Обрано {self.candidate if self.what_is_chosen != "Groupe" else self.groupe} ' \
               f'під номером: {self.chose_candidates_or_groupe}. Номер не може бути менше або дорівнювати нулю!'


class SelectedNotInListError(Exception):
    """ Exception виникає тоді, коли користувач ввів номер кандидата або групи якого немає в списку """

    def __init__(self, chose_candidates_or_groupe: int, length_candidates_or_groupe_list: int, what_is_chosen: str):
        self.chose_candidates_or_groupe = chose_candidates_or_groupe
        self.length_candidates_or_groupe_list = length_candidates_or_groupe_list
        self.what_is_chosen = what_is_chosen
        self.candidate1 = "кандидата"
        self.candidate2 = "кандидатів"
        self.groupe1 = "групу"
        self.groupe2 = "груп"

    def __str__(self):
        return f'Обрано {self.candidate1 if self.what_is_chosen != "Groupe" else self.groupe1} ' \
               f'під номером: {self.chose_candidates_or_groupe}. Такого номеру не має в списку! ' \
               f'Всього {self.candidate2 if self.what_is_chosen != "Groupe" else self.groupe2}: ' \
               f'{self.length_candidates_or_groupe_list}'


class GroupFullError(Exception):
    """ Exception виникає тоді, коли користувач додає студента в групу яка вже набрана """

    def __init__(self, course_groups_full):
        self.course_groups_full = course_groups_full

    def __str__(self):
        return f'Група: "{self.course_groups_full}" вже заповнена'


class WrongChoiceAdditionalActionError(Exception):
    """ Exception виникає тоді, коли користувач ввів не вірний номер додаткової дії """

    def __init__(self, additional_chose):
        self.additional_chose = additional_chose

    def __str__(self):
        return f'Введено: "{self.additional_chose}". Потрібно або "1" або "0"'
