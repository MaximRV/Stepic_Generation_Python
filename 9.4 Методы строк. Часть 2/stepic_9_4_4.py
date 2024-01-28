s = input()
count = 0
for i in range(10):
    if s.count(str(i)) != 0:
        count += s.count(str(i))
print(count)
