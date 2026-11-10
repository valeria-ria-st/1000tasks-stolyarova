k = int(input())
cnt = 0
for _ in range(k):
    prev = int(input())
    increasing = True
    while True:
        x = int(input())
        if x == 0:
            break
        if x <= prev:
            increasing = False
        prev = x
    if increasing:
        cnt += 1
print(cnt)