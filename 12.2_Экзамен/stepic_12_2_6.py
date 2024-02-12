s = input().split()
li = [ i[1:] + i[0] + 'ки'  for i in s]
print(*li)
