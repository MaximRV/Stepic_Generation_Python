L = input().split()
M = input().split()
numbers = [int(L[i]) + int(M[i]) for i in range(len(L))]
print(*numbers)
