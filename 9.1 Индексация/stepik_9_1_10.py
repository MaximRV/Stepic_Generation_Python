a = 'ауоыиэяюёе'
b = 'бвгджзйклмнпрстфхцчшщ'
c = 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
d = 'АУОЫИЭЯЮЁЕ'
count_glass = 0
count_soglass = 0
n = input()
for i in n:
    if i in a or i in d:
        count_glass += 1
    elif i in b or i in c: 
        count_soglass += 1
    
print('Количество гласных букв равно', count_glass)
print('Количество согласных букв равно', count_soglass)
