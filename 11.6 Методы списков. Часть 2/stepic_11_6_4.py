n = int(input()[1:])
for _ in range(n):
    s = input()
    a = s.find('#')
    if a >= 0:
        s = s[:a]
    s = s.rstrip()
    print(s)
