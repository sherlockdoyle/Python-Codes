n = int(input("Enter size: "))


def check(ar, i, j):
    for k in range(i):
        if ar[k][j]:
            return False
    i1 = i
    i2 = j
    while i1 >= 0 and i2 >= 0:
        if ar[i1][i2]:
            return False
        i1 -= 1
        i2 -= 1
    i1 = i
    i2 = j
    while i1 >= 0 and i2 < n:
        if ar[i1][i2]:
            return False
        i1 -= 1
        i2 += 1
    return True


def place(ar, i):
    for j in range(n):
        if check(ar, i, j):
            ar[i][j] = True
            if i < n - 1:
                if place(ar, i + 1):
                    return True
                else:
                    ar[i][j] = False
            else:
                return True
    return False


cb = [[0 for j in range(n)] for i in range(n)]
place(cb, 0)
for i in range(n):
    for j in range(n):
        print("Q " if cb[i][j] else ". ", end="")
    print()
