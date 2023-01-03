"""
    Рознесіть класи, які використовували під час вирішення завдання про замовлення та групу студентів по модулям.
        Переконайтеся у працездатності проєктів.

    1) Замовлення
"""
import buyer_module
import product_module

if __name__ == '__main__':
    print("-" * 42)
    buyer = buyer_module.buyer_registration()
    goods_available_in_stock = product_module.products_available()
    product_module.show_products(goods_available_in_stock)
    buyer_order = buyer_module.buyer_choice(goods_available_in_stock, buyer)
