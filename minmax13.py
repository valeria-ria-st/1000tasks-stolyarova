n = int(input())
mx = float('-inf')
idx = 0
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0 and x > mx:
        mx = x
        idx = i
print(idx)