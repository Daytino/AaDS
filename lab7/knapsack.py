N = 5 # Максимальное число экспонатов
M = 2 # Количество заходов
K = 7 # Вместительность рюкзака

# [цена, вес]
items = [[4, 12], [2, 1], [1, 1], [2, 2], [10, 4]]

res = []
dct = {}
for i, v in enumerate(items):
    dct[i + 1] = v

dct = dict(sorted(dct.items(), key=lambda item: item[1][0] / item[1][1], reverse=True))

summa = summa_final = 0

for m in range(M):
    weight_available = K
    sack = []
    summa = 0
    for i in dct.keys():
        if dct[i][1] > weight_available or N == 0:
            break
        else:
            weight_available -= dct[i][1]
            summa += dct[i][0]
            summa_final += dct[i][0]
            N -= 1
            sack.append(i)
    for i in sack:
        res.append(i)
        del dct[i]
    
    print("Номер захода:", m + 1)
    print("Унесённые предметы:", sack)
    print(f"Заполненность рюкзака: {K - weight_available} / {K}")
    print("Сумма захода:", summa)
    print("---------------")
    if N == 0 or len(dct) == 0: break

print("Унесённые предметы:", *list(sorted(res)))
print("Итоговая сумма:", summa_final)