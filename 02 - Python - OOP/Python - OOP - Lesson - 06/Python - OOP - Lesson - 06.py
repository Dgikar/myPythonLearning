import math


class Rational:

    def __init__(self, a: int, b: int):
        if not isinstance(a, int):
            raise TypeError('A must be int')
        if not isinstance(b, int):
            raise TypeError('B must be int')
        if not b:
            raise ZeroDivisionError()

        self.__a = a
        self.__b = b

    def __eq__(self, other):
        k = math.gcd(self.__a, self.__b)
        self.__a //= k
        self.__b //= k

        k = math.gcd(other.__a, other.__b)
        other.__a //= k
        other.__b //= k
        return (self.__a, self.__b) == (other.__a, other.__b)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.__a / self.__b < other.__a / other.__b

    def __gt__(self, other):
        return self.__a / self.__b > other.__a / other.__b

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        b = self.__b * other.__b
        a = b // self.__b * self.__a - \
            b // other.__b * other.__a
        return Rational(a, b)

    def __rsub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        b = self.__b * other.__b
        a = b // self.__b * self.__a - \
            b // other.__b * other.__a
        return Rational(a, b)

    def __isub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        sign = 1 if self.__a * self.__b > 0 else -1

        b = abs(self.__b) * abs(other.__b)
        a = b // abs(self.__b) * abs(self.__a) - \
            b // abs(other.__b) * abs(other.__a)
        self.__a = sign * a
        self.__b = b
        return self

    def __str__(self):
        sign = '' if self.__a * self.__b > 0 else '-'
        a, b = abs(self.__a), abs(self.__b)
        k = math.gcd(a, b)
        a //= k
        b //= k

        if a == b:
            return f'{sign}1'
        if b == 1:
            return f'{sign}{a}'
        if a > b:
            return f'{sign}{a // b} {a - a // b * b} / {b}'
        return f'{sign}{a} / {b}'


x1 = Rational(1, 2)
x2 = Rational(2, 4)

print(x1 == x2)


# -------------------------------------------
class MySeq:

    def __init__(self, n):
        self.n = n

    def __getitem__(self, item):
        if isinstance(item, int):
            if item > self.n:
                raise IndexError
            return item * 10
        if isinstance(item, slice):
            res = []
            start = item.start or 0
            stop = item.stop or self.n + 1
            step = item.step or 1

            for i in range(start, stop, step):
                res.append(i * 10)
            return res

        raise TypeError()

    def __len__(self):
        return self.n


x = MySeq(10)
print(x[:])


# -------------------------------------------
class Order:

    def __init__(self):
        self.products = []
        self.quantities = []
        self.prices = []

    def add_product(self, product, price, quantity=1):
        self.products.append(product)
        self.prices.append(price)
        self.quantities.append(quantity)

    def __iter__(self):
        return OrderIter(self.products, self.prices, self.quantities)


class OrderIter:

    def __init__(self, products, prices, quantities):
        self.products = products
        self.prices = prices
        self.quantities = quantities
        self.index = 0

    def __next__(self):
        if self.index < len(self.products):
            self.index += 1
            return self.products[self.index - 1], self.prices[self.index - 1], self.quantities[self.index - 1]
        raise StopIteration


order = Order()
order.add_product('banana', 20)
order.add_product('apple', 21, 2)
order.add_product('orange', 22, 3)
order.add_product('bread', 22, 2)

for product, price, quantity in order:
    print(product, price * quantity)
