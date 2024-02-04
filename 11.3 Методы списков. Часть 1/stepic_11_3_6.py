n = int(input())
l = []
s = []
for _ in range(n):
    l.append(int(input()))
             
for i in range(n-1):
    s.append(l[i]+l[i+1])
print(s)
