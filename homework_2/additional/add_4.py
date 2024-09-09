# Прога, що виводить кількість кожного символа з введеної str, наприклад:
# st = 'as 23 fdfdg544'  # введена строка
#
# 'a' -> 1  # вивело в консолі
# 's' -> 1
# ' ' -> 2
# '2' -> 1
# '3' -> 1
# 'f' -> 2
# 'd' -> 2
# 'g' -> 1
# '5' -> 1
# '4' -> 2

st:str = 'as 23 fdfdg544'

symbol_count = {}

for char in st:
    if char in symbol_count:
        symbol_count[char] += 1
    else:
        symbol_count[char] = 1