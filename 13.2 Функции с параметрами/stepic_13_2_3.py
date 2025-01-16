# объявление функции
def print_digit_sum(num):
    chisla = 0
    while num != 0:
        a = num % 10
        chisla += a
        num = num // 10
    print(chisla)

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
