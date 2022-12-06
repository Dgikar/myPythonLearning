"""
Useful Links:
    PyCharm Shortcuts: https://www.shortcutfoo.com/app/dojos/pycharm-win/cheatsheet
    Boolean operations: https://docs.python.org/3/reference/expressions.html#booleans
    Control Flow: https://docs.python.org/3/tutorial/controlflow.html
-------------------------------------------

1. Є дев'ятиповерховий будинок, в якому 4 під'їзди. Номер під'їзду починається з одиниці. На одному поверсі -
    4 квартири. Напишіть програму, яка від користувача отримує номер квартири та виводить для заданої квартири номер
    під'їзду, поверху та номер на поверсі. Якщо такої квартири немає в цьому будинку, то необхідно повідомити
    користувача про це.
"""
apartment_to_find = int(input("Введіть номер квартири: "))

flats_on_floor = 4
numbers_front_door = 4
floors_on_house = 9
flats_in_front_door = flats_on_floor * floors_on_house

apartments_in_building = flats_in_front_door * numbers_front_door

front_door = (apartment_to_find + flats_in_front_door - 1) // flats_in_front_door
floor = (apartment_to_find - 1) % flats_in_front_door // flats_on_floor + 1
apartment_on_floor = apartment_to_find % flats_on_floor or flats_on_floor

message = f"Квартира знаходиться в {front_door} парадному, на {floor} поверсі. Вона {apartment_on_floor} за рахунком"

print(apartment_to_find > apartments_in_building and "Такої квартири не існує у цьому будинку" or message)
# -------------------------------------------

"""
2. Написати програму, яка буде повертати для заданого року кількість днів. Рік є високосним, якщо він кратний 4, але
    не кратний 100, а також якщо він кратний 400
"""
entered_year = int(input("Введіть рік: "))
leap_year = entered_year % 4 == 0 and entered_year % 100 != 0 or entered_year % 400 == 0
print(leap_year and "Цей рік – високосний" or "Цей рік не високосний")
# -------------------------------------------

"""
3. Трикутник існує лише тоді, коли сума будь-яких двох сторін більше третьої.
    Дано: A, B, C - сторони трикутника. Напишіть програму, яка вказує чи існує такий трикутник.
"""
side_a = int(input("Введіть сторону \"А\": "))
side_b = int(input("Введіть сторону \"B\": "))
side_c = int(input("Введіть сторону \"C\": "))

triangle = side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a

print(triangle and "Трикутник існує" or "Трикутник не існує")
