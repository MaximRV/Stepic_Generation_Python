n = int(input())
z = m = 0
for _ in range(n):
    num = int(input())
    if num > m:
        m, z = num, m
    else:
        if num >z:
            z = num
print(m)
print(z)
