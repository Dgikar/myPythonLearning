def i_tag_text(func):
    def inner(*args, **kwargs):
        return f'<i>{func(*args, **kwargs)}</i>'

    return inner


def b_tag_text(func):
    def inner(*args, **kwargs):
        return f'<b>{func(*args, **kwargs)}</b>'

    return inner


def greetings(name):
    return f'Hello, {name}'


text = i_tag_text(b_tag_text(greetings))

print(text('Oleh'))
# -------------------------------------------

print()


def i_tag_text(func):
    def inner(*args, **kwargs):
        return f'<i>{func(*args, **kwargs)}</i>'

    return inner


def b_tag_text(func):
    def inner(*args, **kwargs):
        return f'<b>{func(*args, **kwargs)}</b>'

    return inner


@i_tag_text
def greetings(name):
    return f'Hello, {name}'


@i_tag_text
@b_tag_text
def greetings_by_s_n(surname, name):
    return f'Hello, {surname} {name[0]}.'


str_text = input("Введыть що-небудь: ").strip().split()
if len(str_text) == 1:
    print(greetings(*str_text))
elif len(str_text) == 2:

    print(greetings_by_s_n(*str_text))
