# объявление функции
def draw_triangle(fill, base):
    for i in range(1, base + 1):
        if i <= (base // 2) + 1:
            print(fill * i)
        else:
            print(fill * (base - i + 1))

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
