# объявление функции
def is_prime(num):
    if num == 1:
        return False
    else:
        Flag = True
        for i in range(2, num):
            if num % i == 0 :
                Flag = False
    return Flag

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))
