# объявление функции
def get_factors(num):
    li = []
    for i in range(1, num+1):
        if num % i == 0:
            li.append(i)
    return li

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))
