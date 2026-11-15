n = int(input())
a = [float(input()) for _ in range(n)]
i1, i2 = min(((i, j) for i in range(n) for j in range(i + 1, n)), key=lambda p: abs(a[p[0]] - a[p[1]]))
print(i1 + 1, i2 + 1)