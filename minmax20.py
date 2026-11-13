n = int(input())
mn = float('inf')
mx = float('-inf')
cnt_min = 0
cnt_max = 0
for _ in range(n):
    x = int(input())
    if x < mn:
        mn = x
        cnt_min = 1
    elif x == mn:
        cnt_min += 1
    if x > mx:
        mx = x
        cnt_max = 1
    elif x == mx:
        cnt_max += 1
print(cnt_min + cnt_max)