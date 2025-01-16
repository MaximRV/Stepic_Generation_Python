n = input()
count = 0
count_2 = 0
a = '*'
b = '+'
for c in n:
    if c == a:
        count += 1
    if c == b:
        count_2 += 1
print('Символ + встречается', count_2, 'раз')
print('Символ * встречается', count, 'раз') 
