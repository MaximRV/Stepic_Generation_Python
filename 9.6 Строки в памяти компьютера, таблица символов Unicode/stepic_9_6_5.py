day = int(input())
current_weight = float(input())

target_weight = 99.8 - (day - 1) * 0.2


if current_weight <= target_weight:
    print("Все идет по плану")
else:
    print("Что-то пошло не так")

print(f"#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {current_weight} кг, ЦЕЛЬ по ВЕСУ = {round(target_weight,1)} кг")
