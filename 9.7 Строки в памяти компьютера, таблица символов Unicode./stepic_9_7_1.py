alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

input_letter = input().strip()

index = alphabet.find(input_letter)

if index != -1 and index < len(alphabet) - 1:
    print(alphabet[index + 1])
else:
    print("Дальше букв нет")
