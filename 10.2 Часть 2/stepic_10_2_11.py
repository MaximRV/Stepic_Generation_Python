s = input()
start = s.find('h')
end = s.rfind('h')
s1 = s[start:end+1]
print(s[:start] + s1[::-1] + s[end+1:])
