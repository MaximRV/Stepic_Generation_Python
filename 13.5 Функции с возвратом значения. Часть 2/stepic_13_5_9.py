# объявление функции
def convert_to_python_case(text):
    res = ""
    for i in text:
        if (i.isupper()):
            res += "*" + i
        else:
            res += i
    x = res.split("*")
    x.remove('')
    x = '_'.join(x)
    return x.lower()

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
