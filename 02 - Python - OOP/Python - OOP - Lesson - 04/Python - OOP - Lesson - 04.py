"""
Рішення викладача домашнього завдання з лекції №3
"""


class GroupLimitError(Exception):
    def __init__(self, max_limit):
        self.max_limit = max_limit

    def __str__(self):
        return f'In group we already have  {self.max_limit} students.'


class DublicateStudentError(Exception):
    def __init__(self, student, group_title):
        self.student = student
        self.group_title = group_title

    def __str__(self):
        return f'The {self.student} registered in group {self.group_title}.'


class Human:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.surname} {self.name[0]}.'


class Student(Human):

    def __init__(self, name: str, surname: str, age: int):
        if not isinstance(age, int):
            raise TypeError()

        super().__init__(name, surname)
        self.age = age

    def __str__(self):
        return f'{super().__str__()}, {self.age}'


class Group:

    def __init__(self, title: str, max_students: int = 10):
        if not isinstance(max_students, int):
            raise TypeError()
        if max_students <= 0:
            raise ValueError()

        self.title = title
        self.__students = []
        self.max_student = max_students

    def add_student(self, student: Student):
        """

        :param student:
        :return:
        """
        if student in self.__students:
            raise DublicateStudentError(student, self.title)
        if len(self.__students) >= self.max_student:
            raise GroupLimitError(self.max_student)

        self.__students.append(student)

    def remove_student(self, student: Student):
        """

        :param student:
        :return:
        """
        if student in self.__students:
            self.__students.remove(student)

    def search_surname(self, surname: str):
        """

        :param surname:
        :return:
        """
        res = []
        for student in self.__students:
            if student.surname == surname:
                res.append(student)
        return res

    def __str__(self):
        return f'{self.title}\n\n' + '\n'.join(map(str, self.__students))


try:
    x = Group('Python', max_students=3)

    x.add_student(Student('Ivan', 'Ivanov4', 20))
    x.add_student(Student('Petro', 'Ivanov', 20))
    x.add_student(Student('Ivan1', 'Ivanov4', 20))

    res = x.search_surname('Ivanov5')

    if res:
        print(list(map(str, res)))

except Exception as error:
    print(error)
