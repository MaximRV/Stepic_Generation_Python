n = input()
l = ''
for i in range(len(n)):
    if i % 3 != 0:
        l += n[i]       
print(l)
