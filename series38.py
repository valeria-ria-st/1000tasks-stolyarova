k = int(input())
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
    if inc:
        print(1)
    elif dec:
        print(-1)
    else:
        print(0)