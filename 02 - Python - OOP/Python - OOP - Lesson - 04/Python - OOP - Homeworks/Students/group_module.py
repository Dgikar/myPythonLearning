import logging
import errors
import persons

logging.basicConfig(
    handlers=[logging.FileHandler(
        filename="add_students.log", encoding='utf-8', mode='w')],
    format="%(asctime)s - %(levelname)s: %(message)s",
    datefmt='%d.%m.%Y о %H:%M:%S',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


class Groupe:

    def __init__(self, groupe_name: str, max_students: int = 5):
        """

        :param groupe_name:
        :type groupe_name:
        :param max_students:
        :type max_students:
        """
        self.groupe_name = groupe_name
        self.max_students = max_students
        self.__students_list = []

    def add_students(self, candidates, groupe_name):
        """

        :param candidates:
        :type candidates:
        :param groupe_name:
        :type groupe_name:
        """
        self.__students_list.append(f"{candidates.person_surname} "
                                    f"{candidates.person_name} "
                                    f"{candidates.person_patronymic} - "
                                    f"{candidates.person_age} років. "
                                    f"Телефон: {candidates.person_phone}. "
                                    f"Група \"{groupe_name}\"")

    def search_students(self, person_surname):
        """

        :param person_surname:
        :type person_surname:
        :return:
        :rtype:
        """
        return [student for student in self.__students_list if person_surname in student]

    def remove_students(self, candidates):
        """

        :param candidates:
        :type candidates:
        """
        if candidates + 1 > len(self.__students_list):
            raise errors.SelectedNotInListError(candidates + 1, len(self.__students_list), "Candidate")

        studet_to_del = str(self.__students_list[candidates]).split(" ")

        self.__students_list.pop(candidates)

        logger.info(
            f'З групи {studet_to_del[-1]} видалено: {" ".join(studet_to_del[:3])}. {" ".join(studet_to_del[4:8])} '
        )

    def __str__(self):
        """

        :return:
        :rtype:
        """
        return "\n".join(f"{students}" for students in self.__students_list) or self.groupe_name


def open_groups():
    """

    :return:
    :rtype:
    """
    groups_list = []
    how_many_groups_create = 5

    group_1 = Groupe("Python", 2)
    group_2 = Groupe("Java", 2)
    group_3 = Groupe("FrontEnd", 3)
    group_4 = Groupe("English", 2)
    group_5 = Groupe("DevOps", 2)

    for groups_number in range(1, how_many_groups_create + 1):
        groups_list.append(locals().get(f"group_{groups_number}"))

    return groups_list


def show_groups(grops):
    """

    :param grops:
    :type grops:
    """
    print("Наявні групи:")
    for number_in_list, groupe_name in enumerate(grops):
        if grops[number_in_list].max_students > 0:
            print(f"    {number_in_list + 1}) {groupe_name}. Вільних місць: {grops[number_in_list].max_students}")
        else:
            print(f"    {number_in_list + 1}) {groupe_name}.\033[31m Вільних місць немає \033[0m")

    print("-" * 42)


def add_candidate_to_grope(candidates, course_groups):
    """

    :param candidates:
    :type candidates:
    :param course_groups:
    :type course_groups:
    :return:
    :rtype:
    """
    groups = Groupe(course_groups)

    while True:
        print("Список кандидатів:")
        persons.show_person(candidates, 0)
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
            raise errors.CannotBeLessThanOrEqualZeroError(chose_course_groups, "Groupe")
        elif chose_course_groups > len(course_groups):
            raise errors.SelectedNotInListError(chose_course_groups, len(course_groups), "Groupe")

        for i in range(len(course_groups)):
            if str(course_groups[i]) == str(course_groups[chose_course_groups - 1]):
                course_groups[i].max_students -= 1
            if course_groups[i].max_students < 0:
                raise errors.GroupFullError(str(course_groups[chose_course_groups - 1]))

        print("-" * 42)
        print(f"Тепер, {temp_msg} зараховано до групи \"{course_groups[chose_course_groups - 1].groupe_name}\"")
        print("-" * 42)

        logger.info(f"{temp_msg} зараховано до групи \"{course_groups[chose_course_groups - 1].groupe_name}\"")

        groups.add_students(candidates[chose_candidates - 1], course_groups[chose_course_groups - 1])

        additional_choice = int(input('Бажаєте ще когось дадати до групи ("Так" - 1, "Ні" - 0)? '))
        if additional_choice > 1 or additional_choice < 0:
            raise errors.WrongChoiceAdditionalActionError(additional_choice)
        print("-" * 42)

        if not additional_choice:
            break

    return groups
