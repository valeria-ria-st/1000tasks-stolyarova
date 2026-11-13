n = int(input())
a = []
for _ in range(n):
    a.append(float(input()))
a.sort(reverse=True)
print(a[0], a[1], a[2])