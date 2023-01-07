""" Цей модуль відповідає за ітератор для Кошика """


class CartIterator:
    """ Цей клас дозволяє ітерувати об'єкт Кошика """

    def __init__(self, products):
        """ Метод відповідає за ініціалізацію екземпляру класу після його створення """

        self.products = products
        self.index = 0

    def __next__(self):
        """ Метод повертає наступний елемент, якщо він є, або повертає виняток StopIteration, коли елементи закінчилися.
            :return: наступний елемент, якщо він є, або повертає виняток StopIteration, коли елементи закінчилися
        """

        if self.index >= len(self.products):
            raise StopIteration
        self.index += + 1
        return self.products[self.index - 1]

    def __iter__(self):
        """ Отримання ітератора для перебору об'єкта """

        return self
