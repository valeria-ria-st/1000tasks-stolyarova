r = float(input())
n = int(input())
a = [float(input()) for _ in range(n)]
i = min(range(n - 1), key=lambda i: abs(a[i] + a[i + 1] - r))
print(a[i], a[i + 1])