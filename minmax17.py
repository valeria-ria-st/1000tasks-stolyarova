n = int(input())
mx = float('-inf')
last_max = 0
for i in range(1, n + 1):
    x = int(input())
    if x >= mx:
        mx = x
        last_max = i
print(n - last_max)