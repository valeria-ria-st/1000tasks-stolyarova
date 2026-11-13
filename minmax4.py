n = int(input())
mx = float('-inf')
idx = 0
for i in range(1, n + 1):
    m = float(input())
    v = float(input())
    p = m / v
    if p > mx:
        mx = p
        idx = i
print(idx, mx)