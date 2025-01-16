s = input().split()
counter = 0
for j in range(len(s)):
    if s[j] in s[:j]:
        a = s[:j].count(s[j])
        b = s.count(s[j])
        if b > 1:
            counter += b-1-a    
    else:
        b = s.count(s[j])
        if b > 1:
            counter += b-1
print(counter)
