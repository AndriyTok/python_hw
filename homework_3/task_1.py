# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __perimeter__(self):
        return 2*(self.a+self.b)

    def __square__(self):
        return self.a * self.b

    def __add__(self, other):
        return self.__square__() + other.__square__()

    def __sub__(self, other):
        return self.__square__() - other.__square__()

    def __test_eq__(self, other):
        if self.__square__() == other.__square__():
            return True
        else:
            return False
    def __compare__(self, other):
        if self.__square__() > other.__square__():
            print(f"Rectangle 1's square is bigger than rectangle 2's")
        else:
            print(f"Rectangle 2's square is bigger than rectangle 1")

rectangle_1 = Rectangle(2, 4)
rectangle_2 = Rectangle(5, 6)

print('Периметри:', ', '.join(str(rectangle_1.__perimeter__() and rectangle_2.__perimeter__())))
print('Площі:', ', '.join(str(rectangle_1.__square__() and rectangle_2.__square__())))
Rectangle.__compare__(rectangle_1, rectangle_2)
print(Rectangle.__test_eq__(rectangle_1, rectangle_2))

