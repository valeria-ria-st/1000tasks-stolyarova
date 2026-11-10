k = int(input())
cnt = 0
for _ in range(k):
    prev = int(input())
    inc = True
    dec = True
    while True:
        x = int(input())
        if x == 0:
            break
        if x <= prev:
            inc = False
        if x >= prev:
            dec = False
        prev = x
    if inc or dec:
        cnt += 1
print(cnt)