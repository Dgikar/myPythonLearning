"""
Useful Links:
    Tuples: https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists
-------------------------------------------

1. Використовуючи словник, напишіть програму, яка виведе на екран назву дня тижня за номером.
    Наприклад, 1 - "Monday".
"""
choices_day = int(input("Введіть номер дня тижня: "))
days_of_week = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

if choices_day == 0:
    print(choices_day + 1, " - ", days_of_week.get(choices_day + 1))
elif choices_day >= 1 and choices_day <= 7:
    print(choices_day, " - ", days_of_week.get(choices_day))
# -------------------------------------------

"""
2. Опишіть кота (домашня тварина) на основі словника.
"""
print("Давайте опишемо Вашу кішку:")
cat_description_name = input("Як її звати? ")
cat_description_eyes = input("Які в неї очі? ")
cat_description_tail = input("Який в неї хвіст? ")
cat_description_color = input("Який в неї колір? ")

cat = {
    "name": cat_description_name,
    "eyes": cat_description_eyes,
    "tail": cat_description_tail,
    "color": cat_description_color
}

print(cat)
# -------------------------------------------

"""
3. Напишіть програму, яка читає рядок тексту з клавіатури і виводить на екран статистику, скільки разів яка літера
    зустрічається в цьому рядку.
        Наприклад, для рядка «Hello world» ця статистика виглядає так: «H» - 1, «e» - 1, «l» - 3 і т.д.
"""
word = input("Введіть слово: ")
temp = ""

for i in word:
    if i not in temp and i.isalpha():
        print(f"{i}: {word.count(i)}")
        temp += i
"""
т. я. я запізнився із виконанням домашнього завдання, и Ви вже на уроці розібрали це завдання, то я вирішив зробити це
завдання не копіюючи Ваше рішення, хоча, я написав і своє рішення, схоже з Вашим (див. нижче):
"""
char_in_word = {i: word.count(i) for i in word if i.isalpha()}
char_in_word = "\n".join(map(lambda i: f"{i[0]}: {i[1]}", char_in_word.items()))

print(char_in_word)
# -------------------------------------------

"""
4. Напишіть програму, яка прочитає два рядки тексту з клавіатури і виведе на екран літери, які є одночасно і в першому,
   і в другому рядку. Наприклад, для рядків «Hello» та «World» на екрані мають бути літери «l» та «o».
"""
first_word = set(input("Введіть перше слово: "))
second_word = set(input("Введіть друге слово: "))

result = {item for item in first_word & second_word if item.isalpha()}

"""
той же результат, але замість & можна використати функцію .intersection()
"""
result = {item for item in first_word.intersection(second_word) if item.isalpha()}
print(result)
# -------------------------------------------

"""
5. Напишіть програму, яка згенерує два списки. Один із числами кратними 3, інший із числами кратними 5.
"""
number1 = list(range(3, 100, 3))
number2 = list(range(5, 100, 5))

print(set(number1) & set(number2))

"""
той же результат, але замість & можна використати функцію .intersection()
"""
res = list(set(number1) & set(number2))
print(res)
# -------------------------------------------
