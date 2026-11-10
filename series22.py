n = int(input())
prev = float(input())
ans = 0
for i in range(2, n + 1):
    x = float(input())
    if ans == 0 and x >= prev:
        ans = i
    prev = x
print(ans)