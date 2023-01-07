""" Модуль роботи з обєктом Buyer """

import errors_module
import product_module


class Buyer:
    """ Клас Buyer """

    def __init__(self, buyer_surname: str, buyer_name: str, buyer_patronymic: str, buyer_phone: str):
        """ Цей метод відповідає за ініціалізацію екземплярів класу після його створення """

        self.buyer_surname = buyer_surname
        self.buyer_name = buyer_name
        self.buyer_patronymic = buyer_patronymic
        self.buyer_phone = buyer_phone

    def __str__(self):
        """ Відображення інформації про об'єкт класу для користувачів (наприклад, для функцій print, str)

            :return: f стрічка
            :rtype: str
        """

        return f"{self.buyer_surname} {self.buyer_name} {self.buyer_patronymic} {self.buyer_phone}"


def buyer_registration():
    """ Тут створюється список покупців

        :return: Повертає List[Objects] зі списком покупців
    """

    buyer = Buyer("Петров", "Петро", "Петрович", "4545454545454")
    # buyer = Buyer(
    #     input("Введіть своє прізвище: "),
    #     input("Введіть своє ім'я: "),
    #     input("Як Вас по батькові: "),
    #     input("Ваш номер телефону: ")
    # )

    print("-" * 42, f"\nПриємно познайомитись {buyer.buyer_name}! У нас є такі товари:")

    return buyer


def buyer_choice(product: product_module.Product, buyer):
    """ Додавання товарів у кошик

        :param product: Список товарів (List[Object])
        :type product: List[Object]
        :param buyer: Список покупців (List[Object])
        :type buyer: List[Object]
    """

    import cart_module

    buyer_order = cart_module.Cart(buyer)

    print("-" * 42)

    while True:
        buyer_chose = int(input("Оберіть товар який Вас зацікавив натиснувши цифру біля наіменування товару: "))
        if buyer_chose > len(product):
            raise errors_module.SelectedItemWhichIsNotAvailable(buyer_chose, len(product) - 1)

        buyer_chose_quantity = int(input("Яка кількість Вас цікавить? "))
        if buyer_chose_quantity > product[buyer_chose - 1].product_quantity:
            raise errors_module.QuantityOfProductIsNotAvailableInStock(buyer_chose_quantity,
                                                                       product[buyer_chose - 1].product_quantity)

        print("-" * 42)
        print(f"Ви обрали: {product[buyer_chose - 1].product_name}. Вам потрібно: {buyer_chose_quantity} шт.")

        buyer_order.add_goods(product[buyer_chose - 1], buyer_chose_quantity)
        print("-" * 42)

        additional_buyer_chose = int(input('Бажаєте ще щось додати до кошика ("Так" - 1, "Ні" - 0)? '))
        if additional_buyer_chose > 1 or additional_buyer_chose < 0:
            raise errors_module.WrongChoiceAdditionalAction(additional_buyer_chose)

        print("-" * 42)

        if not additional_buyer_chose:
            print("Дякуємо за замовлення!", end=" ")
            break

    print(buyer_order)
