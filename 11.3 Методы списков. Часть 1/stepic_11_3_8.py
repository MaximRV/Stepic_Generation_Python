n = int(input())
seq = []
for _ in range(n):
    seq.append(input())
k = int(input())
for i in range(n):
    if len(seq[i]) < k:
           continue
    else:
        print(seq[i][k-1], end = '')
