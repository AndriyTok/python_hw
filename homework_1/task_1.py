# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
# #################################################################################

st = 'as 23 fdfdg544'
print(*[int(i) for i in st if i.isdigit()], sep=', ')
