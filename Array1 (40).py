n = int(input())
a = [float(input()) for _ in range(n)]
k = int(input())
l = int(input())
print(sum(a[:k - 1]) + sum(a[l:]))