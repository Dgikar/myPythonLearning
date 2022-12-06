"""
1. Існують такі послідовності чисел:
    0,2,4,6,8,10,12
    1,4,7,10,13
    1,2,4,8,16,32
    1,3,9,27
    1,4,9,16,25
    1,8,27,64,125

    Реалізуйте програму, яка виведе наступний член цієї послідовності (або подібної до них) на екран.
    Послідовність користувач вводить з клавіатури у вигляді рядка. Наприклад, користувач вводить рядок 0,5,10,15,20,25
    та відповіддю програми має бути число 30.
"""


def reading_and_split(incoming_string_with_sequence):
    if len(incoming_string_with_sequence) <= 1:
        print("Ви не ввели послідовність.\n"
              "Введіть наприклад так: 0,5,10,15,20,25...\n"
              "А поки, программа завершена!")
        quit()

    list_for_split = [".", ",", " ", "_", "-", "=", ";", ":"]
    for item in list_for_split:
        if incoming_string_with_sequence.find(item) != -1:
            arithmetic_progression(list(map(int, incoming_string_with_sequence.split(item))))


def calsulating_and_check(entered_sequence, progression_name):
    difference = 0
    difference_temp = 0
    temp_list = []

    for index, value in enumerate(entered_sequence):
        if index == 0 and progression_name == "арифметическая":
            difference = value - entered_sequence[1]
        elif index == 0 and progression_name == "геометрическая":
            difference = value // entered_sequence[1]
        elif index != 0 and progression_name == "арифметическая":
            difference_temp = abs(value - entered_sequence[index - 1])
        elif index != 0 and progression_name == "геометрическая":
            difference_temp = entered_sequence[index - 1] // value
        elif progression_name == "экспоненциальная":
            for degree in range(1, len(entered_sequence)):
                temp_list.clear()
                for i in range(1, len(entered_sequence) + 1):
                    temp = i ** degree
                    difference_temp = (i + 1) ** degree
                    temp_list.append(temp)
                    if temp_list == entered_sequence:
                        result_calculation(difference_temp, progression_name)
            break
        else:
            result_calculation(entered_sequence, "None")

    if difference == difference_temp and progression_name == "арифметическая":
        entered_sequence.reverse()
        result_calculation(entered_sequence[-1] + difference, progression_name)
    elif progression_name == "арифметическая":
        geometric_progression(entered_sequence)

    if difference == difference_temp and progression_name == "геометрическая":
        entered_sequence.reverse()
        result_calculation(entered_sequence[-1] * difference, progression_name)
    elif progression_name == "геометрическая":
        exponential_progression(entered_sequence)


def arithmetic_progression(entered_sequence):
    entered_sequence.reverse()
    progression_name = "арифметическая"
    calsulating_and_check(entered_sequence, progression_name)


def geometric_progression(entered_sequence):
    progression_name = "геометрическая"
    calsulating_and_check(entered_sequence, progression_name)


def exponential_progression(entered_sequence):
    entered_sequence.reverse()
    progression_name = "экспоненциальная"
    calsulating_and_check(entered_sequence, progression_name)


def result_calculation(next_element_entered_sequence, what_progression):
    if what_progression != "":
        print(
            f"Это {what_progression} прогрессия и следующий элемент этой последовательности: {next_element_entered_sequence}")
    else:
        print("Это бессмысленная последовательность!")


# arithmetic_progression([0, 2, 4, 6, 8, 10, 12])
# arithmetic_progression([1, 4, 7, 10, 13])
# arithmetic_progression([1, 2, 4, 8, 16, 32])
# arithmetic_progression([1, 3, 9, 27])
# arithmetic_progression([1, 4, 9, 16, 25])
# arithmetic_progression([1, 8, 27, 64, 125])
# arithmetic_progression([1, 16, 81, 256, 625])

reading_and_split(input("Введіть рядок (наприклад 0,5,10,15,20,25): "))
# -------------------------------------------

"""
2. Число-паліндром з обох сторін (справа ліворуч і ліворуч) читається однаково.
    Найбільше число-паліндром, одержане множенням двох двозначних чисел: 9009 = 91 × 99.
    Знайдіть найбільший паліндром, одержаний множенням двох трицифрових чисел.
    Виведіть значення цього паліндрому і те, множенням яких чисел він є.
"""


def multiplication_and_search_palindrome(number1, number2):
    multiplier1 = 0
    multiplier2 = 0
    temp_palindrome = 0

    for i in range(number1, number2):
        temp_multiplier1 = i
        for item in range(i, number2):
            temp_multiplier2 = item
            item *= i
            palindrome = str(item)

            if palindrome == palindrome[::-1] and int(temp_palindrome) <= int(palindrome):
                temp_palindrome = int(palindrome)
                multiplier1 = temp_multiplier1
                multiplier2 = temp_multiplier2

    printing_palindrome_and_multiplication_result(temp_palindrome, multiplier1, multiplier2)


def printing_palindrome_and_multiplication_result(palindrome, multiplier1, multiplier2):
    print(f"Маємо паліндром: {palindrome}, він з'явився завдяки множенною {multiplier1} * {multiplier2}")


multiplication_and_search_palindrome(1000, 10000)
