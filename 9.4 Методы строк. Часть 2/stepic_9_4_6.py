s = input()
count = 0
n = s
for i in s:
    a = s.count(i)
    if a >= count:
        count = a
        n = i
print(n)
