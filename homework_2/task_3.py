# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

#the function accepts a number(int) and returns a string:
def bits_sum(num:any)->str:
    #variable in which we transform our number from int to str
    st=str(num)
    #to detect how many bits we have
    length=len(st)-1
    #empty list for resulting string
    res=[]
    #loop for with variables i for iteration and ch for the symbol in st
    for i, ch in enumerate(st):
        if ch!='0':
            res.append(ch+'0'*(length-i))
    return ' + '.join(res)+ f' = {st}'

while True:
    number = input('Enter a number: ')
    if -9 <= int(number) <= 9:
        print('Enter a valid number')
        continue
    if number.lower() == 'q':
        break
    print(bits_sum(number))