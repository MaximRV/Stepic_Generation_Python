# объявление функции
def is_palindrome(text):
    li = [i for i in text if i.isalpha()]
    if ''.join(li).lower() == ''.join(li[::-1]).lower():
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
