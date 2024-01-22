word = input()
count = 0
while word != 'стоп' and word != 'достаточно' and word != 'хватит':
    count += 1
    word = input()
print(count)
