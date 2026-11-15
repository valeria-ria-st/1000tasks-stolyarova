n = int(input())
a = [float(input()) for _ in range(n)]
print(a[0::2] + a[n - 1:0:-2])