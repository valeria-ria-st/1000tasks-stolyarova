n = int(input())
a = [float(input()) for _ in range(n)]
c = 0
i = 1
while i < n:
    if a[i] < a[i - 1]:
        c += 1
        while i < n and a[i] < a[i - 1]:
            i += 1
    else:
        i += 1
print(c)