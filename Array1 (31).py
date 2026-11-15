n = int(input())
a = [float(input()) for _ in range(n)]
r = [i + 1 for i in range(1, n) if a[i] > a[i - 1]][::-1]
print(r, len(r))