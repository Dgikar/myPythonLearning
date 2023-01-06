""" Модуль Group """

import logging
import errors
import persons
import group_iterator

logging.basicConfig(
    handlers=[logging.FileHandler(
        filename="students_action.log", encoding='utf-8', mode='w')],
    format="%(asctime)s - %(levelname)s: %(message)s",
    datefmt='%d.%m.%Y о %H:%M:%S',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


class Group:
    """ Клас призначений для роботи з обєктом Group """

    def __init__(self, group_name: str, max_students: int = 5):
        """ Метод відповідає за ініціалізацію екземплярів класу після його створення """

        self.group_name = group_name
        self.max_students = max_students
        self.__students_list = []
        self.index = 0

    def __getitem__(self, index):
        """ Набуття значення за ключом index """

        if isinstance(index, int):
            if index >= 0 and index < len(self.__students_list):
                return self.__students_list[index]
            else:
                raise IndexError(f'Індексу "{index}" не існує')
        raise TypeError()

    def __len__(self):
        """ Дозволяє визначити поведінку екземпляра типу користувача при запиті його довжини len() """

        return len(self.__students_list)

    def __iter__(self):
        """ Отримання ітератора для перебору об'єкта """

        return group_iterator.GroupIterator(self.__students_list)

    def __next__(self):
        """ Перехід до наступного значення та його зчитування """

        if self.index >= len(self.__students_list):
            raise StopIteration
        self.index += 1
        return self.__students_list[self.index - 1]

    def add_students(self, candidates, group_name):
        """ Додавання студента до групи

            :param candidates: List
            :param group_name: List
        """

        self.__students_list.append(f"{candidates.person_surname} "
                                    f"{candidates.person_name} "
                                    f"{candidates.person_patronymic} - "
                                    f"{candidates.person_age} років. "
                                    f"Телефон: {candidates.person_phone}. "
                                    f"Група \"{group_name}\"")

    def search_students(self, person_surname):
        """ Пошук студента за прізвищем

            :return: Список в якому знайдений студент(и)
            :rtype: List
        """
        return [student for student in self.__students_list if person_surname in student]

    def remove_students(self, candidates):
        """ Видалення студента з групи """

        if candidates + 1 > len(self.__students_list):
            raise errors.SelectedNotInListError(candidates + 1, len(self.__students_list), "Candidate")

        student_to_del = str(self.__students_list[candidates]).split(" ")

        self.__students_list.pop(candidates)

        logger.info(
            f'З групи {student_to_del[-1]} видалено: {" ".join(student_to_del[:3])}. {" ".join(student_to_del[4:8])} '
        )

    def __str__(self):
        """ Відображення інформації про об'єкт класу для користувачів (наприклад, для функцій print, str) """

        return "\n".join(f"{students}" for students in self.__students_list) or self.group_name


def open_groups():
    """ Тут створюється список відкритих груп вв школі

        :return: Повертає List зі списком груп та кількістю вільних місць в групі
    """

    groups_list = []
    how_many_groups_create = 5

    group_1 = Group("Python", 2)
    group_2 = Group("Java", 2)
    group_3 = Group("FrontEnd", 3)
    group_4 = Group("English", 2)
    group_5 = Group("DevOps", 2)

    for groups_number in range(1, how_many_groups_create + 1):
        groups_list.append(locals().get(f"group_{groups_number}"))

    return groups_list


def show_groups(groups):
    """ Відображає назву групи та кількість вільних місць в цій групі

        :param groups: List
    """
    print("Наявні групи:")
    for number_in_list, group_name in enumerate(groups):
        if groups[number_in_list].max_students > 0:
            print(f"    {number_in_list + 1}) {group_name}. Вільних місць: {groups[number_in_list].max_students}")
        else:
            print(f"    {number_in_list + 1}) {group_name}.\033[31m Вільних місць немає \033[0m")

    print("-" * 42)


def add_candidate_to_grope(candidates, course_groups):
    """ Додавання кандидата до існуючої групи

        :param candidates: Список кандидатів (List[Object])
        :type candidates: List
        :param course_groups: Список груп (List[Object])
        :type course_groups: List
        :return: Список студенів (List[Object])
        :rtype: List[Object]
    """
    groups = Group(course_groups)

    while True:
        print("Список кандидатів:")
        persons.show_person(candidates)
        print("-" * 42)

        chose_candidates = int(input("Оберіть кандидата за його номером: "))
        if chose_candidates <= 0:
            raise errors.CannotBeLessThanOrEqualZeroError(chose_candidates, "Candidate")
        elif chose_candidates > len(candidates):
            raise errors.SelectedNotInListError(chose_candidates, len(candidates), "Candidate")

        temp_msg = f"{candidates[chose_candidates - 1].person_name} " \
                   f"{candidates[chose_candidates - 1].person_surname}. " \
                   f"{candidates[chose_candidates - 1].person_age} років. " \
                   f"Телефон: {candidates[chose_candidates - 1].person_phone}"

        print("-" * 42)
        print("Ви обрали:", temp_msg)
        print("-" * 42)

        show_groups(course_groups)

        chose_course_groups = int(input("Додайте кандидата до групи за її номером: "))
        if chose_course_groups <= 0:
            raise errors.CannotBeLessThanOrEqualZeroError(chose_course_groups, "Group")
        elif chose_course_groups > len(course_groups):
            raise errors.SelectedNotInListError(chose_course_groups, len(course_groups), "Group")

        for i in range(len(course_groups)):
            if str(course_groups[i]) == str(course_groups[chose_course_groups - 1]):
                course_groups[i].max_students -= 1
            if course_groups[i].max_students < 0:
                raise errors.GroupFullError(str(course_groups[chose_course_groups - 1]))

        print("-" * 42)
        print(f"Тепер, {temp_msg} зараховано до групи \"{course_groups[chose_course_groups - 1].group_name}\"")
        print("-" * 42)

        logger.info(f"{temp_msg} зараховано до групи \"{course_groups[chose_course_groups - 1].group_name}\"")

        groups.add_students(candidates[chose_candidates - 1], course_groups[chose_course_groups - 1])

        additional_choice = int(input('Бажаєте ще когось дадати до групи ("Так" - 1, "Ні" - 0)? '))
        if additional_choice > 1 or additional_choice < 0:
            raise errors.WrongChoiceAdditionalActionError(additional_choice)
        print("-" * 42)

        if not additional_choice:
            break

    return groups
