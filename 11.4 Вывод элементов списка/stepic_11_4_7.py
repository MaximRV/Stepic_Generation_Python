n = int(input())
minus = []
nol = []
plus = []
for _ in range(n):
    a = int(input())
    if a < 0: 
        minus.append(a)
    elif a == 0:
        nol.append(a)
    elif a > 0:
        plus.append(a)
print(*minus, *nol, *plus, sep = '\n')
