s = input().split('.')
for i in s:
    i = int(i)
    flag = True
    if 0 <= i <= 255:
        flag = True
    else:
        flag = False
        break
if flag:
    print('ДА')
else:
    print('НЕТ')
