n = int(input())
a = [int(input()) for _ in range(n)]
r = 0
for i in range(1, n):
    if a[i] % 2 == a[i - 1] % 2:
        r = i + 1
        break
print(r)