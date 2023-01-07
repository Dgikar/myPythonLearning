"""
Useful Links:
    HTML Tutorial - https://www.w3schools.com/html
    CSS Tutorial - https://www.w3schools.com/css/default.asp
    Bootstrap 5 Tutorial - https://www.w3schools.com/bootstrap5/index.php
-----------------------------

2. Модифікуєте клас Замовлення (Лекція 1), додавши реалізацію протоколу послідовностей та ітераційного протоколу.
"""
import buyer_module
import product_module

if __name__ == '__main__':
    print("-" * 42)
    buyer = buyer_module.buyer_registration()
    goods_available_in_stock = product_module.products_available()
    product_module.show_products(goods_available_in_stock)
    buyer_order = buyer_module.buyer_choice(goods_available_in_stock, buyer)
