class PriceItemCannotBeLessThanOrEqualZero(Exception):
    """ Exception виникає тоді, коли користувач ввів ціну товару меншу або яка дорівнює нулю """

    def __init__(self, product_price):
        self.product_price = product_price

    def __str__(self):
        return f"Ціна не може бути менше або дорівнювати нулю! Вказана ціна: {self.product_price} грн."


class ProductPriceIsNotIntOrFloat(Exception):
    """ Exception виникає тоді, коли користувач ввів ціну товару не цифрами, а рядком або замість нуля,
        використав букву "О" """

    def __init__(self, product_price):
        self.product_price = product_price

    def __str__(self):
        return f'Ціна "{self.product_price}" грн. має бути вказана цифрами (можливо з копійками).' \
               f'Введено рядок чи букву "O"'


class IncorrectProductQuantityEntered(Exception):
    """ Exception виникає тоді, коли користувач ввів кількість товару не цифрами, а рядком або замість нуля,
        використав букву "О" """

    def __init__(self, product_quantity):
        self.product_quantity = product_quantity

    def __str__(self):
        return f'Кількість товару "{self.product_quantity}" має бути вказана цілим або дійсним числом. ' \
               f'Введено рядок чи букву "O"'


class SelectedItemWhichIsNotAvailable(Exception):
    """ Exception виникає тоді, коли користувач вибрав товар, якого немає у списку """

    def __init__(self, buyer_chose: int, number_of_items_in_product_list: int):
        self.buyer_chose = buyer_chose
        self.number_of_items_in_product_list = number_of_items_in_product_list

    def __str__(self):
        return f'Обрано товар за номером: "{self.buyer_chose}". Такого товару, немає у списку. ' \
               f'Всього у списку {self.number_of_items_in_product_list} товара'


class QuantityOfProductIsNotAvailableInStock(Exception):
    """ Exception виникає тоді, коли користувач вибрав кількість товару, якої немає у наявності """

    def __init__(self, buyer_chose: int, number_of_items_in_product_list: int):
        self.buyer_chose = buyer_chose
        self.number_of_items_in_product_list = number_of_items_in_product_list

    def __str__(self):
        return f'Введено кількість: {self.buyer_chose} шт. ' \
               f'Всього в наявності: {self.number_of_items_in_product_list} шт.'


class WrongChoiceAdditionalAction(Exception):
    """ Exception виникає тоді, коли користувач ввів не вірний номер додаткової дії """

    def __init__(self, additional_buyer_chose: int):
        self.additional_buyer_chose = additional_buyer_chose

    def __str__(self):
        return f'Введено: "{self.additional_buyer_chose}". Потрібно або "1" або "0"'
