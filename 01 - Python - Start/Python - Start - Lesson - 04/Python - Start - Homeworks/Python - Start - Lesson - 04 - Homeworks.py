"""
Useful Links:
    https://docs.python.org/3/tutorial/datastructures.html
-------------------------------------------

1. Дано число (чотиризначне). Перевірити, чи воно є «щасливим квитком».
    Примітка: щасливим квитком називається число, у якому, при парній кількості цифр, сума цифр його лівої половини
    дорівнює сумі цифр його правої половини.
    Наприклад, 1322 є щасливим квитком, тому що 1 + 3 = 2 + 2.
"""
import random

happy_ticket = [random.randint(1, 4) for _ in range(4)]
print(happy_ticket, ["- це не щасливий квиток", "- це щасливий квиток"][sum(happy_ticket[:2]) == sum(happy_ticket[2:])])

# or

ticket = input("Введіть номер квитка: ")
if len(ticket) % 2:
    print("Ви ввели помилковий номер")
else:
    ticket = list(map(int, ticket))
    mid = len(ticket) // 2
    res = happy_ticket, "- це щасливий квиток" if sum(ticket[:mid]) == sum(ticket[mid:]) else "- це не щасливий квиток"
    print(res)
# -------------------------------------------

"""
2. З клавіатури вводиться число (шестизначне). Перевірити, чи воно є паліндромом.
    Примітка: Паліндром називається число, слово або текст, які однаково читаються зліва направо і справа наліво.
    Наприклад, це числа 143341, 5555, 7117 і т.д.
"""
palindrome = input("Введіть шестизначне число: ")
print(palindrome, ["- це не паліндром", "- це паліндром"][palindrome == palindrome[::-1]])
# -------------------------------------------

"""
3. Дано коло з центром на початку координат та радіусом 4.
    Користувач вводить з клавіатури координати точки x та y.
    Написати програму, яка визначить, лежить ця точка всередині кола чи ні.
"""
import math

x_point = int(input("Введіть координати точки \"Х\": "))
y_point = int(input("Введіть координати точки \"Y\": "))
radius = int(input("Введіть радіус кола: "))

hypotenuse = math.sqrt(x_point ** 2 + y_point ** 2)

print(["Крапка не в колі", "Крапка у колі"][hypotenuse <= radius])

"""
На вихідних будемо говорити про стрічки та цикли. Посилання для ознайомлення:
    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
    https://docs.python.org/3/reference/compound_stmts.html#for
    https://docs.python.org/3/reference/compound_stmts.html#while
"""
