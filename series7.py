n = int(input())
p = 1.0
for _ in range(n):
    x = float(input())
    fp = x - int(x)
    print(fp)
    p *= fp
print(p)