n = int(input())
cnt = 0
for _ in range(n):
    x = int(input())
    if x % 2 == 0:
        print(x)
        cnt += 1
print(cnt)