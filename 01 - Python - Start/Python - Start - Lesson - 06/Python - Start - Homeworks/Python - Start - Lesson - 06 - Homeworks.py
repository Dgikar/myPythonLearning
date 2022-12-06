"""
Useful Links:
    str - https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
-------------------------------------------

1. Напишіть програму, яка порахує скільки літер «b» у введеному рядку тексту.
"""
entered_string = input("Введіть будь-яке слово, яке в собі має букву \"Б\": ")
print(f"Буква \"Б\" у цьому слові, зустрічається", entered_string.count('б'), "рази")
# -------------------------------------------

"""
2. Користувач вводить з клавіатури ім'я людини.
    Написати програму для перевірки введеного ім'я на валідність (мається на увазі, що, наприклад, в імені людини не
    може бути цифр, воно повинно починатися з великої літери, за якою повинні йти маленькі).
"""
entered_string = input("Введіть Ваше ім`я: ")
extra_char = []
count = 0

if entered_string.islower():
    print(f"Ви ввели своє ім`я з маленької літери! Виправляю! Привіт, {entered_string.capitalize()}")
elif entered_string.isnumeric():
    print("Ваше ім`я складається з цифр?")
else:
    for char in entered_string:
        if not char.isdigit():
            extra_char.append(char)
        else:
            count = 1
            break
    if count == 1:
        print("Ви ввели в своєму імені якийсь зайвий символ!")
    else:
        print("Привіт, ", *extra_char, sep="")
"""
    Можна було б звичайно зупинитися на першому ELIF, зробивши перевірку на isalnum(), але захотілося трохи розписати...
    Хотів ще зробити перевірку на те, що користувач ввів ім'я з маленької літери і туди ж вписав цифру, але не став
    цього робити...
"""
# Правильне рішення (версія викладача):
entered_string = input("Введіть Ваше ім`я: ")
if entered_string.isalpha() or entered_string.istitle():
    print("Valid")
else:
    print("Invalid")
# -------------------------------------------

"""
3. Напишіть програму, яка обчислить суму всіх кодів символів рядка.
"""
entered_string = input("Введіть строку: ")
len_entered_string = len(entered_string)
letter_code_list = []

for letter_code in range(len_entered_string):
    letter_code_list.append(ord(entered_string[letter_code]))

print("Сума всіх кодів символів рядка =", sum(letter_code_list))

# іще такий варіант (більш продвинутий):
entered_string = input("Введіть строку: ")
len_entered_string = len(entered_string)
letter_code_list = [ord(entered_string[letter_code]) for letter_code in range(len_entered_string)]

print("Сума всіх кодів символів рядка =", sum(letter_code_list))

# Правильне рішення (версія викладача):
entered_string = input("Введіть строку: ")
res = 0

for item in entered_string:
    res += ord(item)

print("Сума всіх кодів символів рядка =", res)

# іще такий варіант правильного рішення (більш продвинутий):
entered_string = input("Введіть строку: ")
res = sum(ord(item) for item in entered_string)

print("Сума всіх кодів символів рядка =", res)
# -------------------------------------------

"""
4. Виведіть на екран 10 рядків із значенням числа Pi. У першому рядку має бути 2 знаки після коми, у другому 3 і т. д.
"""
import math

print("Pi =", math.pi)

for i in range(10):
    print(math.pi[:i + 4])

# Правильне рішення (версія викладача):
import math

print("Pi =", math.pi)

for i in range(2, 12):
    print(f"{math.pi:.{i}f}")
# -------------------------------------------

"""
5. Вводиться з клавіатури користувачем текст. Знайти в ньому найдовше слово та вивести його на екран.
"""
# Це правильне рішення та більш лаконічне:
entered_string = input("Введіть строку: ")
print(max(entered_string.split(), key=len))

# Правильне рішення (версія викладача):
entered_string = input("Введіть строку: ")

entered_string = entered_string.split()
print(max(entered_string, key=len))
# -------------------------------------------

"""
Додаткові задачі до домашнього завдання:
1. Вовочка, сидячи на уроці, писав поспіль однакові слова (слово може складатися з однієї літери). Коли Марія Іванівна
    забрала у нього зошит, там був один рядок тексту. Напишіть програму, яка визначить найкоротше слово з написаних
    Вовочкою. Наприклад:
        aaaaaaa - Вовочка писав слово - "a"
        ititititit - Вовочка писав слово - "it"
        catcatcatcat - Вовочка писав слово - "cat"
"""
wowan_word = input("Введіть слово: ")
len_wowan_word = len(wowan_word)

for i in range(len_wowan_word):
    if i < len_wowan_word:
        temp = wowan_word[:i]

        if wowan_word.count(temp) * len(temp) == len(wowan_word):
            print(temp)
            break
else:
    print("Це слово написав не Вовочка!")

# Правильне рішення (версія викладача):
wowan_word = input("Введіть слово: ")
len_wowan_word = len(wowan_word)

for i in range(1, len(wowan_word) // 2 + 1):
    temp = wowan_word[:i]
    if len(temp) * wowan_word.count(temp) == len_wowan_word:
        print(temp)
        break
else:
    print("Це слово написав не Вовочка!")

# Правильне рішення (версія викладача) з перевіркою на час виконання:
stp = """
wowan_word = input("Введіть слово: ")
"""
import timeit
s = """
len_wowan_word = len(wowan_word)

for i in range(1, len(wowan_word) // 2 + 1):
    temp = wowan_word[:i]
    if len(temp) * wowan_word.count(temp) == len_wowan_word:
        print(temp)
        break
else:
    print("Це слово написав не Вовочка!")
"""
print(timeit.timeit(s, setup=stp, number=1000))
# -------------------------------------------

"""
2. Напишіть програму для очищення тексту від HTML-тегів. Більше про html-теги https://html5book.ru/html-tags
    
    Також необхідно врахувати кілька особливостей:
        - крім одинарних тегів є парні теги, наприклад <div> </div>, тобто. перший тег відкриває, а другий закриває.
        - тег у собі може містити купу додаткової інформації.
            Наприклад <div id="rcnt" style="clear:both;position:relative;zoom:1">
"""
import re

html_text = "<ul uk-accordion=\"collapsible: false\"><li><a class=\"uk-accordion-title\" href=\"#\">Item 1</a>" \
            "<divclass=\"uk-accordion-content\"><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do" \
            "eiusmod tempor</p></div></li><li><a class=\"uk-accordion-title\" href=\"#\">Item 2</a>" \
            "<div class=\"uk-accordion-content\"><p>Ut enim ad minim veniam, quis nostrud exercitation ullamco" \
            "laboris nisi ut aliquip</p></div></li><li><a class=\"uk-accordion-title\" href=\"#\">Item 3</a>" \
            "<div class=\"uk-accordion-content\"><p>Duis aute irure dolor in reprehenderit in voluptate velit esse" \
            "cillum dolore eu fugiat nulla pariatur</p></div></li></ul>"

print(re.sub(r'<.*?>', '', html_text))

# Правильне рішення (версія викладача):
html_text = """
<ul uk-accordion>
    <li class="uk-open">
        <a class="uk-accordion-title" href="#">Item 1</a>
        <div class="uk-accordion-content">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut</p>
        </div>
    </li>
    <li>
        <a class="uk-accordion-title" href="#">Item 2</a>
        <div class="uk-accordion-content">
            <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo</p>
        </div>
    </li>
    <li>
        <a class="uk-accordion-title" href="#">Item 3</a>
        <div class="uk-accordion-content">
            <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur</p>
        </div>
    </li>
</ul>
"""
while "<" in html_text:
    start = html_text.find("<")
    stop = html_text.find(">")
    html_text = html_text.replace(html_text[start:stop + 1], "")

while "  " in html_text:
    html_text = html_text.replace("  ", " ")

html_text = html_text.replace("\n", "").strip()
print(html_text)
