n = int(input())
a = [float(input()) for _ in range(n)]
r = [i + 1 for i in range(n - 1) if a[i] > a[i + 1]]
print(r, len(r))