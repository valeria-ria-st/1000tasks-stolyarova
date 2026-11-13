n = int(input())
mn = float('inf')
idx = 0
for i in range(1, n + 1):
    x = float(input())
    if x < mn:
        mn = x
        idx = i
print(idx)