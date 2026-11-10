k = int(input())
n = int(input())
cnt = 0
for _ in range(k):
    has2 = False
    for _ in range(n):
        if int(input()) == 2:
            has2 = True
    if has2:
        cnt += 1
print(cnt)