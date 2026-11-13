n = int(input())
cur = 0
mx = 0
for _ in range(n):
    x = int(input())
    if x % 2 == 0:
        cur += 1
        if cur > mx:
            mx = cur
    else:
        cur = 0
print(mx)