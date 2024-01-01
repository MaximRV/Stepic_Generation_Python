a = input()
Flag = False
for i in range(0, 10):
    if str(i) in a:
        Flag = True
if Flag == True:
    print('Цифра')
else:
    print('Цифр нет')
