n = int(input())
a = [float(input()) for _ in range(n)]
b = []
s = 0
for x in a:
    s += x
    b.append(s)
print(b)