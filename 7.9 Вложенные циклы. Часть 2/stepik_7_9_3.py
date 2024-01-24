a = int(input())
b = int(input())
total = 0
total_2 = 0
c = 0
flag = False
for i in range(a, b + 1):
    for j in range(1, i + 1):
        x = i % j
        if x == 0:
            total += j
    if total >= total_2:
        total_2 = total
        c = i
    total = 0
print(c, total_2)
