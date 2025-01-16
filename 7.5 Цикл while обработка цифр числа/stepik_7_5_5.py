n = int(input())
count = 0
z = n
while n != 0:
    count += 1
    n = n // 10
m = (z // ( 10 ** (count-2))) % 10
print(m)
