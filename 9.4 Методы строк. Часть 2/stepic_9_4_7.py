s = input()
a = s.count('f')
if a == 1 :
    print(s.find('f'))
elif a >= 2:
    print(s.find('f'), s.rfind('f'))
else:
    print('NO')
