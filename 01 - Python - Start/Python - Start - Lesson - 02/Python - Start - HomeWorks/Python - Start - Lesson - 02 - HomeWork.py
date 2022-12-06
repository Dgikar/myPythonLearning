"""
Useful Links:
    Data Model - https://docs.python.org/3/reference/datamodel.html
    Numbers - https://docs.python.org/3/library/stdtypes.html#typesnumeric
    Decimal Numbers - https://docs.python.org/3/library/decimal.html
    Math Module - https://docs.python.org/3/library/math.html
    Random Module - https://docs.python.org/3/library/random.html
-------------------------------------------

1. Write a Python program to print the number entered by user only if the num-ber entered is negative.
"""
entered_number = int(input("Введіть число: "))
if entered_number < 0:
    print("Ура! Ви ввели число, яке менше нуля!")
else:
    print("Введено некоректне число. Програма завершена")

# or

entered_number < 0 and print(entered_number)
# -------------------------------------------

# 2. Write a Python program to check if that value an is less than 20 or not.
entered_number = int(input("Введіть число: "))
if entered_number < 20:
    print("Введене Вами число менше 20")
elif entered_number == 20:
    print("Введене Вами число дорівнює 20")
else:
    print("Введене Вами число, більше 20")
# -------------------------------------------

# 3. Write a Python program to check if a given number is Zero or Not.
entered_number = int(input("Введіть число: "))
if entered_number == 0:
    print("Введене Вами число дорівнює нулю!")
elif entered_number < 0:
    print("Введене Вами число менше нуля")
else:
    print("Введене Вами число більше нуля")
# -------------------------------------------

# 4. Write a Python program to check if a given number is Even or Odd.
entered_number = int(input("Введіть число: "))
if entered_number % 2 == 0:
    print("Введене число парне")
else:
    print("Введене число не парне")
# -------------------------------------------

# 5. Write a Python program to find the largest number among three numbers entered by user.
first_entered_number = int(input("Введіть перше число: "))
second_entered_number = int(input("Введіть друге число: "))
third_entered_number = int(input("Введіть третє число:"))

largest_number = first_entered_number

if second_entered_number > largest_number:
    largest_number = second_entered_number
if third_entered_number > largest_number:
    largest_number = third_entered_number

print("Найбільше число серед введених:", largest_number)
