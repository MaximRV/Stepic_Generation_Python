m = int(input())
n = int(input())

if m % 2 == 0 and m - 1 == n: print(n)
elif m % 2 != 0 and m - 1 == n: print(m)
elif m % 2 == 0:
    for i in range(m - 1, n, -2):
        print(i)
else:
    for i in range(m, n, -2):
        print(i)
