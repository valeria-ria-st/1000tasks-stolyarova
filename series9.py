n = int(input())
cnt = 0
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        print(i)
        cnt += 1
print(cnt)