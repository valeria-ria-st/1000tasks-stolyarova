n = int(input())
a = [float(input()) for _ in range(n)]
k = int(input())
l = int(input())
b = a[:k - 1] + a[l:]
print(sum(b) / len(b))