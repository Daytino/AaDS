import operator, pprint

N = 100
M = 1
K = 7
res = []

items = [[4, 12], [2, 1], [1, 1], [2, 2], [10, 4]]
items = [[5, 4], [4, 3], [3, 2], [2, 1]]
# items = [[1, 2], [2, 3], [5, 4], [6, 5]]
items = [[50, 3], [40, 2], [70, 4], [80, 5], [10, 1]]
names_dct = {}

# Список в словарь ----
dct = {}
for i, v in enumerate(items):
    dct[i + 1] = v
print(dct)
# Создание таблицы ----
a = [[0] * (K + 1) for i in range(len(items) + 1)]
for i in range(1, len(items) + 1):
    for j in range(1, K + 1):
        if dct[i][1] > j: a[i][j] = a[i - 1][j]
        else: a[i][j] = max(a[i - 1][j], a[i - 1][j - dct[i][1]] + dct[i][0])

# Определение собранных предметов ----
i, j, = len(items), K
while i > 0:
    if a[i - 1][j] != a[i][j]:
        res.append(i)
        j -= dct[i][1]
    i -= 1
print(res[::-1])

pprint.pprint(a)
