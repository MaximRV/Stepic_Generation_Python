n = int(input())
rez_numbers = []
numbers = []
for _ in range(n):
    a = int(input())
    numbers.append(a)
    rez_numbers.append(a**2 + 2 * a + 1)

print(*numbers, sep='\n')
print()
print(*rez_numbers, sep='\n')
