"""
Работа со строками

Если в print() вставить %s, то вместо %s можно подставить значение переменной. Например:
"""

a = 20
b = 50
print("У меня есть %s гривен и %s копеек" % (a, b))

# или

print(f"У меня есть {a} гривен и {b} копеек")        # это называется F строка
# --------------------

s = input("Text = ")

while '  ' in s:                # вместо '  ' может быть любая строка или переменная
    s = s.replace('  ', ' ')    # в первых кавычках, указываю что менять, а во вторых, на что менять
print(s)
# --------------------

a=(input())
patterrn = ",.!;:"

for i in a:
    if i in patterrn:
        a.replace(i, " ")

print(a)
# --------------------

import string
s = input("text=")

for i in f"{string.punctuation}":
    while i + i in s:
        s = s.replace(i * 2, i)
print(s)
# --------------------

s = 'kkljkljkl,lkll:kjhkjhjkk         ,sdfsdf,,,,sdfdsfsdf'
simvol = '''!()-[]{};?@#$%:'"\,./^&amp;*_'''
for i in s:
    if i in simvol or '  ' in i:
        s = s.replace(i, ' ')
        s = s.replace('  ', ' ')
print(s)

# или верный вариант:

text = "kkljkljkl,lkll:kjhkjhjkk         ,sdfsdf,,,,sdfdsfsdf"
import string
for item in string.punctuation:
    text = text.replace(item, " ")

res = text.split()
print(' '.join(res))
print(len(res))
# --------------------
