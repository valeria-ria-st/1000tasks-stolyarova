n = int(input())
a = [float(input()) for _ in range(n)]
k = int(input())
print(a[k - 1::k])