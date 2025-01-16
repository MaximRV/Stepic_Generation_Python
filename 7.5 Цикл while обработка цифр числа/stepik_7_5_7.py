n = int(input())
while n % 10 <= n // 10 % 10:
    n //= 10
print('YES' if n < 10 else 'NO')
