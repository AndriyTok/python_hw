# є функція:
# def pr():
#     return 'Hello_boss_!!!'
#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення
# функцию pr менять не можно
from decorator import decorator

def decor(func):
    def wrapper():
        result=func()
        return result.replace('_', ' ')
    return wrapper

@decor
def pr():
    return 'Hello_boss_!!!'

print(pr())

