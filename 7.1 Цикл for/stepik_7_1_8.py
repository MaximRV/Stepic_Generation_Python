m = int(input())
p = int(input())
n = int(input())
for i in range(n):
    print(i + 1, float(m * ((1 + p / 100) ** (i))))
