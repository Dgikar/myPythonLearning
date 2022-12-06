"""
Список использованной литературы:
    1) Лутц М. Изучаем Python, 4-е издание. - Пер. с англ. - СПб.: Символ-Плюс, 2011. - 121-126 стр.
    2) Саммерфилд М. Программирование на Python 3. Подробное руководство. - Пер. с англ. - СПб.:Символ-Плюс, 2009. - 69-76 с.
"""


# Homework 1
# Exercise 1. Write a Python-script that displays the message “Hello world”. sourcery skip: sum-comprehension
print("Hello world")
# --------------------

# Exercise 2. Rewrite the first script to display three any messages.
print("First message", "Second massage", "Third message")

# or
print("First message", "Second massage", "Third message.", sep=", ")
# --------------------

# Exercise 3. Write a Python-script to reads values for the length and width of a rectangle and returns the area of
# the rectangle
rectangle_length = int(input("Введіть довжину: "))
rectangle_width = int(input("Введіть ширину: "))
print("Площа прямокутника:", rectangle_length * rectangle_width)

# or
rectangle_area = rectangle_length * rectangle_width
print("Площа прямокутника:", rectangle_area)
# --------------------

# Exercise 4. Write a program that requests the user to enter two numbers and prints the sum, product, difference,
# and quotient of the two numbers.
number_one = int(input("Введіть перше число: "))
number_two = int(input("Введіть друге число: "))
print("Результатом додавання буде:", number_one + number_two)
print("Результатом віднімання буде:", number_one - number_two)
print("Результатом множення буде:", number_one * number_two)
print("Результатом поділу буде:", number_one // number_two)
print("Результатом поділу із залишком буде:", number_one / number_two)
# --------------------

# Exercise 5. Write a program that reads in the radius of a circle and prints the circle’s diameter, circumference
# and area. Use the constant value 3.14159 for π.
pi = 3.14159
radius = float(input("Введіть радіус кола: "))
diametr = radius * 2
area = pi * radius ** 2
print("Радіус кола дорівнює:", radius)
print("Діаметр кола дорівнює:", diametr)
print("Довжина кола дорівнює:", 2 * pi * radius)
print("Площа кола дорівнює:", area)

# -------------------------------------------

# Homework 2
# 1. Construct an integer from the string "123"
string_line = "123"
print("Дані у змінній string_line відносяться до", type(string_line))
digital_line = int(string_line)
print("Дані у змінній digital_line відносяться до", type(digital_line))
# --------------------

# 2. Create a floating point number from the integer 123
my_integer = int(input("Введіть ціле число: "))
my_float = float(my_integer)
print("Ви ввели число", my_integer, "це -", type(my_integer))
print("Після наведення типів, ціле число", my_integer, "стало числом ", type(my_float), "т. е.: ", my_float)
# --------------------

# 3. Create an integer from the floating point number 12.345
my_float = 12.345
my_integer = int(my_float)
print("Число", my_float, "це -", type(my_float))
print("Після приведення типів, число з плаваючою комою,", my_float, "стало цілим числом -", type(my_integer), "тобто: ",
      my_integer)
# --------------------

# 4. Write a Python script that determines the last 4 digits of a credit card.
card_number = input("ВВведіть Ваш номер банківської картки (16-ть цифр): ")
print("Останні 4-и цифри: ", card_number[-4:])
# --------------------

# 5. Write a Python script that calculates the sum of the digits of a three-digit number.
enter_digits = input("Введіть тризначне число:")
enter_digits_sum = int(enter_digits[0]) + int(enter_digits[1]) + int(enter_digits[2])
print("Сума цифр тризначного числа:", enter_digits_sum)
# --------------------

# 6. Write a program that calculates and displays the area of a triangle if its sides are known
triangle_side = int(input("Введіть довжину сторони трикутника: "))
triangle_height = int(input("Введіть висоту трикутника: "))
triangle_area = triangle_side * triangle_height / 2
print("Площа трикутника дорівнює:", triangle_area)
# --------------------

# 7. * Write a Python script that calculates the sum of the digits of a number
enter_digits = input("Введіть будь-яке число:")
length_enter_digits = len(enter_digits)
digits_sum = sum(int(enter_digits[i]) for i in range(length_enter_digits))

print("Сума введених чисел:", digits_sum)

# або інший варіант:
enter_digits = input("Введіть будь-яке число:")
length_enter_digits = len(enter_digits)
digits_sum = 0

for i in range(length_enter_digits):
    digits_sum += int(enter_digits[i])

print("Сума введених чисел:", digits_sum)
# --------------------

# 8. * Determine the number of digits in a number
enter_digits = input("Введіть будь-яке число:")
length_enter_digits = len(enter_digits)
print("Ви ввели", length_enter_digits, "цифр")
# --------------------

# 9. *Print the numbers in reverse order
enter_word = input("Введіть будь-яке слово:")
print(enter_word[::-1])
# --------------------

"""
10. Написати програму, яка зчитує 5-ти значне число з клавіатури та виводить цифри, з якої воно складається.
    Наприклад: Зчитується число 54698
        Виводиться:
            5
            4
            6
            9
            8
"""
number = int(input("Введіть п'ятизначне число: "))
part_one = number // 10000
part_two = number % 10000 // 1000
part_three = number % 1000 // 100
part_four = number % 100 // 10
part_five = number % 10 // 1

print(part_one)
print(part_two)
print(part_three)
print(part_four)
print(part_five)
# --------------------
