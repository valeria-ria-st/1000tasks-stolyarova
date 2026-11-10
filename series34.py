k = int(input())
n = int(input())
for _ in range(k):
    s = 0
    has2 = False
    for _ in range(n):
        x = int(input())
        s += x
        if x == 2:
            has2 = True
    print(s if has2 else 0)