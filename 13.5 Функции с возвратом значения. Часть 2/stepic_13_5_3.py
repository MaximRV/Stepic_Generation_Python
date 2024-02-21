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

def get_next_prime(num):
    x = num
    z = False
    while z == False:
        y = x + 1
        z = is_prime(y)
        x = x +1
    return x

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
