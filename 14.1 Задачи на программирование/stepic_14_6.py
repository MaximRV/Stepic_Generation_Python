# объявление функции
def is_magic(date):
    return int(date[0]) * int(date[1]) == int(date[2]) % 100

# считываем данные
date = input().split('.')

# вызываем функцию
print(is_magic(date))
