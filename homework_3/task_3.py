# ###############################################################################
#
# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
#
# Приклад:
#
# Main.add(Magazine('Magazine1'))
#     Main.add(Book('Book1'))
#     Main.add(Magazine('Magazine3'))
#     Main.add(Magazine('Magazine2'))
#     Main.add(Book('Book2'))
#
#     Main.show_all_magazines()
#     print('-' * 40)
#     Main.show_all_books()
#
#
# для перевірки ксассів використовуємо метод isinstance, приклад:
#
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False

from abc import ABC, abstractmethod
from sympy.codegen import Print


class Printable(ABC):
   @abstractmethod
   def __print__(self):
       print(str(self.__dict__))

class Book(Printable):
    def __init__(self, name, number_of_pages, title):
        self.name = name
        self.number_of_pages = number_of_pages
        self.title = title


    def __print__(self):
        print(str(self.__dict__))

class Magazine(Printable):
    def __init__(self, name, number_of_pages):
        self.name = name
        self.number_of_pages = number_of_pages


    def __print__(self):
        print(str(self.__dict__))

class Main:
    __printable_list:list[Printable] = []

    @classmethod
    def add(cls, item:Book|Magazine):
          if isinstance(item, (Book, Magazine)):
                cls.__printable_list.append(item)

    @classmethod
    def show_all_magazines(cls):
        for item in cls.__printable_list:
            if isinstance(item, Magazine):
                item.__print__()
            else:
                pass
    @classmethod
    def show_all_books(cls):
        for item in cls.__printable_list:
            if isinstance(item, Book):
                item.__print__()
            else:
                pass


Main.add(Magazine('magazine1', 10))
Main.add(Magazine('magazine4', 12))
Main.add(Book('book1', 300, 'Book1'))
Main.add(Book('book2', 500, 'Book2'))
Main.add(Book('book3', 1000, 'Book3'))
Main.add(Book('book4', 80, 'Book4'))
Main.add(Magazine('magazine3', 15))

Main.add(Magazine('magazine2', 2))
Main.add('ddddddddddddddd')

Main.show_all_magazines()
print('********************************************')
Main.show_all_books()