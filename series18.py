n = int(input())
prev = int(input())
cnt = 0
for _ in range(n - 1):
    x = int(input())
    if prev < x:
        print(prev)
        cnt += 1
    prev = x
print(cnt)