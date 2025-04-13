import re

def is_valid_car_number(car_number):
    # Определяем регулярное выражение для проверки
    pattern = r'^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}_(\d{2}|\d{3})$'
    return bool(re.match(pattern, car_number))

# Читаем входные данные
car_number = input().strip()

# Проверяем и выводим результат
if is_valid_car_number(car_number):
    print("YES")
else:
    print("NO")