"""
Рішення викладача домашнього завдання з лекції №4
"""


class Box:

    def __init__(self, x: int | float, y: int | float, z: int | float):
        self.x = x
        self.y = y
        self.z = z

    def volume(self) -> int | float:
        return self.x * self.y * self.z

    def __gt__(self, other):
        return self.volume() > other.volume()

    def __lt__(self, other):
        return self.volume() < other.volume()

    def __ge__(self, other):
        return self.volume() >= other.volume()

    def __le__(self, other):
        return self.volume() <= other.volume()

    def __add__(self, other):
        if isinstance(other, Box):
            return self.volume() + other.volume()
        if isinstance(other, int | float):
            return self.volume() + other
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return self.volume() + other
        return NotImplemented

    def __str__(self):
        return f'{self.x} x {self.y} x {self.z}'


x = Box(1, 2, 3)
y = Box(3, 4, 5)

print(x)
print(y)

print(x.__add__(3))
