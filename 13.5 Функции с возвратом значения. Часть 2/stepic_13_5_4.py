# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return False
    elif not True in [ch.isdigit() for ch in password]:
        return False
    elif not True in [ch.isalpha() for ch in password]:
        return False
    elif password.islower():
        return False
    elif password.isupper():
        return False
    else:
        return True

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
