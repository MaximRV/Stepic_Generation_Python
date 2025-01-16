s = input().split()
line = '+'.join(s)
numbers = [int(i) for i in s]
print(line, '=', sum(numbers), sep='')
