# порахувати кількість парних і непарних цифр числа,
#   наприклад: х = 225688 -> п = 5, н = 1;
#          х = 33294 -> п = 2, н = 3

x = int(input('Enter your number:'))
#парні
even_count:int = 0
#непарні
odd_count:int = 0

for digit in str(x):
    num = int(digit)
    if num%2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Even_count: {even_count}, Odd_count: {odd_count}")
