def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2
    
    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if int(list1[p1]) <= int(list2[p2]):
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):   # прицепление остатка
        result += list1[p1:]
    else:                 # иначе прицепляем остаток другого списка
        result += list2[p2:]
    
    return result

n = int(input())
list = []
for i in range(n):
    a = input().split()
    list.append(a)

list2 = []    
for i in range(len(list)):
    a = quick_merge(list2, list[i])
    list2 = a
print(*list2)
