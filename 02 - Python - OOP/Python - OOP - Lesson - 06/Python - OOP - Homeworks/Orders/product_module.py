""" Модуль роботи з обєктом Product """

import errors_module


class Product:
    """ Клас Product """

    def __init__(self,
                 product_name: str,
                 product_desc: str,
                 product_dimensions_length: int,
                 product_dimensions_width: int,
                 product_price: float,
                 product_quantity: float):
        """ Цей метод відповідає за ініціалізацію екземплярів класу після його створення """

        if not isinstance(product_price, float | int):
            raise errors_module.ProductPriceIsNotIntOrFloat(product_price)
        elif product_price <= 0:
            raise errors_module.PriceItemCannotBeLessThanOrEqualZero(product_price)
        elif not isinstance(product_quantity, float | int):
            raise errors_module.IncorrectProductQuantityEntered(product_quantity)

        self.product_name = product_name
        self.product_desc = product_desc
        self.product_dimensions_length = product_dimensions_length
        self.product_dimensions_width = product_dimensions_width
        self.product_price = product_price
        self.product_quantity = product_quantity

    def __str__(self):
        """ Відображення інформації про об'єкт класу для користувачів (наприклад, для функцій print, str)

            :return: f стрічка
            :rtype: str
        """

        return f"{self.product_name}\n" \
               f"   Опис: {self.product_desc}\n" \
               f"   Довжина = {self.product_dimensions_length} мм\n" \
               f"   Ширина = {self.product_dimensions_width} мм\n" \
               f"   Ціна: {self.product_price} грн.\n" \
               f"   В наявності є {self.product_quantity} шт."


def products_available():
    """ Тут створюється список товарів які є в наявності

        :return: Повертає List[Objects] зі списком товарів
    """
    products_list = []
    how_much_goods_available_in_stock = 4

    product_1 = Product("Комп'ютер", "Цей комп'ютер дуже хороший!", 500, 700, 4_320, 12)
    # product_1 = Product("Комп'ютер", "Цей комп'ютер дуже хороший!", 500, 700, -4_320, 12)
    # product_1 = Product("Комп'ютер", "Цей комп'ютер дуже хороший!", 500, 700, 0, 12)
    # product_1 = Product("Комп'ютер", "Цей комп'ютер дуже хороший!", 500, 700, "4_320", 12)
    # product_1 = Product("Комп'ютер", "Цей комп'ютер дуже хороший!", 500, 700, 4_32o, 12)
    product_2 = Product("Стіл", "Цей стіл дуже зручний і красивий!", 1_200, 600, 1_230, 4)
    # product_2 = Product("Стіл", "Цей стіл дуже зручний і красивий!", 1_200, 600, 1_230, "4")
    product_3 = Product("Годинник", "Годинник як годинник", 30, 30, 230, 60)
    product_4 = Product("Клавіатура", "Ця клавіатура є клавіатурою з великою кількістю клавіш", 700, 450, 584, 43)

    for i in range(1, how_much_goods_available_in_stock + 1):
        products_list.append(locals().get(f"product_{i}"))

    # products_list.append(how_much_goods_available_in_stock)

    return products_list


def show_products(in_stock):
    """ Виведення списка товарів на екран (в консоль)

        :param in_stock: List[Objects]
        :type in_stock:  List[Objects]
    """

    for position_in_list, i in enumerate(in_stock):
        print(f"{position_in_list + 1}) {in_stock[position_in_list]}")
        if position_in_list < len(in_stock) - 2:
            print("-" * 14)
