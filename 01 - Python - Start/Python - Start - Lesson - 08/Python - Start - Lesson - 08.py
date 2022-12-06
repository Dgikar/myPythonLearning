"""
Как разбить число на разряды
    Есть число 1234567.
    Как разбить пробелами число по разрядам, чтобы получилось 1 234 567?

https://ru.stackoverflow.com/questions/545836/%D0%9A%D0%B0%D0%BA-%D1%80%D0%B0%D0%B7%D0%B1%D0%B8%D1%82%D1%8C-%D1%87%D0%B8%D1%81%D0%BB%D0%BE-%D0%BD%D0%B0-%D1%80%D0%B0%D0%B7%D1%80%D1%8F%D0%B4%D1%8B
"""
x = 1234567890
fstring = f"{x:_} руб.".replace("_", " ")
print(f"Итого: {fstring} \n Напишите сумму прописью: ________________")

"""
Эта программа подсчитывает кол-во разрядов в сумма:
"""
n = int(input("n = "))
count = 1
n = abs(n)
n //= 10
while n > 0:
    n //= 10
    count += 1

print("Количество разрядов - ", count)
# -------------------------------------------------

num = 12478.75
print(num % 10)  # 8.75 - берутся последняя цифра перед точкой и цифры копеек
print(num // 10 % 10)  # 7.0 - берется третья цифра (предпоследняя перед точкой)
print(num % 100)  # 78.75 - берутся 2-е предпоследние цифры до точки
print(num // 100)  # 124.0 - берется первые 2-е цифры до точки

one = num % 10
ten = num // 10 % 10
pos_teen = num % 100
hundred = num // 100
# -------------------------------------------------

x = 27
fstring = f"{x:_} руб.".replace("_", " ")
print(f"Итого: {fstring}")
# -------------------------------------------------

f1 = (257 % 100) // 10 != 1 and 257 % 10 == 1
x = (257 % 100)
y = x // 10
print(x)
print(y)
z = 257 % 10
print(z)
print(25 % 1000)
# -------------------------------------------------

value = '225252222787.85'
print(value[-2:])
print(value[:-3])
# -------------------------------------------------

roman_digits = (int(input("Введіть ціле число: ")))
print("roman_digits", roman_digits)

print("res_units - roman_digits % 10 - ", roman_digits % 10)  # высчитывает единицы
print("res_dozens - roman_digits // 10 % 10 - ", roman_digits // 10 % 10)  # высчитывает десятки
print("res_hundreds - roman_digits // 100 % 10 - ", roman_digits // 100 % 10)  # высчитывает соткни
print("res_thousands - roman_digits // 1000 - ", roman_digits // 1000)  # высчитывает тысячи
print("res_tens_of_thousands - roman_digits // 10000 - ", roman_digits // 10000)  # высчитывает десятки тысяч
print("res_tens_of_thousands - roman_digits // 10000 % 10 - ", roman_digits // 10000 % 10)  # высчитывает
print("res_tens_of_thousands - roman_digits % 100 - ", roman_digits % 100)  # высчитывает