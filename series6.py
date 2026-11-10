n = int(input())
s = 0
for _ in range(n):
    x = float(input())
    r = int(x + 0.5) if x >= 0 else -int(-x + 0.5)
    print(r)
    s += r
print(s)