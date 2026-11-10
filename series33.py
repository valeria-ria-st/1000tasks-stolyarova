k = int(input())
n = int(input())
for _ in range(k):
    ans = 0
    for i in range(1, n + 1):
        if int(input()) == 2:
            ans = i
    print(ans)