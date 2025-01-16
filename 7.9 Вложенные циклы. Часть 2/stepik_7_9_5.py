n = int(input())
total = 0
count = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        count *= j
    total += count
    count = 1
print(total)
