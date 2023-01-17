def volume(self):
    return self.x * self.y * self.z


def add_attr(cls):
    def inner(*args, **kwargs):
        new_instance = cls(*args, **kwargs)
        new_instance.title = 'volume'
        return new_instance

    return inner


@add_attr
class Box:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'{self.x}x{self.y}x{self.z}'


x_1 = Box(1, 2, 3)
print(x_1.__dict__)
x_2 = Box(4, 2, 3)


# -------------------------------------------

def decorator_upper_str(func):
    def inner(*args, **kwargs):
        return f'{func(*args, **kwargs)}'.upper()

    return inner


def decorator_add_str(func):
    def inner(*args, **kwargs):
        return f'*{func(*args, **kwargs)}*'

    return inner


@decorator_upper_str
@decorator_add_str
def get_str(name):
    return f'Hello, {name}'


print(get_str('Oleh'))
