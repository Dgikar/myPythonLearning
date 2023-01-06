""" Цей модуль відповідає за ітератор для Group """


class GroupIterator:
    """ Цей клас дозволяє ітерувати об'єкт Group """

    def __init__(self, students):
        """ Метод відповідає за ініціалізацію екземпляру класу після його створення """

        self.students = students
        self.index = 0

    def __next__(self):
        """ Метод повертає наступний елемент, якщо він є, або повертає виняток StopIteration, коли елементи закінчилися.
            :return: наступний елемент, якщо він є, або повертає виняток StopIteration, коли елементи закінчилися
        """

        if self.index >= len(self.students):
            raise StopIteration
        self.index += + 1
        return self.students[self.index - 1]

    def __iter__(self):
        """ Отримання ітератора для перебору об'єкта """

        return self
