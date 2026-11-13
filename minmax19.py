n = int(input())
mn = float('inf')
cnt = 0
for _ in range(n):
    x = int(input())
    if x < mn:
        mn = x
        cnt = 1
    elif x == mn:
        cnt += 1
print(cnt)