n = input()
count = 0
for i in n:
    if i == i.lower() and i not in '0123456789':
        count += 1
print(count)
