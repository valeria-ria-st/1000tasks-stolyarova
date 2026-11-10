k = int(input())
cnt = 0
for _ in range(k):
    a1 = int(input())
    a2 = int(input())
    zigzag = True
    prev2 = a1
    prev1 = a2
    while True:
        x = int(input())
        if x == 0:
            break
        if not ((prev1 > prev2 and prev1 > x) or (prev1 < prev2 and prev1 < x)):
            zigzag = False
        prev2 = prev1
        prev1 = x
    if zigzag:
        cnt += 1
print(cnt)