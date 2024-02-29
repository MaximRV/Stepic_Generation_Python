# объявление функции
def get_month(language, number):
    li_month_ru = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь','ноябрь', 'декабрь']
    li_month_en = ['', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                   'november', 'december']
    if language == 'ru':
        return li_month_ru[number]
    elif language == 'en':
        return li_month_en[number]

# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))
