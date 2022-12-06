"""
1. Скільки разів у словнику (dictionary) зустрічається буква L у Hello, World!
"""
entered_string = input("Введіть рядок: ")
char_to_finde = input("Введіть літеру для перевірки: ")
res = {}
temp = 0

for item in entered_string:
    if item.isalpha() and not res.get(item):
        res[item] = entered_string.count(item)

    temp = res.get(char_to_finde)

# print("Словник виглядає так:", res)
print("Кількість входжень:", temp)
# -------------------------------------------


# -------------------------------------------
