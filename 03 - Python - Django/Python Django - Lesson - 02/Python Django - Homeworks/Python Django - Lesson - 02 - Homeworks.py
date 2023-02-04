"""
Useful Links:
    regex101: build, test, and debug regex - https://regex101.com
    Regex Generator - https://regex-generator.olafneumann.org/
-------------------------------------------

1. Напишіть регулярний вираз, який знаходитиме в тексті фрагменти, що складаються з однієї літери R,
    за якою слідує одна або більше літер b, за якою одна r. Враховувати верхній та нижній регістр.
"""
import re


def find_regular_expression(text):
    """
    Функція find_regular_expression шукає схожі входження у рядку згідно з патерном регулярного виразу

    :param text: Текст для пошуку співпадіння
    """

    pattern = re.compile(r"[Rr][Bb]+[Rr]")
    return pattern.findall(text)


print("-" * 77, "\n")
print(*find_regular_expression("RbrxwweewdfsfRbbyzvwRbbbr"))
# -------------------------------------------

"""
2. Напишіть функцію, яка виконує валідацію номера банківської картки (9999-9999-9999-9999).
"""


def validate_card_number(text):
    """
    Функція validate_card_number перевіряє, чи дійсний номер картки чи ні.

    :param text: рядок, який представляє номер кредитної картки
    """

    pattern = r"^\d{4}-\d{4}-\d{4}-\d{4}$"
    return "Введений номер карты - правильний" \
        if re.search(pattern, text) else \
        "Ви вказали не вірний номер карти"


print("-" * 77, "\n")
print(validate_card_number("9999-9999-9999-9999"))
print(validate_card_number("9999-9999-9999-99999"))
print(validate_card_number("9999-9999"))
print(validate_card_number("1234567812345678"))
# -------------------------------------------

"""
3. Напишіть функцію, яка приймає рядкові дані та виконує перевірку на їхню відповідність E-Mail.
    Вимоги:
        - цифри (0-9).
        - лише латинські літери у великому (A-Z) та малому (a-z) регістрах.
        - у тілі E-Mail допустимі лише символи "_" і "-". Але вони не можуть бути першим символом E-Mail.
        - символ "-" не може повторюватися.
"""


def validate_email(text):
    """
    Функція validate_email перевіряє, чи є введений E-Mail коректним чи ні.

    :param text: Адреса електронної пошти для перевірки
    """

    pattern = r"^[A-Za-z0-9]+([-._][A-Za-z0-9]+)*@[A-Za-z0-9]+\.[A-Za-z]{2,}$"
    return f"{text} - коректний" if re.search(pattern, text) else f"{text} - не коректний"


print("-" * 77, "\n")
print(validate_email("mail@gmail.com"))
print(validate_email("1mail@gmail.com"))
print(validate_email("1mai0l@gmail.com"))
print(validate_email("1MAI0l@gmail.com"))
print(validate_email("1_mai0l@gmail.com"))
print(validate_email("m_a-il@gmail.com"))
print(validate_email("m-ail@gmail.com"))
print(validate_email("m-ai-l@gmail.com"))
print(validate_email("-mail@gmail.com"))
print(validate_email("ma--il@gmail.com"))
print(validate_email("mail@gmail"))
# -------------------------------------------

"""
4. Напишіть функцію, яка перевіряє правильність логіну.
    Правильний логін – рядок від 2 до 10 символів, що містить лише літери та цифри.
"""


def validate_login(text):
    """
    Функція validate перевіряє, чи є введений логін коректним (повертає True) чи ні (повертає False)

    :param text: Логин пользователя
    """

    pattern = r"^[a-zA-Z0-9]{2,10}$"
    return f"{text} - коректний" if re.search(pattern, text) else f"{text} - не коректний"


print("-" * 77, "\n")
print(validate_login("Dgikar"))
print(validate_login("Dgikar125"))
print(validate_login("1234567890"))
print(validate_login("D"))
print(validate_login("Dgikar12551545"))
