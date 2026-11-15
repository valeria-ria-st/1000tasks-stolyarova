n = int(input())
a = [int(input()) for _ in range(n)]
print(1 + sum(1 for i in range(1, n) if a[i] != a[i - 1]))