"""
1. Створіть клас для опису товару.
    У якості атрибутів товару можете використовувати значення ціни товару, опису товару, габарити товару.
    Створіть пару екземплярів вашого класу та протестуйте їхню роботу.
"""


class Product:
    def __init__(self, product_name: str, product_desc: str, product_dimensions_length: int,
                 product_dimensions_width: int, product_price: float, product_quantity: float):
        self.product_name = product_name
        self.product_desc = product_desc
        self.product_dimensions_length = product_dimensions_length
        self.product_dimensions_width = product_dimensions_width
        self.product_price = product_price
        self.product_quantity = product_quantity

    def __str__(self):
        return f"{self.product_name}\n" \
               f"Опис: {self.product_desc}\n" \
               f"Довжина = {self.product_dimensions_length} мм\n" \
               f"Ширина = {self.product_dimensions_width} мм\n" \
               f"Ціна: {self.product_price} грн.\n" \
               f"В наявності є {self.product_quantity} шт."


# -------------------------------------------

"""
2. Створіть клас "Покупець".
    У якості атрибутів можна використовувати прізвище, ім'я, по батькові, мобільний телефон тощо.
"""


class Buyer:
    def __init__(self, buyer_surname: str, buyer_name: str, buyer_patronymic: str, buyer_phone: str):
        self.buyer_surname = buyer_surname
        self.buyer_name = buyer_name
        self.buyer_patronymic = buyer_patronymic
        self.buyer_phone = buyer_phone

    def __str__(self):
        return f"{self.buyer_surname} {self.buyer_name} {self.buyer_patronymic} {self.buyer_phone}"


# -------------------------------------------

"""
3. Створіть клас "Замовлення".
    Замовлення може містити декілька товарів певної кількості.
    Замовлення має містити дані про користувача, який його здійснив.
    Реалізуйте метод обчислення сумарної вартості замовлення.
    Визначте метод str() для коректного виведення інформації про це замовлення.
"""


class Order:

    def __init__(self, buyer: Buyer):
        self.buyer = buyer
        self.__product_selected_by_buyer = []
        self.__quantity_of_goods = []

    def add_goods(self, goods: Product, quantity: float):
        self.__product_selected_by_buyer.append(goods)
        self.__quantity_of_goods.append(quantity)

    def check_generation(self):
        return "\n".join(f"{index + 1}) {goods.product_name} - "
                         f"{goods.product_price} грн. "
                         f"Додано до кошика: {self.__quantity_of_goods[index]} шт. "
                         f"на загальну суму: {goods.product_price * self.__quantity_of_goods[index]} грн."
                         for index, goods in enumerate(self.__product_selected_by_buyer))

    def total_summa_to_paid(self):
        return sum(goods.product_price * self.__quantity_of_goods[index] for index, goods in
                   enumerate(self.__product_selected_by_buyer))

    def __str__(self):
        return f"Візьміть Ваш чек:\n" \
               f"Замовник: {self.buyer.buyer_name} " \
               f"{self.buyer.buyer_patronymic} " \
               f"{self.buyer.buyer_surname}\n" \
               f"Телефон замовника: {self.buyer.buyer_phone}\n" \
               f"{'-' * 42}\n" \
               f"Замовлені товари:\n{self.check_generation()}\n" \
               f"{'-' * 42}\n" \
               f"ЗАГАЛЬНА СУМА ДО СПЛАТИ: {self.total_summa_to_paid()} грн."


def buyer_registration():
    # buyer = Buyer("Петров", "Петро", "Петрович", "4545454545454")
    buyer = Buyer(
        input("Введіть своє прізвище: "),
        input("Введіть своє ім'я: "),
        input("Як Вас по батькові: "),
        input("Ваш номер телефону: ")
    )

    print("-" * 42, f"\nПриємно познайомитись {buyer.buyer_name}! У нас є такі товари:")

    return buyer


def goods_available():
    goods_list = []
    how_much_goods_available_in_stock = 4

    product_1 = Product("Комп'ютер", "Цей комп'ютер дуже хороший!", 500, 700, 4_320, 12)
    product_2 = Product("Стіл", "Цей стіл дуже зручний і красивий!", 1_200, 600, 1_230, 4)
    product_3 = Product("Годинник", "Годинник як годинник", 30, 30, 230, 60)
    product_4 = Product("Клавіатура", "Ця клавіатура є клавіатурою з великою кількістю клавіш", 700, 450, 584, 43)

    for i in range(1, how_much_goods_available_in_stock + 1):
        goods_list.append(locals().get(f"product_{i}"))

    return goods_list


def show_goods(in_stock):
    for i in range(len(in_stock)):
        print(f"{i + 1})", in_stock[i])

        if i < len(in_stock) - 1:
            print("-" * 14)


def buyer_choice(goods: Product, buyer):
    order = Order(buyer)
    done = False

    print("-" * 42)

    while not done:
        buyer_chose = int(input("Оберіть товар який Вас зацікавив натиснувши цифру біля наіменування товару: "))
        buyer_chose_quantity = int(input("Яка кількість Вас цікавить? "))

        print("-" * 42)
        order.add_goods(goods[buyer_chose - 1], buyer_chose_quantity)
        print(f"Ви обрали: {goods[buyer_chose - 1].product_name}. Вам потрібно: {buyer_chose_quantity} шт.")
        print("-" * 42)
        optional_buyer_chose = int(input('Бажаєте ще щось ("Так" - 1, "Ні" - 0)? '))
        print("-" * 42)

        if not optional_buyer_chose:
            done = True
            print("Дякуємо за замовлення!", end=" ")

    return order


print("-" * 42)
buyer = buyer_registration()
goods_available_in_stock = goods_available()
show_goods(goods_available_in_stock)
order = buyer_choice(goods_available_in_stock, buyer)

print(order)
