n = int(input())
max_number = 0
min_number = n
while n != 0:
    last_digit = n % 10
    if last_digit > max_number:
        max_number = last_digit
    if last_digit < min_number:
        min_number = last_digit
    n = n // 10
print('Максимальная цифра равна', max_number)
print('Минимальная цифра равна', min_number)
