# объявление функции
def compute_binom(n, k):
    n_f = factorial(n)
    k_f = factorial(k)
    n_k_f = factorial(n-k)
    return int(n_f / (k_f*n_k_f))

def factorial(n):
    count = 1
    for i in range(1, n+1):
        count = count * i
    return count

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))
