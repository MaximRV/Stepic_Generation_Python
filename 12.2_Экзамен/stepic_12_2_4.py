s = input().split('-')

if len(s) != 4 and len(s) != 3:
    print('NO')
    
elif len(s[-1]) != 4 or len(s[-2]) != 3 or len(s[-3]) != 3 :
    print('NO')
    
elif len(s) == 4 and len(s[0]) != 1:
    print('NO')
    
elif len(s) == 4 and int(s[0][0]) != 7:
    print('NO')
    
elif not ''.join(s).isdigit():
    print('NO')
    
else:
    print('YES')
