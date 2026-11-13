n = int(input())
a = [int(input()) for _ in range(n)]
mn = min(a)
mx = 0
cur = 0
for x in a:
    if x == mn:
        cur += 1
        if cur > mx:
            mx = cur
    else:
        cur = 0
print(mx)