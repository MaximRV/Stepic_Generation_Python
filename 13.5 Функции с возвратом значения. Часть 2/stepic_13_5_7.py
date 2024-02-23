# объявление функции
def is_valid_password(password):
    p = psw[0]
    s = int(psw[1])
    w = int(psw[2])

    Flag_1 = False
    Flag_2 = True

    if p == p[::-1] and w % 2 == 0:
        Flag_1 = True

    for i in range(2,s):
        if s % i == 0:
            Flag_2 = False
            break

    if Flag_1 and Flag_2 and len(psw) == 3:
        return True
    else:
        return False

# считываем данные
psw = input().split(':')

# вызываем функцию
print(is_valid_password(psw))
