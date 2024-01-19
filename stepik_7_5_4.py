n = int(input())
m = n
total_all = 0
count_all = 0
total_pr_all = 1

while n != 0:
    x = n % 10
    total_all += x
    count_all += 1
    total_pr_all *= x
    n = n // 10
sr_znach = total_all / count_all
last_digit = m % 10
first_digit = m // (10**(count_all-1))
sum_first_last_digits = last_digit + first_digit

print(total_all)
print(count_all)
print(total_pr_all)
print(sr_znach)
print(first_digit)
print(sum_first_last_digits)
