s = [int(el)**2 for el in input().split() if int(el) % 2 == 0 and int(el)**2 % 10 != 4]
print(*s)
