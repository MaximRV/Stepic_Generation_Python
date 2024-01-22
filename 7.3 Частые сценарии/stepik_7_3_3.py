import math
n = int(input())
log = math.log(n)
total = 1
for i in range(2, n + 1):
    total += (1 / i)
print(total - log)  
