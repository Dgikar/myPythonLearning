"""
Properties
"""


class Student:

    def __init__(self, surname, name, passport):
        self.surname = surname
        self.name = name
        self.passport = passport

    @property
    def passport(self):
        return f'UA {self.__passport}'

    @passport.setter
    def passport(self, value):
        if not isinstance(value, str):
            raise TypeError()
        if len(value.strip()) != 6:
            raise ValueError()

        self.__passport = value

    @passport.deleter
    def passport(self):
        ...

    def __str__(self):
        return f'{self.surname} {self.name} {self.passport}'


x = Student('Ivanov', 'Ivan', '123456')
print(x.passport)
del x.passport

print(x)
# -------------------------------------------

"""
getattr, setattr, delattr
"""


class Student:
    __attrs = ('surname', 'name', 'passport', 'age', 'birth_date', 'nationality')

    def __init__(self, surname, name, passport):
        self.surname = surname
        self.name = name
        self.passport = passport

    def __getattr__(self, item):
        if item in Student.__attrs:
            self.__dict__[item] = None
            return self.__dict__[item]
        else:
            raise AttributeError()

    def __setattr__(self, key, value):
        if key in Student.__attrs:
            if key == 'nationality' and value.lower() == 'russion':
                raise ValueError('Russion boat go to the ***')
            self.__dict__[key] = value
        else:
            raise AttributeError()

    def __delattr__(self, item):
        if item in ('surname', 'name', 'passport'):
            ...
        else:
            del self.__dict__[item]

    def __str__(self):
        return '; '.join(map(lambda item: f'[{item[0]}]: {item[1]}', self.__dict__.items()))


x = Student('Ivanov', 'Ivan', '123456')
x.age = 20
x.nationality = 'Ukranian'
del x.age

print(x)
# -------------------------------------------

"""
getattribute
"""


class Student:
    __attrs = ('surname', 'name', 'passport', 'age', 'birth_date', 'nationality')

    def __init__(self, surname, name, passport):
        self.surname = surname
        self.name = name
        self.passport = passport

    def __getattribute__(self, item):
        try:
            return object.__getattribute__(self, item)
        except AttributeError:
            if item in Student.__attrs:
                self.__dict__[item] = None
                return self.__dict__[item]

    def __setattr__(self, key, value):
        if key in Student.__attrs:
            if key == 'nationality' and value.lower() == 'russion':
                raise ValueError('Russion boat go to the ***')
            self.__dict__[key] = value
        else:
            raise AttributeError()

    def __delattr__(self, item):
        if item in ('surname', 'name', 'passport'):
            ...
        else:
            del self.__dict__[item]

    def __str__(self):
        return '; '.join(map(lambda item: f'[{item[0]}]: {item[1]}', self.__dict__.items()))


x = Student('Ivanov', 'Ivan', '123456')
x.age = 20
x.nationality = 'Ukranian'
del x.age

print(x)
# -------------------------------------------

"""
Descriptors
"""
import uuid


class MyDescriptor:

    def __init__(self, attr_name):
        self.attr_name = attr_name

    def __get__(self, instance, owner):
        if not instance.__dict__.get(self.attr_name):
            instance.__dict__[self.attr_name] = uuid.uuid4()
        return instance.__dict__.get(self.attr_name)

    def __del__(self):
        pass


class Student:

    def __init__(self, surname, name, passport):
        self.surname = surname
        self.name = name
        self.passport = passport

    id = MyDescriptor('id')


x = Student('Ivanov', 'Ivan', '123456')
print(x.id)
# -------------------------------------------

"""

"""
