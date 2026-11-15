r = float(input())
n = int(input())
a = [float(input()) for _ in range(n)]
print(min(a, key=lambda x: abs(x - r)))