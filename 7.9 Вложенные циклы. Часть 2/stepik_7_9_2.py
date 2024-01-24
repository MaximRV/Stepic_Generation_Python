n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print(j+1, end='')
    for f in range(i - 1, 0, -1):
        print(f, end='')
    print()
