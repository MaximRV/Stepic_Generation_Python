s = input().lower().split()

cnt1 = s.count('a')
cnt2 = s.count('an')
cnt3 = s.count('the')

print('Общее количество артиклей:', cnt1+cnt2+cnt3)
