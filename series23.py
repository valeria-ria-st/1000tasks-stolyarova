n = int(input())
a1 = float(input())
a2 = float(input())
ans = 0
prev2 = a1
prev1 = a2
for i in range(3, n + 1):
    x = float(input())
    if ans == 0 and not ((prev1 > prev2 and prev1 > x) or (prev1 < prev2 and prev1 < x)):
        ans = i - 1
    prev2 = prev1
    prev1 = x
print(ans)