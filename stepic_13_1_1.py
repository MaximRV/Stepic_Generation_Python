# объявление функции
def draw_box():
    n = 14
    a = 8
    for i in range(n):
        if i == 0:
            print('*', '*', sep = '*'*a)
        elif i == n - 1:
            print('*', '*', sep = '*'*a)
        else:
            print('*', '*', sep = ' '*a)
            
draw_box()  # вызов функции
