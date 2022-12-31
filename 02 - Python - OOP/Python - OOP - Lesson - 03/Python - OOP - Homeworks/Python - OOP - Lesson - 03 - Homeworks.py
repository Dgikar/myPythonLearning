"""
1. Модифікуйте Перше домашнє завдання так, щоб при спробі встановити від'ємну або нульову вартість товару викликалася
    виняткова ситуація (тип виняткової ситуації треба самостійно реалізувати).
"""


class PriceItemCannotBeLessThanOrEqualZero(Exception):
    """ Exception виникає тоді, коли користувач ввів ціну товару меншу або яка дорівнює нулю """

    def __init__(self, product_price):
        self.product_price = product_price

    def __str__(self):
        return f"Ціна не може бути менше або дорівнювати нулю! Вказана ціна: {self.product_price} грн."


class ProductPriceIsNotIntOrFloat(Exception):
    """ Exception виникає тоді, коли користувач ввів ціну товару не цифрами, а рядком або замість нуля,
        використав букву "О" """

    def __init__(self, product_price):
        self.product_price = product_price

    def __str__(self):
        return f'Ціна "{self.product_price}" грн. має бути вказана цифрами (можливо з копійками).' \
               f'Введено рядок чи букву "O"'


class IncorrectProductQuantityEntered(Exception):
    """ Exception виникає тоді, коли користувач ввів кількість товару не цифрами, а рядком або замість нуля,
        використав букву "О" """

    def __init__(self, product_quantity):
        self.product_quantity = product_quantity

    def __str__(self):
        return f'Кількість товару "{self.product_quantity}" має бути вказана цілим або дійсним числом. ' \
               f'Введено рядок чи букву "O"'


class SelectedItemWhichIsNotAvailable(Exception):
    """ Exception виникає тоді, коли користувач вибрав товар, якого немає у списку """

    def __init__(self, buyer_chose: int, number_of_items_in_product_list: int):
        self.buyer_chose = buyer_chose
        self.number_of_items_in_product_list = number_of_items_in_product_list

    def __str__(self):
        return f'Обрано товар за номером: "{self.buyer_chose}". Такого товару, немає у списку. ' \
               f'Всього у списку {self.number_of_items_in_product_list} товара'


class QuantityOfProductIsNotAvailableInStock(Exception):
    """ Exception виникає тоді, коли користувач вибрав кількість товару, якої немає у наявності """

    def __init__(self, buyer_chose: int, number_of_items_in_product_list: int):
        self.buyer_chose = buyer_chose
        self.number_of_items_in_product_list = number_of_items_in_product_list

    def __str__(self):
        return f'Введено кількість: {self.buyer_chose} шт. ' \
               f'Всього в наявності: {self.number_of_items_in_product_list} шт.'


class WrongChoiceAdditionalAction(Exception):
    """ Exception виникає тоді, коли користувач ввів не вірний номер додаткової дії """

    def __init__(self, additional_buyer_chose: int):
        self.additional_buyer_chose = additional_buyer_chose

    def __str__(self):
        return f'Введено: "{self.additional_buyer_chose}". Потрібно або "1" або "0"'


class Product:
    def __init__(self,
                 product_name: str,
                 product_desc: str,
                 product_dimensions_length: int,
                 product_dimensions_width: int,
                 product_price: float,
                 product_quantity: float):
        if not isinstance(product_price, float | int):
            raise ProductPriceIsNotIntOrFloat(product_price)
        elif product_price <= 0:
            raise PriceItemCannotBeLessThanOrEqualZero(product_price)
        elif not isinstance(product_quantity, float | int):
            raise IncorrectProductQuantityEntered(product_quantity)

        self.product_name = product_name
        self.product_desc = product_desc
        self.product_dimensions_length = product_dimensions_length
        self.product_dimensions_width = product_dimensions_width
        self.product_price = product_price
        self.product_quantity = product_quantity

    def __str__(self):
        return f"{self.product_name}\n" \
               f"   Опис: {self.product_desc}\n" \
               f"   Довжина = {self.product_dimensions_length} мм\n" \
               f"   Ширина = {self.product_dimensions_width} мм\n" \
               f"   Ціна: {self.product_price} грн.\n" \
               f"   В наявності є {self.product_quantity} шт."


class Buyer:
    def __init__(self, buyer_surname: str, buyer_name: str, buyer_patronymic: str, buyer_phone: str):
        self.buyer_surname = buyer_surname
        self.buyer_name = buyer_name
        self.buyer_patronymic = buyer_patronymic
        self.buyer_phone = buyer_phone

    def __str__(self):
        return f"{self.buyer_surname} {self.buyer_name} {self.buyer_patronymic} {self.buyer_phone}"


class Order:

    def __init__(self, buyer: Buyer):
        self.buyer = buyer
        self.__product_selected_by_buyer = []
        self.__quantity_of_goods = []

    def add_goods(self, goods: Product, quantity: float):
        self.__product_selected_by_buyer.append(goods)
        self.__quantity_of_goods.append(quantity)

    def check_generation(self):
        return "\n".join(f"     {index + 1}) {goods.product_name} - "
                         f"{goods.product_price} грн. "
                         f"Додано до кошика: {self.__quantity_of_goods[index]} шт. "
                         f"на загальну суму: {goods.product_price * self.__quantity_of_goods[index]} грн."
                         for index, goods in enumerate(self.__product_selected_by_buyer))

    def total_summa_to_paid(self):
        return sum(goods.product_price * self.__quantity_of_goods[index] for index, goods in
                   enumerate(self.__product_selected_by_buyer))

    def __str__(self):
        return f"Візьміть Ваш чек:\n\n" \
               f"   Замовник: {self.buyer.buyer_name} {self.buyer.buyer_patronymic} {self.buyer.buyer_surname}\n" \
               f"   Телефон замовника: {self.buyer.buyer_phone}\n" \
               f"   {'-' * 42}\n" \
               f"   Замовлені товари:\n" \
               f"{self.check_generation()}\n\n" \
               f"   {'-' * 42}\n" \
               f"   ЗАГАЛЬНА СУМА ДО СПЛАТИ: {self.total_summa_to_paid()} грн."


def buyer_registration():
    buyer = Buyer("Петров", "Петро", "Петрович", "4545454545454")
    # buyer = Buyer(
    #     input("Введіть своє прізвище: "),
    #     input("Введіть своє ім'я: "),
    #     input("Як Вас по батькові: "),
    #     input("Ваш номер телефону: ")
    # )

    print("-" * 42, f"\nПриємно познайомитись {buyer.buyer_name}! У нас є такі товари:")

    return buyer


def goods_available():
    goods_list = []
    how_much_goods_available_in_stock = 4

    product_1 = Product("Комп'ютер", "Цей комп'ютер дуже хороший!", 500, 700, 4_320, 12)
    # product_1 = Product("Комп'ютер", "Цей комп'ютер дуже хороший!", 500, 700, -4_320, 12)
    # product_1 = Product("Комп'ютер", "Цей комп'ютер дуже хороший!", 500, 700, 0, 12)
    # product_1 = Product("Комп'ютер", "Цей комп'ютер дуже хороший!", 500, 700, "4_320", 12)
    # product_1 = Product("Комп'ютер", "Цей комп'ютер дуже хороший!", 500, 700, 4_32o, 12)
    product_2 = Product("Стіл", "Цей стіл дуже зручний і красивий!", 1_200, 600, 1_230, 4)
    # product_2 = Product("Стіл", "Цей стіл дуже зручний і красивий!", 1_200, 600, 1_230, "4")
    product_3 = Product("Годинник", "Годинник як годинник", 30, 30, 230, 60)
    product_4 = Product("Клавіатура", "Ця клавіатура є клавіатурою з великою кількістю клавіш", 700, 450, 584, 43)

    for i in range(1, how_much_goods_available_in_stock + 1):
        goods_list.append(locals().get(f"product_{i}"))

    goods_list.append(how_much_goods_available_in_stock)

    return goods_list


def show_goods(in_stock):
    for i in range(len(in_stock) - 1):
        print(f"{i + 1})", in_stock[i])

        if i < len(in_stock) - 2:
            print("-" * 14)


def buyer_choice(goods: Product, buyer):
    order = Order(buyer)

    print("-" * 42)

    while True:
        buyer_chose = int(input("Оберіть товар який Вас зацікавив натиснувши цифру біля наіменування товару: "))
        if buyer_chose > len(goods) - 1:
            raise SelectedItemWhichIsNotAvailable(buyer_chose, len(goods) - 1)

        buyer_chose_quantity = int(input("Яка кількість Вас цікавить? "))
        if buyer_chose_quantity > goods[buyer_chose - 1].product_quantity:
            raise QuantityOfProductIsNotAvailableInStock(buyer_chose_quantity, goods[buyer_chose - 1].product_quantity)

        print("-" * 42)
        print(f"Ви обрали: {goods[buyer_chose - 1].product_name}. Вам потрібно: {buyer_chose_quantity} шт.")

        order.add_goods(goods[buyer_chose - 1], buyer_chose_quantity)
        print("-" * 42)

        additional_buyer_chose = int(input('Бажаєте ще щось додати до кошика ("Так" - 1, "Ні" - 0)? '))
        if additional_buyer_chose > 1 or additional_buyer_chose < 0:
            raise WrongChoiceAdditionalAction(additional_buyer_chose)

        print("-" * 42)

        if not additional_buyer_chose:
            print("Дякуємо за замовлення!", end=" ")
            break

    return order


print("-" * 42)
buyer = buyer_registration()
goods_available_in_stock = goods_available()
show_goods(goods_available_in_stock)
order = buyer_choice(goods_available_in_stock, buyer)

print(order)

# -------------------------------------------

"""
2. Модифікуйте Друге домашнє завдання так, щоб при спробі додавання до групи більше 10-ти студентів, викликалася
    виняткова ситуація (тип виняткової ситуації треба самостійно реалізувати).

    Подію додавання нового студента до групи необхідно фіксувати у лог-файлі.
"""
import logging

logging.basicConfig(
    handlers=[logging.FileHandler(
        filename="add_students.log", encoding='utf-8', mode='w')],
    format="%(asctime)s - %(levelname)s: %(message)s",
    datefmt='%d.%m.%Y о %H:%M:%S',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


class OverMaxStudentError(Exception):
    """ Exception виникає тоді, коли до групи намагаються додати більше студентів ніж зарезервовано місць """

    def __init__(self, groupe_name, max_student):
        self.groupe_name = groupe_name
        self.max_student = max_student

    def __str__(self):
        return f'Не має можливості додати до групи. В групі "{self.groupe_name}" всього {self.max_student} місць'


class CannotBeLessThanOrEqualZeroError(Exception):
    """ Exception виникає тоді, коли користувач ввів номер кандидата або групи який менше або дорівнює нулю """

    def __init__(self, chose_candidates_or_groupe: int, what_is_chosen: str):
        self.chose_candidates_or_groupe = chose_candidates_or_groupe
        self.what_is_chosen = what_is_chosen
        self.candidate = "кандидата"
        self.groupe = "групу"

    def __str__(self):
        return f'Обрано {self.candidate if self.what_is_chosen != "Groupe" else self.groupe} ' \
               f'під номером: {self.chose_candidates_or_groupe}. Номер не може бути менше або дорівнювати нулю!'


class SelectedNotInListError(Exception):
    """ Exception виникає тоді, коли користувач ввів номер кандидата або групи якого немає в списку """

    def __init__(self, chose_candidates_or_groupe: int, length_candidates_or_groupe_list: int, what_is_chosen: str):
        self.chose_candidates_or_groupe = chose_candidates_or_groupe
        self.length_candidates_or_groupe_list = length_candidates_or_groupe_list
        self.what_is_chosen = what_is_chosen
        self.candidate1 = "кандидата"
        self.candidate2 = "кандидатів"
        self.groupe1 = "групу"
        self.groupe2 = "груп"

    def __str__(self):
        return f'Обрано {self.candidate1 if self.what_is_chosen != "Groupe" else self.groupe1} ' \
               f'під номером: {self.chose_candidates_or_groupe}. Такого номеру не має в списку! ' \
               f'Всього {self.candidate2 if self.what_is_chosen != "Groupe" else self.groupe2}: ' \
               f'{self.length_candidates_or_groupe_list}'


class GroupFullError(Exception):
    """ Exception виникає тоді, коли користувач додає студента в групу яка вже набрана """

    def __init__(self, course_groups_full):
        self.course_groups_full = course_groups_full

    def __str__(self):
        return f'Група: "{self.course_groups_full}" вже заповнена'


class WrongChoiceAdditionalActionError(Exception):
    """ Exception виникає тоді, коли користувач ввів не вірний номер додаткової дії """

    def __init__(self, additional_chose):
        self.additional_chose = additional_chose

    def __str__(self):
        return f'Введено: "{self.additional_chose}". Потрібно або "1" або "0"'


class Human:
    def __init__(self,
                 person_surname: str,
                 person_name: str,
                 person_patronymic: str,
                 person_gender: str,
                 person_phone: str
                 ):
        self.person_surname = person_surname
        self.person_name = person_name
        self.person_patronymic = person_patronymic
        self.person_gender = person_gender
        self.person_phone = person_phone

    def __str__(self):
        return f"{self.person_surname} " \
               f"{self.person_name} " \
               f"{self.person_patronymic}. " \
               f"Стать: {self.person_gender}. " \
               f"Телефон: {self.person_phone}"


class Student(Human):

    def __init__(self, person_surname, person_name, person_patronymic, person_gender, person_phone, person_age):
        super().__init__(person_surname, person_name, person_patronymic, person_gender, person_phone)
        self.person_age = person_age

    def __str__(self):
        return f"{super().__str__()}. {self.person_age} років"


class Groupe:

    def __init__(self, groupe_name: str, max_students: int = 5):
        self.groupe_name = groupe_name
        self.max_students = max_students
        self.__students_list = []

    def add_students(self, candidates, groupe_name):
        self.__students_list.append(f"{candidates.person_surname} "
                                    f"{candidates.person_name} "
                                    f"{candidates.person_patronymic} - "
                                    f"{candidates.person_age} років. "
                                    f"Телефон: {candidates.person_phone}. "
                                    f"Група \"{groupe_name}\"")

    def search_students(self, person_surname):
        return [student for student in self.__students_list if person_surname in student]

    def remove_students(self, candidates):
        if candidates + 1 > len(self.__students_list):
            raise SelectedNotInListError(candidates + 1, len(self.__students_list), "Candidate")

        studet_to_del = str(self.__students_list[candidates]).split(" ")

        self.__students_list.pop(candidates)

        logger.info(
            f'З групи {studet_to_del[-1]} видалено: {" ".join(studet_to_del[:3])}. {" ".join(studet_to_del[4:8])} '
        )

    def __str__(self):
        return "\n".join(f"{students}" for students in self.__students_list) or self.groupe_name


def open_groups():
    groups_list = []
    how_many_groups_create = 5

    group_1 = Groupe("Python", 2)
    group_2 = Groupe("Java", 2)
    group_3 = Groupe("FrontEnd", 3)
    group_4 = Groupe("English", 2)
    group_5 = Groupe("DevOps", 2)

    for groups_number in range(1, how_many_groups_create + 1):
        groups_list.append(locals().get(f"group_{groups_number}"))

    return groups_list


def show_groups(grops):
    print("Наявні групи:")
    for number_in_list, groupe_name in enumerate(grops):
        if grops[number_in_list].max_students > 0:
            print(f"    {number_in_list + 1}) {groupe_name}. Вільних місць: {grops[number_in_list].max_students}")
        else:
            print(f"    {number_in_list + 1}) {groupe_name}.\033[31m Вільних місць немає \033[0m")

    print("-" * 42)


def person_registration():
    student_list = []
    how_many_student_register = 6

    student_1 = Student("Петров", "Петро", "Петрович", "чоловіча", "111-1111111", 25)
    student_2 = Student("Сідоров", "Сідор", "Сідорович", "чоловіча", "222-2222222", 19)
    student_3 = Student("Марініна", "Марія", "Петрівна", "жіноча", "333-3333333", 36)
    student_4 = Student("Іванова", "Іванна", "Іванівна", "жіноча", "444-4444444", 27)
    student_5 = Student("Петров", "Петро", "Петрович", "чоловіча", "555-5555555", 37)
    student_6 = Student("Мусієнко", "Василь", "Андрійович", "чоловіча", "777-7777777", 20)

    for student_number in range(1, how_many_student_register + 1):
        student_list.append(locals().get(f"student_{student_number}"))

    return student_list


def show_person(candidates, action_choice):
    if action_choice == 1:
        if candidates:
            students_list = str(candidates).split("\n")
        else:
            print("Список студентів порожній")

        for index, students in enumerate(students_list):
            print(f"    {index + 1}) {students}")

    else:
        for position_in_list, candidate in enumerate(candidates):
            print(f"    {position_in_list + 1}) {candidate}")


def add_candidate_to_grope(candidates, course_groups):
    groups = Groupe(course_groups)

    while True:
        print("Список кандидатів:")
        show_person(candidates, 0)
        print("-" * 42)

        chose_candidates = int(input("Оберіть кандидата за його номером: "))
        if chose_candidates <= 0:
            raise CannotBeLessThanOrEqualZeroError(chose_candidates, "Candidate")
        elif chose_candidates > len(candidates):
            raise SelectedNotInListError(chose_candidates, len(candidates), "Candidate")

        temp_msg = f"{candidates[chose_candidates - 1].person_name} " \
                   f"{candidates[chose_candidates - 1].person_surname}. " \
                   f"{candidates[chose_candidates - 1].person_age} років. " \
                   f"Телефон: {candidates[chose_candidates - 1].person_phone}"

        print("-" * 42)
        print("Ви обрали:", temp_msg)
        print("-" * 42)

        show_groups(course_groups)

        chose_course_groups = int(input("Додайте кандидата до групи за її номером: "))

        for i in range(len(course_groups)):
            if str(course_groups[i]) == str(course_groups[chose_course_groups - 1]):
                course_groups[i].max_students -= 1
            if course_groups[i].max_students < 0:
                raise GroupFullError(str(course_groups[chose_course_groups - 1]))

        if chose_course_groups <= 0:
            raise CannotBeLessThanOrEqualZeroError(chose_course_groups, "Groupe")
        elif chose_course_groups > len(course_groups):
            raise SelectedNotInListError(chose_course_groups, len(course_groups), "Groupe")

        print("-" * 42)
        print(f"Тепер, {temp_msg} зараховано до групи \"{course_groups[chose_course_groups - 1].groupe_name}\"")
        print("-" * 42)

        logger.info(f"{temp_msg} зараховано до групи \"{course_groups[chose_course_groups - 1].groupe_name}\"")

        groups.add_students(candidates[chose_candidates - 1], course_groups[chose_course_groups - 1])

        additional_choice = int(input('Бажаєте ще когось дадати до групи ("Так" - 1, "Ні" - 0)? '))
        if additional_choice > 1 or additional_choice < 0:
            raise WrongChoiceAdditionalActionError(additional_choice)
        print("-" * 42)

        if not additional_choice:
            break

    return groups


def actions_with_students(on_course):
    while True:
        print("Що бажаєте зробити? ")
        choose_an_action = int(
            input("     1) Подивитись список студентів\n"
                  "     2) Видалити студента\n"
                  "     3) Знайти студента за прізвищем\n"
                  "     4) Вихід\n"
                  "Введіть номер обраного дії: "))

        print("-" * 42)

        if choose_an_action == 1:
            print("Список студентів:")
            show_person(on_course, 1)
            print("-" * 42)

        elif choose_an_action == 2:
            print("Кого потрібно видалити?:")
            show_person(on_course, 1)
            print("-" * 42)

            chose_student_to_del = int(input("Оберіть студента за його номером: "))

            on_course.remove_students(chose_student_to_del - 1)
            print("-" * 42)

            print("Студенти які продовжують навчання:")
            show_person(on_course, 1)
            print("-" * 42)

        elif choose_an_action == 3:
            finde_student = "Петров"
            # finde_student = "Сідоров"
            # finde_student = "Марініна"
            # finde_student = "Петрова" # немає в жодному із списків

            print("Кого потрібно знайти?", finde_student)
            print("-" * 42)

            students_finde_list = on_course.search_students(finde_student)

            if not students_finde_list:
                print("Такого студента немає на жодному курсі...")
                print("-" * 42)
            else:
                print("Знайдено!")
                for index, students in enumerate(students_finde_list):
                    print(f"    {index + 1}) {''.join(students)}")
                print("-" * 42)

        else:
            break


print("-" * 42)
candidates = person_registration()
course_groups = open_groups()
students_on_course = add_candidate_to_grope(candidates, course_groups)
actions_with_students(students_on_course)
