n = int(input())
x = n % 10
count = 0
count_d = 0
while n != 0:
    m = n % 10
    count += 1
    if m == x:
        count_d += 1
    n = n // 10
if count == count_d:
    print('YES')
else:
    print('NO')
