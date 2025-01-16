# объявление функции
def draw_triangle():
    count = 7
    for i in range(1,16,2):
        print(' ' * count + "*" * i)
        count -= 1

# основная программа
draw_triangle()  # вызов функции
