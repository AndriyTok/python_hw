# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення
from abc import ABC

class Human(ABC):
    def __init__(self, name, age):
        self.name:str = name
        self.age:int = age

class Cinderella(Human):
    count = 0 # variable for counting

    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size:int = foot_size
        Cinderella.count += 1 #increasing count

    @classmethod
    def get_count(cls):
        return cls.count


class Prince(Human):
    def __init__(self, name, age, found_foot_size):
        super().__init__(name, age)
        self.found_foot_size:int = found_foot_size
    def __find__(self, cinderellas_list):
        for item in cinderellas_list:
            if item.foot_size == self.found_foot_size:
                print(f"{item.name} is a princess!")
                break


cinderellas:list[Cinderella] = [
    Cinderella('Alla', 18, 38),
    Cinderella('Nina', 19, 40),
    Cinderella('Rosa', 20, 35),
    Cinderella('Alisa', 30, 34),
]

prince = Prince('Alex', 35, 35)
prince.__find__(cinderellas)
print(Cinderella.count)