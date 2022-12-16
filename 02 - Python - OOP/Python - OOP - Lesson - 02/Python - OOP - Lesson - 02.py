"""
Домашне завдання:
    1. Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
    2. На його основі створіть клас Студент (перевизначте метод виведення інформації).
    3. Створіть клас Група, який містить масив із 10 об'єктів класу Студент.
        Реалізуйте методи додавання, видалення студента та метод пошуку студента за прізвищем.
        Визначте для Групи метод str() для повернення списку студентів у вигляді рядка.

Рішення викладача
"""


class Human:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.surname} {self.name[0]}.'


class Student(Human):

    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age

    def __str__(self):
        return f'{super().__str__()}, {self.age}'


class Group:

    def __init__(self, title, max_students=10):
        self.title = title
        self.__students = []
        self.max_student = max_students

    def add_student(self, student):
        if student not in self.__students and len(self.__students) < self.max_student:
            self.__students.append(student)

    def remove_student(self, student):
        if student in self.__students:
            self.__students.remove(student)

    def search_surname(self, surname):
        res = []
        for student in self.__students:
            if student.surname == surname:
                res.append(student)

        return res

    def __str__(self):
        return f'{self.title}\n\n' + '\n'.join(map(str, self.__students))


x = Group('Python', max_students=2)

x.add_student(Student('Ivan', 'Ivanov', 20))
x.add_student(Student('Petro', 'Ivanov', 20))
x.add_student(Student('Ivan', 'Ivanov3', 20))
x.add_student(Student('Ivan', 'Ivanov4', 20))

print(x)

res = x.search_surname('Ivanov')
for item in res:
    print(item.name, item.surname, item.age)
    print(item)
