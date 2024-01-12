n = int(input())
total_p = 0
total_m = 0
for i in range(1,(abs(((-1) ** (n + 1)) * n)) + 1):
    if i %2 == 0:
        total_m += - i
    else: 
        total_p += i
print(total_p + total_m)
    
