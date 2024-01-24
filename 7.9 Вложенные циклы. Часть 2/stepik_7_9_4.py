n = int(input())
count = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        x = i % j
        if x == 0:
            count += 1
    print(i, '+' * count, sep='')
    count = 0
