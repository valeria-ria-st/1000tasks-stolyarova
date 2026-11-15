n = int(input())
a = [float(input()) for _ in range(n)]
print(a[1::2] + a[0::2])