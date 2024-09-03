# - створити функцію яка виводить ліст

li = [1,2,1,5,6,2,1]
def show_list(l):
    print(*[i for i in l], sep=', ')
show_list(li)

# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def show_max(a,b,c):
    max_num = max(a, b, c)
    print(max_num)
    return max_num

show_max(120,23,0)

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def max_min(*args):
    print(max(args))
    return min(args)

max_min(1,2,3,4)

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def sum_of_list(l):
    print(sum(l))
sum_of_list(li)
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
def avg_of_list(l):
    return sum(l) / len(l)
