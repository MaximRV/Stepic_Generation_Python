n = int(input())
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)
for i in range(n):
    if numbers[i] != min(numbers) and numbers[i] != max(numbers) :      
        print(numbers[i], sep = '\n')
