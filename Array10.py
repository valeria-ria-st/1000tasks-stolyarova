n = int(input())
a = [float(input()) for _ in range(n)]
b = [float(input()) for _ in range(n)]
print([max(x, y) for x, y in zip(a, b)])