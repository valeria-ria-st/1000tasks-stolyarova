n = int(input())
a = [float(input()) for _ in range(n)]
r = 0
for i in range(1, n - 1):
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        r = i + 1
print(r)