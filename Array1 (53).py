n = int(input())
a = [int(input()) for _ in range(n)]
b = [a[i] for i in range(n - 1, -1, -1) if a[i] % 2 == 0]
print(b, len(b))