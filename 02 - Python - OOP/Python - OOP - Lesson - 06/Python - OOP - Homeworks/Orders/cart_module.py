""" Модуль Кошика """

import product_module
import buyer_module
import cart_iterator


class Cart:
    """ Клас призначений для роботи з обєктом Cart """

    def __init__(self, buyer: buyer_module.Buyer):
        """ Метод відповідає за ініціалізацію екземплярів класу після його створення

            :type buyer: object
        """
        self.buyer = buyer
        self.__product_selected_by_buyer = []
        self.__quantity_of_goods = []
        self.index = 0

    def __getitem__(self, index):
        """ Набуття значення за ключом index """

        if isinstance(index, int):
            if index >= 0 and index < len(self.__product_selected_by_buyer):
                return self.__product_selected_by_buyer[index]
            else:
                raise IndexError(f'Індексу "{index}" не існує')
        raise TypeError()

    def __len__(self):
        """ Дозволяє визначити поведінку екземпляра типу користувача при запиті його довжини len() """

        return len(self.__product_selected_by_buyer)

    def __iter__(self):
        """ Отримання ітератора для перебору об'єкта """

        return cart_iterator.CartIterator(self.__product_selected_by_buyer)

    def __next__(self):
        """ Перехід до наступного значення та його зчитування """

        if self.index >= len(self.__product_selected_by_buyer):
            raise StopIteration
        self.index += 1
        return self.__product_selected_by_buyer[self.index - 1]

    def add_goods(self, goods: product_module.Product, quantity: float):
        """ Додавання товарів у кошик

            :param goods: Список товарів - List[Objects]
            :type goods: List[Objects]
            :param quantity: Список кількості замовлених товарів - List[float]
            :type quantity: List[float]
        """

        self.__product_selected_by_buyer.append(goods)
        self.__quantity_of_goods.append(quantity)

    def check_generation(self):
        """ Генерація чеку для покупця

            :return: f стрічка
        """
        return "\n".join(f"     {index + 1}) {goods.product_name} - "
                         f"{goods.product_price} грн. "
                         f"Додано до кошика: {self.__quantity_of_goods[index]} шт. "
                         f"на загальну суму: {goods.product_price * self.__quantity_of_goods[index]} грн."
                         for index, goods in enumerate(self.__product_selected_by_buyer))

    def total_summa_to_paid(self):
        """ Підрахунок загальної суми всіх замовлених товарів """

        return sum(goods.product_price * self.__quantity_of_goods[index] for index, goods in
                   enumerate(self.__product_selected_by_buyer))

    def __str__(self):
        """ Відображення інформації про об'єкт класу для користувачів (наприклад, для функцій print, str)

            :return: f стрічка
        """

        return f"Візьміть Ваш чек:\n\n" \
               f"   Замовник: {self.buyer.buyer_name} {self.buyer.buyer_patronymic} {self.buyer.buyer_surname}\n" \
               f"   Телефон замовника: {self.buyer.buyer_phone}\n" \
               f"   {'-' * 42}\n" \
               f"   Замовлені товари:\n" \
               f"{self.check_generation()}\n\n" \
               f"   {'-' * 42}\n" \
               f"   ЗАГАЛЬНА СУМА ДО СПЛАТИ: {self.total_summa_to_paid()} грн."
