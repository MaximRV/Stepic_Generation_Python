n = input()
a = len(n)
b = n[:a//2]
c = n[a//2:]
if a % 2 != 0:
    b = n[:a//2+1]
    c = n[a//2+1:]
d = c + b
print(d)
