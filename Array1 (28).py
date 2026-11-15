n = int(input())
a = [float(input()) for _ in range(n)]
print(max(a[i] for i in range(1, n - 1) if a[i] < a[i - 1] and a[i] < a[i + 1]))