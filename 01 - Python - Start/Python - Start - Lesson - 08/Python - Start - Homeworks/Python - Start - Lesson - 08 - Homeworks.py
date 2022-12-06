"""
Useful Links:
    Defining Functions: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
    Arguments and parameters: https://docs.python.org/3/faq/programming.html#faq-argument-vs-parameter
    More on Defining Functions: https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
    Arbitrary Argument Lists: https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists
-------------------------------------------

1. Реалізуйте функцію, параметрами якої є два числа та рядок. Повертає вона конкатенацію рядка із сумою чисел.
"""


def concat_sum(number1, number2, string):
    numbers = number1 + number2
    return f"{string}{numbers}"


entered_number1 = int(input("Введіть перше число: "))
entered_number2 = int(input("Введіть друге число: "))
entered_string = str(input("Введіть строку: "))

res = concat_sum(entered_number1, entered_number2, entered_string)
print(res)
# -------------------------------------------

"""
2. Реалізуйте функцію, яка малює на екрані прямокутник із зірочок «*». Її параметрами будуть цілі числа, які описують
    довжину та ширину такого прямокутника.
"""


def square_paint(width_square, height_square):
    for i in range(height_square):
        if i in [0, height_square - 1]:
            for _ in range(width_square):
                print('*', end=' ')
        else:
            print('*', end=' ')
            for _ in range(1, width_square - 1):
                print(' ', end=' ')
            print('*', end=' ')
        print()


width = int(input("Введіть висоту прямокутника: "))
height = int(input("Введіть ширину прямокутника: "))
square_paint(width, height)
# -------------------------------------------

"""
3. Напишіть функцію, яка реалізує лінійний пошук елемента у списку цілих чисел. Якщо такий елемент у списку є,
    то поверніть індекс, якщо ні, то поверніть число «-1».
"""
import random


def find_number_in_list(lst, number):
    return f"Індекс числа {number} - {lst.index(number)}" if desired_number in random_lst else -1


random_lst = [random.randint(1, 10) for _ in range(10)]
print(f"У нас э такий список: {random_lst}")
desired_number = int(input("Яке число шукати? "))

res = find_number_in_list(random_lst, desired_number)
print(res)


# or
def find_number_in_list(lst, number):
    if desired_number in random_lst:
        result = f"Індекс числа {number} - {lst.index(number)}"
    else:
        result = -1

    return result


random_lst = [random.randint(1, 10) for _ in range(10)]
print(f"У нас э такий список: {random_lst}")
desired_number = int(input("Яке число шукати? "))

res = find_number_in_list(random_lst, desired_number)
print(res)
# -------------------------------------------

"""
4. Напишіть функцію, яка поверне кількість слів у текстовому рядку.
"""


def words_per_line(text):
    return len(text.split())

    # or
    result = len(text.split())
    return result


entered_string = str(input("Введіть строку: "))
res = words_per_line(entered_string)
print(f"У введенному Вами рядку, {res} слів")
# -------------------------------------------

"""
5. Напишіть функцію, яка переводить число, що означає кількість доларів і центів, в прописний формат. Наприклад:
    > 123,34
    > one hundred twenty three dollars thirty four cents
"""
big_n = ["", ["тисяча", "тисячі", "тисяч"], ["мільйон", "мільйона", "мільйонів"], ["мільярд", "мільярда", "мільярдів"]]
grn = ["гривня", "гривні", "гривень"]
kop = ["копійка", "копійки", "копійок"]


def reading_and_split(incoming_string_with_digits):
    how_big_summa(incoming_string_with_digits)

    if incoming_string_with_digits in ["0", "0.0", "0,0", "0.00", "0,00"]:
        entered_zero(incoming_string_with_digits)

    list_for_split = [".", ",", " ", "_", "-", "=", ";", ":"]
    for i in range(len(list_for_split)):
        if incoming_string_with_digits.find(list_for_split[i]) != -1:
            return incoming_string_with_digits.split(list_for_split[i])
    else:
        return [incoming_string_with_digits, "0"]


def entered_zero(incoming_zero):
    print("Ви вказали: ноль гривень ноль копійок")
    quit()


def how_big_summa(summa_grn):
    if len(str(summa_grn)) < 16:
        return
    print("Вибачте, але це дуже велика цифра")
    quit()


def sum_gluing(digit):
    temp_for_digit = []

    for index, value in enumerate(digit):
        if not index:
            temp_for_digit.append(int(value))
        elif index:
            if len(value) == 1:
                temp_for_digit.append(int(value + '0'))
            else:
                temp_for_digit.append(int(value))
    digit = temp_for_digit

    res_grn = [declination(digit[0] % 1000, grn)]
    res_kop = [declination(digit[1] % 1000, kop)]

    if digit[0]:
        for i in range(4):
            if temp := digit[0] % 1000:
                res_grn.append(declination(temp, big_n[i]))
                res_grn.extend(convert_to_words(temp))
            digit[0] //= 1000

        res_grn.reverse()

    else:
        res_grn = ["ноль гривень"]

    if digit[1]:
        for i in range(4):
            if temp2 := digit[1] % 1000:
                res_kop.append(declination(temp2, big_n[i]))
                res_kop.extend(convert_to_words(temp2))
            digit[1] //= 1000

        res_kop.reverse()

    else:
        res_kop = ["ноль копійок"]

    res_grn += res_kop
    res_grn = " ".join(list(filter(None, res_grn)))
    res_grn = replace_word(res_grn)
    return res_grn


def declination(summa, sting_grn_and_kop):
    if not sting_grn_and_kop:
        return ""

    f1 = (summa % 100) // 10 != 1 and summa % 10 == 1
    f2 = (summa % 100) // 10 != 1 and summa % 10 in [2, 3, 4]

    return sting_grn_and_kop[0] if f1 else sting_grn_and_kop[1] if f2 else sting_grn_and_kop[2]


def convert_to_words(incoming_summa):
    num = ["", "один", "два", "три", "чотири", "п'ять", "шість", "сім", "вісім", "дев'ять", "десять", "одинадцять",
           "дванадцять", "тринадцять", "чотирнадцять", "п'ятнадцять", "шістнадцять", "сімнадцять", "вісімнадцять",
           "дев'ятнадцять"
           ]

    list_for_word = []

    if incoming_summa // 100:
        hundred = ["", "сто", "двісті", "триста", "чотириста", "п'ятсот", "шістсот", "сімсот", "вісімсот", "дев'ятсот"]

        list_for_word.append(hundred[incoming_summa // 100])

    if (incoming_summa // 10) % 10 > 1:
        dozens = ["", "", "двадцять", "тридцять", "сорок", "п'ятдесят", "шістдесят", "сімдесят", "вісімдесят",
                  "дев'яносто"
                  ]

        list_for_word.extend((dozens[(incoming_summa // 10) % 10], num[incoming_summa % 10]))
    else:
        list_for_word.extend(["", num[incoming_summa % 100]])
    return list_for_word[::-1]


def replace_word(word):
    return word \
        .replace("один копійка", "одна копійка") \
        .replace("два копійки", "дві копійки") \
        .replace("один гривня", "одна гривня") \
        .replace('два гривні', 'дві гривні') \
        .replace("один тисяча", "тисяча") \
        .replace('два тисячі', 'дві тисячі')


reading_and_split_sum = reading_and_split(input("Введіть сумму (можна і з копійками): "))
sum_in_words = sum_gluing(reading_and_split_sum)

print(sum_in_words.capitalize())
# -------------------------------------------
"""
6. Напишіть функцію, яка переводить ціле число з римського запису до десяткового.
    Наприклад: XXII -> 22
        Докладніше: https://en.wikipedia.org/wiki/Roman_numerals
"""


def how_big_entered_number(digit):
    if digit <= 3999:
        return digit
    print("Вибачте, але це дуже велика цифра")
    quit()


def roman_to_arabic(entered_roman_digits):
    roman_digits_dict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

    res = 0
    for i, c in enumerate(entered_roman_digits):
        if i + 1 < len(entered_roman_digits) and roman_digits_dict[entered_roman_digits[i]] < roman_digits_dict[
            entered_roman_digits[i + 1]]:
            res -= roman_digits_dict[entered_roman_digits[i]]
        else:
            res += roman_digits_dict[entered_roman_digits[i]]

    how_big_entered_number(res)
    return res


def arabic_to_roman(arabic_digits):
    units = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    dozens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thousands = ["", "M", "MM", "MMM"]

    res_units = units[arabic_digits % 10]
    res_dozens = dozens[arabic_digits // 10 % 10]
    res_hundreds = hundreds[arabic_digits // 100 % 10]
    res_thousands = thousands[arabic_digits // 1000]

    return res_thousands + res_hundreds + res_dozens + res_units


entered_summa = (input("Введіть (або римськими, або арабським) ціле число: "))

if entered_summa.isalpha():
    print(
        f"Коли в древньому Римі написали '{entered_summa}', то це значить що це {roman_to_arabic(entered_summa)}")
else:
    print(f"Число {entered_summa}, у древньому Римі написали б так:", arabic_to_roman(int(entered_summa)))
