n = int(input())
numbers = []
for _ in range(n):
    num = input()
    if num not in numbers:
        numbers.append(num)
print(*numbers, sep='\n')
