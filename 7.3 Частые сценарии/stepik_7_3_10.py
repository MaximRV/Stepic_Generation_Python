counter = 0
numbers = 10
for _ in range(10):
    num = int(input())
    if num%2 == 0:
        counter += 1
if counter == numbers:
    print('YES')
else:
    print('NO') 
