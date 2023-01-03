import product_module
import buyer_module


class Cart:

    def __init__(self, buyer: buyer_module.Buyer):
        """

        :type buyer: object
        """
        self.buyer = buyer
        self.__product_selected_by_buyer = []
        self.__quantity_of_goods = []

    def add_goods(self, goods: product_module.Product, quantity: float):
        """

        :param goods:
        :type goods:
        :param quantity:
        :type quantity:
        """
        self.__product_selected_by_buyer.append(goods)
        self.__quantity_of_goods.append(quantity)

    def check_generation(self):
        """

        :return:
        :rtype:
        """
        return "\n".join(f"     {index + 1}) {goods.product_name} - "
                         f"{goods.product_price} грн. "
                         f"Додано до кошика: {self.__quantity_of_goods[index]} шт. "
                         f"на загальну суму: {goods.product_price * self.__quantity_of_goods[index]} грн."
                         for index, goods in enumerate(self.__product_selected_by_buyer))

    def total_summa_to_paid(self):
        """

        :return:
        :rtype:
        """
        return sum(goods.product_price * self.__quantity_of_goods[index] for index, goods in
                   enumerate(self.__product_selected_by_buyer))

    def __str__(self):
        """

        :return:
        :rtype:
        """
        return f"Візьміть Ваш чек:\n\n" \
               f"   Замовник: {self.buyer.buyer_name} {self.buyer.buyer_patronymic} {self.buyer.buyer_surname}\n" \
               f"   Телефон замовника: {self.buyer.buyer_phone}\n" \
               f"   {'-' * 42}\n" \
               f"   Замовлені товари:\n" \
               f"{self.check_generation()}\n\n" \
               f"   {'-' * 42}\n" \
               f"   ЗАГАЛЬНА СУМА ДО СПЛАТИ: {self.total_summa_to_paid()} грн."
