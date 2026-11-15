n = int(input())
a = [float(input()) for _ in range(n)]
b = []
s = 0
for i, x in enumerate(a):
    s += x
    b.append(s / (i + 1))
print(b)