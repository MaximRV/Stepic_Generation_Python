n = int(input())
a =''
while n != 0:
    x = n % 2
    a += str(x)
    n = n // 2
print(a[::-1])
