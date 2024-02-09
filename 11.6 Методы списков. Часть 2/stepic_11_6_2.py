li = input().split()
for i in range(len(li)):
    li[i] = int(li[i])
minimum = min(li)
maximum = max(li)
min_index = li.index(minimum)
max_index = li.index(maximum)
li[min_index], li[max_index] = li[max_index], li[min_index]
print(*li)
