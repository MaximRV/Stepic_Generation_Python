n = int(input())
li = []

for _ in range(n):
    a = input()
    li.append(a)
    
b = input()
for i in li:
    if b.lower() in i.lower():
        print(i)
