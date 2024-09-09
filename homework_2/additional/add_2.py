# вивести послідовність Фібоначі, кількість вказана в знінній,
#   наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
#   (число з послідовності - це сума попередніх двох чисел)

x = int(input('Enter a number for fibonacci: '))

fibonacci:[int] = [1,1]

if x > 2:
    for i in range(2,x):
        next_num=fibonacci[i-1]+fibonacci[i-2]
        fibonacci.append(next_num)
elif x == 1:
    fibonacci = [1]
else:
    fibonacci = [1,1]

print(' '.join(map(str,fibonacci)))

