"""
Приклад:
-----------
class Student:
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name

    def __str__(self):
        return f'{self.surname} {self.name[0]}.'

class Group:
    def __init__(self, title):
        self.title = title
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def __str__(self):
        return f"{self.title}\n{'-' * 10}\n" + '\n'.join(map(str, self.students)) + '\n'


if __name__ == '__main__':
    student_1 = Student('Ivanov', 'Ivan')
    student_2 = Student('Petrov', 'Petro')
    student_3 = Student('Marieva', 'Marria')

    group_python_it = Group('Python IT Gen')
    group_python_it.add_student(student_1)
    group_python_it.add_student(student_2)
    group_python_it.add_student(student_3)

    group_eng_it = Group('English IT Gen')
    group_eng_it.add_student(student_2)
    group_eng_it.add_student(student_1)

    print(group_python_it)
    print(group_eng_it)
"""
"""
1. Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
"""

# -------------------------------------------

"""
2. На його основі створіть клас Студент (перевизначте метод виведення інформації).
"""

# -------------------------------------------

"""
3. Створіть клас Група, який містить масив із 10 об'єктів класу Студент.
    Реалізуйте методи додавання, видалення студента та метод пошуку студента за прізвищем.
    Визначте для Групи метод str() для повернення списку студентів у вигляді рядка.
"""
