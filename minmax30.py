n = int(input())
a = [int(input()) for _ in range(n)]
mx = max(a)
mn = n
cur = 0
for x in a:
    if x == mx:
        cur += 1
    else:
        if 0 < cur < mn:
            mn = cur
        cur = 0
if 0 < cur < mn:
    mn = cur
print(mn)