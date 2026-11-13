n = int(input())
prev = float(input())
mn = float('inf')
idx1 = 0
idx2 = 0
for i in range(2, n + 1):
    x = float(input())
    p = prev * x
    if p < mn:
        mn = p
        idx1 = i - 1
        idx2 = i
    prev = x
print(idx1, idx2)