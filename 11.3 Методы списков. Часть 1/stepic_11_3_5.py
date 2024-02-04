n = int(input())
spisok = []
for i in range(1,n+1):
    if n % i == 0:
        spisok.append(i)
print(spisok)
