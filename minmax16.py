n = int(input())
mn = float('inf')
cnt = 0
for i in range(1, n + 1):
    x = int(input())
    if x < mn:
        mn = x
        cnt = i - 1
print(cnt)