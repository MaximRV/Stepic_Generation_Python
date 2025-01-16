n = int(input())
a = input()
for i in a:
    b = ord(i)
    if b - n < 97:
        c = 122 - n + (b - 96)
    else: 
        c = b - n
    d = chr(c)
    print(d, end = '')
