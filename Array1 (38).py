n = int(input())
a = [int(input()) for _ in range(n)]
d = a[1] - a[0]
ok = all(a[i] - a[i - 1] == d for i in range(2, n))
print(d if ok else 0)