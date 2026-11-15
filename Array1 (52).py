n = int(input())
a = [int(input()) for _ in range(n)]
b = [x for x in a if x % 2 == 0] + [a[i] for i in range(n - 1, -1, -1) if a[i] % 2 != 0]
print(b)