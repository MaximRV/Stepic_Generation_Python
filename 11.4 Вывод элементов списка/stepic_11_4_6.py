n = int(input())
stroki = []
zapros = []

for _ in range(n):
    a = input()
    stroki.append(a)
    
k = int(input())

for _ in range(k):
    b = input()
    zapros.append(b)
 
flag = True
for i in stroki:
    for j in zapros:
        if j.lower() not in i.lower():
            flag = False
    if flag:
        print(i)
    flag = True
