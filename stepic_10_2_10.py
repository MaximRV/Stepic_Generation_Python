s = input()
start = s.find('f') + 1
a = s.count('f')
if a == 1:
    print(-1)
elif a == 0:
    print(-2)
    
else:
    print(s.find('f', start))
