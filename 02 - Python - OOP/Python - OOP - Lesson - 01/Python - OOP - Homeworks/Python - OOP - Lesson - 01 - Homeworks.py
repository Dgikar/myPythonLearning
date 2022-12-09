"""
1. Створіть клас для опису товару.
    У якості атрибутів товару можете використовувати значення ціни товару, опису товару, габарити товару.
    Створіть пару екземплярів вашого класу та протестуйте їхню роботу.
"""

# -------------------------------------------

"""
2. Створіть клас "Покупець".
    У якості атрибутів можна використовувати прізвище, ім'я, по батькові, мобільний телефон тощо.
"""

# -------------------------------------------

"""
3. Створіть клас "Замовлення".
    Замовлення може містити декілька товарів певної кількості.
    Замовлення має містити дані про користувача, який його здійснив.
    Реалізуйте метод обчислення сумарної вартості замовлення.
    Визначте метод str() для коректного виведення інформації про це замовлення.
"""
"""
Приклад:
-----------

class Product:

    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title}: {self.price}'


class Customer:

    def __init__(self, surname: str, name: str, phone: str):
        self.surname = surname
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'{self.surname} {self.name}; {self.phone}'


class Cart:

    def __init__(self, customer: Customer):
        self.customer = customer
        self.__products = []
        self.__quantities = []

    def add_product(self, product: Product, quantity: float=1):
        if product in self.__products:
            index = self.__products.index(product)
            self.__quantities[index] += quantity
        else:
            self.__products.append(product)
            self.__quantities.append(quantity)

    def total(self):
        return sum(item.price * self.__quantities[index] for index, item in enumerate(self.__products))

    def __str__(self):
        res = '\n'.join(map(
            lambda item: f'{item[0]} x {item[1]} = {item[0].price * item[1]} UAH',
            zip(self.__products, self.__quantities))
        )

        return f'{customer}\n{res}\nTotal: {self.total()} UAH'


apple = Product('apple', 20)
banana = Product('banana', 30)
orange = Product('orange', 40)

customer = Customer('Ivanov', 'Ivan', '+380990000001')

order = Cart(customer)
order.add_product(apple, 3)
order.add_product(banana)
order.add_product(orange, 0.5)

print(order)


# print(order.__quantities)

print(order.__dict__)
print(order._Cart__products)
print(order._Cart__quantities)
"""
