# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
#   - видалити усі дублікати
#   - замінити кожне 4-те значення на 'X'
# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
# 3) вывести табличку множення за допомогою цикла while
# 4) переробити це завдання під меню

listok = [22, 3,5,2,8,2,-23, 8,23,5]
def min_list(l):
    print(min(l))
def delete_duplicates(l):
    mylist=listok.copy()
    print(list(set(mylist)))
def fourth_to_x(l):
    copy = l.copy()
    print(['X' if not (i + 1) % 4 else item for i, item in enumerate(copy)])
def square_with_stars(n):
    for i in range(n):
        if i==0 or i==n-1:
            print('*'*n)
        else:
            print('*'+' '*(n-2)+'*')
def multi_table():
    size = 9
    i = 1
    while i <= size:
        j = 1
        while j <= size:
            res = i*j
            print(f'{res:4}', end='')
            j += 1
        print()
        i += 1

while True:
    print('1) Знайти мінімальне число')
    print('2) Видалити усі дублікати')
    print('3) Замінити кожне 4-те значення на "X"')
    print('4) Вивести квадрат')
    print('5) Вивести табличку множення')
    print('9) Вихід')

    choice = input('Зробіть свій вибір: ')

    if choice == '1':
        print(min_list(listok))
    elif choice == '2':
        delete_duplicates()
    elif choice == '3':
        fourth_to_x()
    elif choice == '4':
        square_with_stars(7)
    elif choice == '5':
        multi_table()
    elif choice == '9':
        break