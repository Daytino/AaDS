f = open("26_17537.txt")
n, rows, seats = list(map(int, f.readline().split()))
print(rows, seats)

a = [[int(x.split()[0]), int(x.split()[1])] for x in f.readlines()]
a.sort(key=lambda x: [x[0], x[1]])
print(a)


def f(n):
    s = [0] * seats
    for row, seat in a:
        if row < n:
            s[seat - 1] = 1
    return s

print([0, 0] in [0, 0])
