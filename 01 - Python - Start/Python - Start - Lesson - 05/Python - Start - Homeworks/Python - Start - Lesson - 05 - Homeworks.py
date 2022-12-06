import random

"""
Useful Links:
    while - https://docs.python.org/3/reference/compound_stmts.html#while
    for - https://docs.python.org/3/reference/compound_stmts.html#for
    range - https://docs.python.org/3/library/stdtypes.html#range
    break, continue - https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
-------------------------------------------

1. Написати Python-скрипт, який виводить на екран усі числа в діапазоні від 1 до 100 кратні 7.
"""
random_numbers = [random.randint(1, 100) for _ in range(100)]
for i, item in enumerate(random_numbers):
    if i % 7 == 0:
        print(i)
# -------------------------------------------

"""
2. Написати Python-скрипт, який обчислює за допомогою циклу факторіал числа n (n вводиться з клавіатури).
"""
import math

entered_number = int(input("Введіть число: "))
print(f"Факторіал числа {entered_number} дорівнює {math.factorial(entered_number)}")
# -------------------------------------------

"""
3. Написати Python-скрипт, який виводить на екран таблицю множення на 5.
    Переважно друкувати 1 x 5 = 5, 2 x 5 = 10, а не просто 5, 10, ...
"""
multiplier = int(input("Введіть число на яке хочете помножити"))
for i in range(1, 11):
    print(f"{i} x {multiplier} = {i * multiplier}")
# -------------------------------------------

"""
4. Написати Python-скрипт, який виводить на екран прямокутник із '*'.
    Висота і ширина прямокутника вводяться з клавіатури. 
        Наприклад, нижче представлений прямокутник з висотою 4 та шириною 5.
            *****
            *   *
            *   *
            *****
"""
width = int(input("Введіть висоту прямокутника: "))
height = int(input("Введіть ширину прямокутника: "))

for i in range(height):
    if i in [0, height - 1]:
        for _ in range(width):
            print('*', end=' ')
    else:
        print('*', end=' ')
        for _ in range(1, width - 1):
            print(' ', end=' ')
        print('*', end=' ')
    print()
# -------------------------------------------

"""
5. Є список [0,5,2,4,7,1,3,19]. Написати Python-скрипт для підрахунку непарних цифр у ньому.
"""
numbers = [0, 5, 2, 4, 7, 1, 3, 19]
count_odd = 0
count_even = 0

for x in numbers:
    if not x % 2:
        count_even += 1
    else:
        count_odd += 1

print("Кількість парних чисел:", count_even)
print("Кількість непарних чисел:", count_odd)
# -------------------------------------------

"""
6. Створіть список випадкових чисел (розміром 4 елементи). Створіть другий список у два рази більше першого, де перші 4
    елементи повинні дорівнювати елементам першого списку, а решта елементів - подвоєним значенням початкових.
        Наприклад,
            Було → [1,4,7,2]
            Стало → [1,4,7,2,2,8,14,4]
"""

random_numbers_in_list = [random.randint(1, 20) for _ in range(4)]
print("Наш список такий:", random_numbers_in_list)
new_list = random_numbers_in_list[:] + [item * item for item in random_numbers_in_list]
print("Наш список новий список такий:", new_list)
# -------------------------------------------

"""
7. Створіть список із 12 елементів. Кожен елемент цього списку є зарплатою робітника за місяць. Виведіть цей список на
    екран та обчисліть середньомісячну зарплату цього робітника.
"""
random_salary_list = [random.randint(1, 100) for _ in range(12)]
print("Список всіх зарплат:", random_salary_list)
average_salary = sum(random_salary_list) / len(random_salary_list)
print("Середня зарплата дорівнює:", average_salary)
# -------------------------------------------

"""
8. Є матриця
    [1, 2, 3, 4]
    [5, 6, 7, 8]
    [9,10, 11, 12]
    [13,14, 15, 16]
    
    Напишіть Python-скрипт, який виведе цю матрицю на екран, обчислить та виведе суму елементів цієї матриці.
"""
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 18, 11, 12],
          [13, 14, 15, 16]]

print("Наша матриця:")
for str_count in matrix:
    print("\t".join(map(str, str_count)))

elements_sum = sum(sum(row) for row in matrix)
print("--------------")
print("Сума всіх елементів цієї матриці =", elements_sum)
# -------------------------------------------

"""
9. Написати код для дзеркального перевороту списку [7,2,9,4] -> [4,9,2,7].
    Список може бути довільною довжиною.
"""
random_list = [random.randint(1, 4) for _ in range(4)]
print("Маємо такий список:", random_list)
random_list.reverse()
print("Тепер, цей список такий:", random_list)
# -------------------------------------------

"""
10. За допомогою циклів вивести на екран усі прості числа від 1 до 100.
"""
count = []

for number in range(1, 101):
    if number > 1:
        for i in range(2, number):
            if(number % i) == 0:
                break
        else:
            count.append(number)

print("Прості числа від 1 до 100 це:", *count)
# -------------------------------------------

"""
11. Виведіть на екран «пісочний годинник», максимальна ширина якого зчитується з клавіатури (число непарне). У прикладі
    ширина дорівнює 5.
        *****
         ***
          *
         ***
        *****
"""
how_many_stars = int(input("Зі скількох зірочок зробити годинник? "))
res = [f"{' ' * j}{'*' * i}\n" for j, i in enumerate(range(how_many_stars, 0, -2))]
res += res[-2::-1]
result = ''.join(res)
print(result)
