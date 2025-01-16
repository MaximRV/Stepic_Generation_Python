# объявление функции
def is_correct_bracket(text):
    if txt[0] == ')':
        return False
    elif txt[len(txt)-1] == '(':
        return False
    count = 0
    for i in txt:
        if count < 0:
            break
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
    if count == 0:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
