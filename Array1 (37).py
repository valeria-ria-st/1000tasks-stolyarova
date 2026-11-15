n = int(input())
a = [int(input()) for _ in range(n)]
ok = True
for i in range(2, n):
    if a[i] * a[0] != a[i - 1] * a[1]:
        ok = False
print(a[1] // a[0] if ok and a[1] % a[0] == 0 else 0)