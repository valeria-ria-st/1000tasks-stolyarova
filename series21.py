n = int(input())
prev = int(input())
cnt = 0
for _ in range(n - 1):
    x = int(input())
    if x < prev:
        print(x)
        cnt += 1
    prev = x
print(cnt)