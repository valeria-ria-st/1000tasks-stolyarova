n = int(input())
a = [float(input()) for _ in range(n)]
r = []
for i in range(n):
    lo = i > 0 and i < n - 1 and a[i] < a[i - 1] and a[i] < a[i + 1]
    hi = i > 0 and i < n - 1 and a[i] > a[i - 1] and a[i] > a[i + 1]
    if not lo and not hi:
        r.append(a[i])
print(max(r) if r else 0)