n = int(input())
a = [float(input()) for _ in range(n)]
i = max(range(n - 1), key=lambda i: a[i] + a[i + 1])
print(a[i], a[i + 1])